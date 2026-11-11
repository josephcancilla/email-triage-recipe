# Email Triage Agent Recipe

A pattern for an AI agent that works your inbox down to only the email that still needs you. It reads each thread, writes down what happened in your client system, files the email, and leaves the rest alone.

This repo is a recipe, not a finished product. It contains no code you must run and no credentials. You hand it to your own commander agent (the Claude Code agent you already run), and that agent builds a version tailored to your inbox, your CRM and your rules.

## What the agent does, in plain English

1. Checks whether there is any new mail. If not, it stops. No model call, no cost.
2. Pulls recent email threads.
3. Skips anything it should never touch (flagged mail, unread mail from a real person, money, legal, "action required").
4. Reads the whole thread and decides what it is: needs a reply, information to file, robot noise, a sales pitch, or an opt-out.
5. Finds the matching client or policy record in your CRM. It checks for an existing record before ever creating one.
6. Writes what the email said into that record, word for word.
7. Only after the record is saved, it labels the email, moves it to a folder, and archives it.
8. Optionally drafts replies for you to approve. It never sends on its own at first.
9. Reports what it did, in a short summary.

The inbox ends up holding only what still needs a human.

## What is in this repo

| File | What it is |
|------|-----------|
| RECIPE.md | The full pipeline, step by step, with the ordering rules |
| SAFETY_GATES.md | Guardrails: what the agent must never do |
| TRUST_LADDER.md | How the agent earns more freedom, one level at a time |
| RULES_TEMPLATE.md | A fill-in rule book with insurance agency examples |
| LESSONS_TEMPLATE.md | How to turn a correction into a lesson the agent reads next run |
| examples/triage_skeleton.py | A stubbed Python skeleton (no network, no credentials) |
| examples/config.example.yaml | Placeholder settings |
| examples/windows_task_scheduler.md | How to run it on a schedule on Windows |

## How to hand this to your agent

Open your commander agent in this folder and paste this:

> Read every file in this repo. Interview me in rounds of 3 questions about my inbox, my CRM, my folders and my rules. Then build me a read-only triage agent at L0 following RECIPE.md. Do not let it send, delete, or archive anything until I approve.

Then answer the questions. Short answers are fine. If you do not know, say so and the agent should pick the safest default.

Things your agent will want to know:

- Which mailboxes (yours, your partner's, a shared one) and whether they are Microsoft 365 / Outlook.
- Which CRM or agency system holds your clients (for example HubSpot, Salesforce, a SharePoint list, or an AMS).
- Which folders you already use, and which you wish you had (the agent must not invent folders on its own).
- Which senders are always noise, always important, or must never be touched.
- Who on your team handles what, so a teammate's reply counts as "handled".

## Suggested build order

1. Interview (the prompt above). Agent writes down your answers in a rule book (RULES_TEMPLATE.md).
2. Connect to the mailbox read-only (Microsoft Graph, mail read permission only).
3. Connect to the CRM read-only. Prove it can find a client by email address.
4. Build the classifier and run it on 20 old emails. Compare with your own judgment.
5. Run daily at L0 (it only reports what it would do). You review.
6. Turn on CRM logging (write access to one note field). Still no email changes.
7. Turn on labeling and filing. Archive last, and only for mail that was logged.
8. Add reply drafts. You approve every one.
9. Later: add the vendor and applicant auto-reply lane.

## Start read-only, add one rule a day

Do not try to build the whole thing in a day. Start with an agent that can only look and report. Each day, add exactly one rule (for example "carrier notices go to the Carriers folder") and watch one full run. When a run goes well three times, move up a level (see TRUST_LADDER.md). When it makes a mistake, write a one-line lesson (see LESSONS_TEMPLATE.md) and drop back a level.

A slow, boring rollout is the whole point. The agent should earn trust the way a new hire does.
