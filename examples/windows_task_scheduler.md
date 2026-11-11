# Running the agent on a schedule (Windows Task Scheduler)

Run it two or three times a day, not every minute. The cheap pre-check means a quiet run costs almost nothing.

## Create the task (PowerShell, run as the user who owns the mailbox)

```powershell
$action  = New-ScheduledTaskAction -Execute "python" `
  -Argument "C:\TriageAgent\examples\triage_skeleton.py --dry-run" `
  -WorkingDirectory "C:\TriageAgent"
$times   = @("09:15","13:15","17:15")
$triggers = $times | ForEach-Object { New-ScheduledTaskTrigger -Daily -At $_ }
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable `
  -ExecutionTimeLimit (New-TimeSpan -Minutes 20) -MultipleInstances IgnoreNew
Register-ScheduledTask -TaskName "EmailTriageAgent" `
  -Action $action -Trigger $triggers -Settings $settings `
  -Description "Read-only email triage (L0)"
```

Notes:

- `-StartWhenAvailable` runs a missed slot when the computer wakes up.
- `-MultipleInstances IgnoreNew` stops two runs overlapping.
- `-ExecutionTimeLimit` kills a stuck run.
- Keep `--dry-run` until you have reviewed several runs.

## Secrets

Set the environment variable names from config.example.yaml as user-level environment variables, or read them from Windows Credential Manager. Never put them in the task definition, the script, or this repo.

```powershell
[Environment]::SetEnvironmentVariable("TRIAGE_MAILBOX", "<set this yourself>", "User")
```

## Check that it ran

```powershell
Get-ScheduledTaskInfo -TaskName "EmailTriageAgent"
```

Look at the last run result and compare it with the start and end lines in logs. A start with no end means the run crashed.

## Stop it

```powershell
Disable-ScheduledTask -TaskName "EmailTriageAgent"
```
