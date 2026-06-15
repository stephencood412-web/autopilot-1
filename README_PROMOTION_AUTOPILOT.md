# Autopilot promotion scaffold

This repository includes a minimal, free automation scaffold to run scheduled promotional tasks from GitHub Actions.

What it does
- Posts a message to Mastodon (if `MASTODON_TOKEN` + `MASTODON_BASE_URL` are set as repo secrets).
- Sends a simple email via SMTP (if `SMTP_HOST`, `SMTP_USER`, `SMTP_PASS`, etc. are set).
- Runs on a daily schedule (09:00 UTC) and can be manually triggered.

Files created
- `.github/workflows/schedule.yml` — cron + manual trigger workflow.
- `scripts/post_mastodon.py` — simple Mastodon poster.
- `scripts/send_email.py` — simple SMTP email sender.
- `content/scheduled/post1.md` — example message used by the jobs.
- `requirements.txt` — Python dependencies.

Setup (GitHub repository)
1. In your repository Settings → Secrets → Actions, add the secrets you want to use:
   - `MASTODON_BASE_URL` (e.g. https://mastodon.social)
   - `MASTODON_TOKEN` (user access token)
   - `SMTP_HOST` (e.g. smtp.gmail.com)
   - `SMTP_PORT` (587)
   - `SMTP_USER` (SMTP username / email)
   - `SMTP_PASS` (app password)
   - `EMAIL_TO` (recipient list; comma separated)
   - `EMAIL_FROM` (from address)
2. Edit `content/scheduled/post1.md` with the text you want posted/sent.
3. Trigger the workflow from the Actions tab to run a dry run.

Notes & limitations
- This scaffold uses free GitHub Actions minutes (public repos have more generous limits).
- Twitter/X requires paid API access for posting and isn't included here.
- Amazon Ads and reporting require paid APIs/credentials and are not automated in this free scaffold.

Next steps I can take
- Add more scheduled messages and rotation logic.
- Add logging and retry logic.
- Add GitHub Pages publishing for blog posts and link-tracking.
