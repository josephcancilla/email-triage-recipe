# The Pipeline

This is the full order of operations. Build it in this order and keep the order. Most of the safety comes from the sequence.

## The three ordering rules

1. **Record first, label second, archive last.** Never label or archive an email until the note about it is saved and confirmed in your CRM.
2. **Never archive what was not logged.** If logging failed, the email stays in the inbox. A visible mess beats a hidden loss.
3. **Never delete email.** Not ever. The agent has no delete capability. Archive is the strongest move it has, and only late in the ladder.

## Stage 0: cheap pre-check (no new mail, no model call)

Before anything else, ask the mailbox a plain question: is there any mail newer than the last successful run, or any thread still waiting to be filed? If not, write a one-line "nothing to do" receipt and exit.

This is ordinary code, not an AI call. It keeps costs near zero and keeps the agent quiet.

## Stage 1: fetch recent threads

Pull whole threads (not single messages). With Microsoft Graph, fetch messages from the inbox and group them by conversation id so you see the full back and forth. Keep a small state file of thread ids already handled and the last time you saw them change, so a thread is reprocessed only when something new arrives.

## Stage 2: skip and protect rules

Run these cheap checks before spending any model time. If any one matches, leave the thread exactly where it is and note why.

- Flagged or starred (the human marked it on purpose).
- Unread mail from a real person. Unread human mail never leaves the inbox.
- Money, legal or "action required" mail: payment failed, past due, cancellation notice, lapse, audit, subpoena, claim deadline.
- A thread where the last message is from a real person waiting on a reply.
- Anything on your "never touch" sender list.

Protection beats every other rule. If protection and a filing rule disagree, protection wins.

## Stage 3: read the WHOLE thread, then classify

Read every message in the thread, oldest to newest, including what your team already sent. Then pick one class:

| Class | Meaning | Default action |
|-------|---------|----------------|
| Needs reply | Someone asked something nobody has answered | Stays in inbox (optionally drafts a reply) |
| Info to file | Update, FYI, document drop, thank-you | Log to record, then file |
| Robot noise | Receipts, login codes, system notices, no-reply mail | Log if useful, then file or archive |
| Pitch | Cold sales outreach | File or archive; later, auto-reply lane |
| Opt-out | "Stop emailing me", "unsubscribe me" in a person's own words | Hard stop (see below) |

### Judge the email, not the sender

A filing rule based only on who sent it cannot tell an update from a question. A client can send a plain update that needs no reply. A vendor can send something urgent. Read the email itself and decide from what it says and what is still open in the thread.

### A teammate's reply counts as handled

If you or a teammate already answered after the last inbound message, or someone already logged it in the CRM, the thread is not waiting on you. No reply draft, no alert.

### Do not guess

Low confidence means leave it in the inbox and say so in the report. The agent may only act when it is highly confident.

## Stage 4: match to a CRM record (dedup first)

Search the CRM for the right record: sender email address first, then policy number, then client name, then thread subject. Rules:

- **Check before you create.** Search at least two ways before creating anything. Duplicate client records are expensive to clean up.
- If there are zero matches, do not create a record automatically at first. Report it and let the human decide.
- If there are several plausible matches, do not pick one. Report them.
- A match is "confirmed" only when at least two signals agree (for example the email address and the policy number).

## Stage 5: log to the record, verbatim

Write the email into the record: who, when, subject, and the actual text (quoted history trimmed). Attach any files to the record. Do not paraphrase away facts such as dates, policy numbers, coverage details or names. Mark the entry with the date and the fact that the agent logged it.

Verify the write by reading it back. If the read-back fails, stop for this thread.

## Stage 6: label, file, archive (only now)

In this order, and only if Stage 5 succeeded:

1. Apply the label or category (a label that claims "logged" must only exist after the log is true).
2. Move the message to the matching folder (Outlook: move to the folder id, or set a category).
3. Archive last (in Outlook, move out of the inbox to the target folder or the archive folder).

Never create new folders or categories. If the folder in your rule does not exist, drop the filing step and warn. The human owns the folder system.

### Scope-change hold

If a client email changes something material (add a driver, change an address, cancel or add coverage, change a limit, change a payment date), do not just file it. The change must be applied to the record by a human (or an approved update step) first. Until then the email stays in the inbox, marked as a held change. Information a vendor or third party needs is flagged for follow-through, never auto-sent.

## Stage 7: optional reply drafts

Not at the start. When you get there:

- Draft only. Never send. A draft appears in the Drafts folder for a human to review.
- Only for threads classified "needs reply" that a teammate has not already handled.
- Run the voice lint (SAFETY_GATES.md) before saving the draft.

## Stage 8: report

End every run with a short report: how many threads seen, how many logged, filed, left alone and why, anything that failed, anything that needs a human. Plain English, answer first. Also write a run receipt (start and end) so a silent failure is visible.

## Opt-out is a hard stop, forever

If a person writes, in their own words, something like "do not email me", "unsubscribe me", or "take me off your list":

- Add their address to the do-not-contact list. If the message speaks for an organization ("take us off your list"), add the whole domain.
- No agent or automation sends them anything again, on any channel.
- Detect it from the human's own typed text, with quoted history and signature stripped. Do not match on the word "unsubscribe" in a footer: nearly every marketing email contains it. Bulk mail advertises itself in headers (List-Unsubscribe, List-Id, bulk precedence), so treat those as never an opt-out by the footer alone.
- When unsure, stop sending. Stopping someone who did not quite mean it costs one lead. Emailing someone who asked twice costs the relationship.
- Every send path checks the list (To, CC and BCC), and if the list cannot be read, the send is refused.

## Later add-on: vendor and applicant auto-reply lane

Once the basics have run cleanly for a while, add a narrow lane for cold pitches from vendors, performers, freelancers or job applicants. Instead of the human replying, the agent sends one canned, brand-checked reply pointing them to your official registration or application link, logs it, and files the thread. Rules for this lane:

- Only for mail classified as a pitch or application, never for clients, carriers or anyone already in the CRM.
- One reply per sender, ever (keep a handled list).
- Do not run it until the agent is at the auto-send level for that lane (TRUST_LADDER.md).
- The reply text is fixed and approved by you. The model chooses whether to use it, not what it says.

## Microsoft 365 / Outlook notes

- Use Microsoft Graph. Start with read-only mail scope (Mail.Read). Add Mail.ReadWrite only when you reach filing. Do not request send scope until much later.
- Register the app in your own tenant and get an administrator to grant consent. Store the client id, tenant id and secret in environment variables or Windows Credential Manager, never in a file in this repo.
- Group by conversationId to get whole threads. Use the message "isRead" and "flag" fields for the protection rules.
- Outlook "categories" are the closest thing to labels. Folders are real folders. Use move, never delete.
- For delta runs, use Graph delta queries on the inbox so the pre-check is cheap.
- If your agency uses a shared mailbox, remember that "a teammate replied" means checking Sent Items of every person who works that mailbox.
- Respect throttling: back off on HTTP 429 and honor the Retry-After header.
