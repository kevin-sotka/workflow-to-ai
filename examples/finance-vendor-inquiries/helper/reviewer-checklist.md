# Reviewer checklist: vendor payment inquiry helper

*Built from the failure modes found in testing. Takes about one minute per draft.*

1. **Invoice number:** does the number in "For the reviewer" match the vendor's email? Watch for REM- and PO- numbers.
2. **Status and date:** do they match the report row cited?
3. **Holds:** if the status is On hold, is there no payment date anywhere in the reply?
4. **Every question:** did the draft answer or route every question in the email, including ones buried lower in a thread?
5. **Nothing changed:** does the reply avoid confirming any bank, address, or contact change?
6. **Tone:** would you be comfortable if this vendor forwarded it to your manager?

If any check fails: fix it, or click Escalate. Log anything new in the failure log so it becomes a test case.
