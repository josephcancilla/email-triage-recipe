# Rule Book Template

Fill this in with your agent during the interview. Placeholders in angle brackets are yours to replace. The agent must only use folders and categories listed here. It must never invent new ones.

## 1. Your folders and categories

| Placeholder | Your real name | Notes |
|-------------|----------------|-------|
| <FOLDER: Clients> | | Client correspondence already logged |
| <FOLDER: Carriers> | | Carrier and underwriting notices |
| <FOLDER: Renewals> | | Renewal reminders and renewal workflow mail |
| <FOLDER: Claims> | | Claims mail already logged |
| <FOLDER: Certificates> | | Certificate request threads that are done |
| <FOLDER: Newsletters> | | Newsletters you do not need to read |
| <FOLDER: Vendors> | | Vendor and software mail |
| <FOLDER: Receipts> | | Receipts and invoices (never archive blindly) |
| <FOLDER: Archive> | | Anything handled with no better home |

Rule: if a message has no obvious home, leave it in the inbox and flag it.

## 2. Never-touch list (always stays in the inbox)

- Flagged or starred messages.
- Unread mail from a real person.
- Anything mentioning: <WORDS: cancel, non-renewal, lapse, past due, audit, legal, subpoena, claim deadline>
- Anything from: <SENDERS: your top clients, your attorney, your accountant, your E&O carrier>
- Money that failed or is overdue.

## 3. Class rules (example rows, replace with yours)

| Email looks like | Class | CRM action | Then | Notes |
|------------------|-------|------------|------|-------|
| Carrier sends a policy notice (new business issued, endorsement processed) | Info to file | Log to the policy record | Label, move to <FOLDER: Carriers> | Read it: a cancellation or non-renewal notice is protected, not filed |
| Automated renewal reminder from a carrier or your AMS | Robot noise | Log if it names a client | Move to <FOLDER: Renewals> | Reminder does not replace the human renewal review |
| Client asks for a quote | Needs reply | Log to the client record | Stays in inbox, optional draft | Never quote figures in a draft |
| Client sends an update (new address, new vehicle, new driver) | Info to file, scope change | Hold for a human to update the record first | Stays in inbox until applied | Scope-change hold applies |
| Client reports a claim or loss | Needs reply | Log to the client and claim record | Stays in inbox, alert once | Never auto-file, never auto-reply |
| Certificate request from a client or a third party | Needs reply | Log to the client record | Stays in inbox until the certificate is sent | Draft only, human sends |
| Certificate issued confirmation (our own sent mail) | Info to file | Log to the client record | Move to <FOLDER: Certificates> | |
| Login code, one-time passcode | Robot noise | None | Archive | A code never needs a reply |
| Payment receipt or invoice | Robot noise | Log if tied to a client | Move to <FOLDER: Receipts> | Never archive without filing |
| Newsletter from a carrier, trade group or software company | Robot noise | None | Move to <FOLDER: Newsletters> | Exceptions: <NEWSLETTERS I READ> |
| Cold sales pitch from a vendor | Pitch | None | Move to <FOLDER: Vendors> | Later: auto-reply lane |
| Someone says stop emailing me | Opt-out | Add to do-not-contact list | File, no reply | Hard stop forever |
| A teammate already replied to the thread | Handled | Log if not logged | File | Do not draft |

## 4. Matching rules (finding the CRM record)

1. Sender email address matches a client contact.
2. Policy number or account number appears in the subject or body.
3. Client or business name matches exactly.
4. Two signals must agree before the match counts as confirmed.
5. Where to search first: <CRM: object or list name>
6. Where to write the note: <CRM: field or activity type>

## 5. Voice and compliance for any outbound

- Tone: <e.g. warm, plain, short>
- Required sign-off: <SIGN-OFF>
- Banned: coverage promises, binding language, quote figures, claim outcome predictions, <YOUR OWN>
- Always route through: the lint check in SAFETY_GATES.md.

## 6. Who handles what

| Person | Handles | Counts as "handled" if they replied? |
|--------|---------|--------------------------------------|
| <PERSON A> | <e.g. personal lines> | Yes |
| <PERSON B> | <e.g. commercial lines> | Yes |

## 7. Alerts

- Where alerts go: <CHANNEL>
- Quiet hours: <START> to <END>
- Always alert for: <e.g. lapse notice, claim, legal>
