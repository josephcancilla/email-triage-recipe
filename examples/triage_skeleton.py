#!/usr/bin/env python3
"""Provider-agnostic email triage skeleton. Stdlib only. No network, no credentials.

Every stub below is where your commander agent wires in a real mailbox (for
example Microsoft Graph) and a real CRM. Config comes from environment variable
NAMES only. Run with --dry-run to see the flow without side effects.
"""
import argparse
import json
import os
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone

ENV_NAMES = ["TRIAGE_MAILBOX", "TRIAGE_CRM_URL", "TRIAGE_CRM_TOKEN"]  # names only
CLASSES = ["needs_reply", "info_to_file", "robot_noise", "pitch", "opt_out"]
PROTECT_WORDS = ["cancel", "non-renewal", "lapse", "past due", "audit", "legal"]


@dataclass
class Thread:
    thread_id: str
    subject: str
    messages: list  # oldest to newest: {"from","body","is_read","flagged","is_teammate"}
    labels: list = field(default_factory=list)


def has_new_mail(last_run_iso: str) -> bool:
    """Cheap pre-check. No new mail means no model call. STUB."""
    return True


def fetch_threads(limit: int) -> list:
    """Fetch recent whole threads (group by conversation id). STUB: returns samples."""
    return [
        Thread("t1", "Renewal reminder", [{"from": "carrier", "body": "Your renewal is due.",
               "is_read": True, "flagged": False, "is_teammate": False}]),
        Thread("t2", "Question about my policy", [{"from": "client", "body": "Can you call me?",
               "is_read": False, "flagged": False, "is_teammate": False}]),
    ][:limit]


def is_protected(t: Thread) -> str:
    """Return a reason string if the thread must be left alone, else ''."""
    last = t.messages[-1]
    if last["flagged"]:
        return "flagged"
    if not last["is_read"] and not last["from"].endswith("-robot"):
        return "unread human mail"
    text = " ".join(m["body"].lower() for m in t.messages) + t.subject.lower()
    if any(w in text for w in PROTECT_WORDS):
        return "money/legal/action-required keyword"
    return ""


def teammate_already_replied(t: Thread) -> bool:
    return t.messages[-1]["is_teammate"]


def classify(t: Thread) -> tuple:
    """Read the WHOLE thread, return (class, confidence). STUB: replace with a model call."""
    body = " ".join(m["body"].lower() for m in t.messages)
    if "unsubscribe me" in body or "do not email" in body:
        return "opt_out", 0.9
    if "reminder" in t.subject.lower():
        return "robot_noise", 0.9
    return "needs_reply", 0.5


def match_record(t: Thread):
    """Search the CRM two ways before concluding. Return record id or None. STUB."""
    return None


def log_to_record(record_id: str, t: Thread) -> bool:
    """Write the thread verbatim to the record, read it back, return True only if confirmed. STUB."""
    return False


def file_thread(t: Thread, folder: str) -> bool:
    """Label, then move. Never delete. Never invent a folder. STUB."""
    return False


def process(t: Thread, dry_run: bool) -> dict:
    out = {"thread": t.thread_id, "action": "left_alone", "why": ""}
    why = is_protected(t)
    if why:
        out["why"] = f"protected: {why}"
        return out
    if teammate_already_replied(t):
        out["why"] = "teammate already replied (handled)"
        return out
    cls, conf = classify(t)
    out["class"] = cls
    if cls == "opt_out":
        out.update(action="add_to_do_not_contact", why="hard stop")  # human reviews at L0
        return out
    if conf < 0.8 or cls == "needs_reply":
        out["why"] = "low confidence or needs reply, stays in inbox"
        return out
    record = match_record(t)
    if not record:
        out["why"] = "no confirmed CRM match, stays in inbox"
        return out
    if dry_run:
        out.update(action="would_log_then_file", why=f"record {record}")
        return out
    if log_to_record(record, t):          # 1. record first
        file_thread(t, "<FOLDER: Archive>")  # 2. label/file, 3. archive last
        out["action"] = "logged_and_filed"
    else:
        out["why"] = "log not confirmed, stays in inbox (fail closed)"
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="no writes of any kind")
    ap.add_argument("--limit", type=int, default=50)
    args = ap.parse_args()
    missing = [n for n in ENV_NAMES if not os.environ.get(n)]
    if missing and not args.dry_run:
        print("Missing environment variables:", ", ".join(missing), file=sys.stderr)
        return 2  # fail closed
    start = datetime.now(timezone.utc).isoformat()
    print(json.dumps({"event": "run_start", "at": start, "dry_run": args.dry_run}))
    if not has_new_mail("last-run-timestamp"):
        print(json.dumps({"event": "run_end", "note": "nothing to do"}))
        return 0
    results = [process(t, args.dry_run) for t in fetch_threads(args.limit)]
    for r in results:
        print(json.dumps(r))
    print(json.dumps({"event": "run_end", "threads": len(results)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
