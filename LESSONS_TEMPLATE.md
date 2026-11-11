# Lessons Template

Every time you correct the agent, write the correction as one line. The agent reads this file at the start of every run, before it classifies anything. A lesson is short, specific, and says what to do, not just what went wrong.

## How to write a lesson

One line, this shape:

`<date> | <what the agent did> -> <what it should do> | <why>`

Good lessons are small and concrete. Bad lessons are long stories. If a lesson keeps getting broken, promote it into a real rule in RULES_TEMPLATE.md, or into a code check.

Keep the file short. Every few weeks, merge duplicates and retire lessons that are now rules.

## Where to put corrections

Whoever notices the mistake (you, your partner, or the verifier) appends a line. The agent never deletes lessons. A human prunes.

## Example lessons (generic starting set)

1. `A login code or one-time passcode never needs a reply. File it as noise.`
2. `A teammate's reply means the thread is handled. Do not draft a reply and do not alert.`
3. `Do not create a "needs reply" folder. If it needs a reply, it stays in the inbox.`
4. `Marketing email from a software company is not a request, even if the subject has a question mark. Classify it as noise, not needs-reply.`
5. `A client update (new address, new vehicle) is information to file, not a reply to write. But it is a scope change, so hold it for the record update.`
6. `Judge the email, not the sender. A client can send noise and a vendor can send something urgent. Read the thread.`
7. `Do not write a comment on a record unless the match is confirmed. When two records could fit, report both and stop.`
8. `A "from" address that says no-reply may still carry an action required notice. Read it before archiving.`

## Starter file for your agent

Copy this into a file named LESSONS.md in your agent's own folder and let the agent append to it:

```
# Lessons (newest first)
- <date> | <what happened> -> <what to do instead> | <why>
```
