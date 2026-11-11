# Trust Ladder

The agent does not start with freedom. It earns it, one level at a time, by being right in front of you.

| Level | Name | What it may do | Gate to reach it |
|-------|------|----------------|------------------|
| L0 | Draft only | Reads, classifies, and shows you what it would do. Changes nothing. | Default for a new agent |
| L1 | Staged | Prepares the actions (log note, label, move, reply draft) and queues them. A human approves each batch. | 3 clean passes at L0 |
| L2 | Auto | Does the approved kinds of action itself (log, label, file, archive) when highly confident. Still no free-form sending. | 3 clean passes at L1 and an independent check |
| L3 | Autonomous | Acts and reports afterwards, including lanes like the vendor auto-reply. | 3 clean passes at L2 and an independent check |

## What counts as a clean pass

One full run (or one day) where a human or an independent verifier checked the agent's decisions against the real emails and found no mistakes of consequence. A near miss is not clean. Three clean passes in a row move it up one level.

## Demotion

- One serious mistake (a wrongly archived email, a record logged to the wrong client, an email that should have been protected): drop one level.
- Two mistakes in one week: drop two levels.
- Anything involving an opt-out, a legal or coverage matter, or money: drop to L0 and find the cause before going back up.
- After a demotion, write the lesson (LESSONS_TEMPLATE.md) before the agent runs again.

## The agent never grades itself

An agent that marks its own homework will pass itself. Grading is done by one of:

- You, spot-checking a sample of the run.
- A separate verifier agent that has no memory of the run, is told to assume the work is wrong, and has to find evidence from the real mailbox and the real CRM.

Both the pass count and the promotion should be recorded somewhere the agent cannot edit. The agent may report what it did. It does not decide whether that was good.

## Per lane, not just per agent

Trust can differ by action. A reasonable starting point:

- Logging to the CRM and labeling: can reach L2 early.
- Archiving: later than labeling.
- Reply drafts: stay at L0 or L1 for a long time.
- Sending anything, including auto-replies: last, one narrow lane at a time, with a lint gate.

## Keeping a human veto

Whatever the level, you can demote the agent, pause it, or put a sender or a whole lane on a "never automate" list at any time. Every promotion is announced to you in the daily report, not silently applied.
