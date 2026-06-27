# n8n Business Automation Workflows

[![CI](https://github.com/emirhuseynrmx/n8n-business-automation-workflows/actions/workflows/ci.yml/badge.svg)](https://github.com/emirhuseynrmx/n8n-business-automation-workflows/actions)

Tested n8n workflow templates for small-business automation.

Built for simple, practical workflows: forms, emails, sheets, alerts, AI summaries, and lead routing. Each workflow is intentionally small enough to customize quickly.

## Workflows

| Workflow | Use case |
| --- | --- |
| `lead_form_to_sheets.json` | Capture web form leads and append them to Google Sheets |
| `email_to_ai_summary.json` | Summarize inbound emails and send a short digest |
| `telegram_alert_router.json` | Route business alerts to Telegram |
| `daily_sales_digest.json` | Read rows from Sheets and send a daily summary |

`workflow_catalog.json` describes each template, its use case, and required credentials.

## How To Use

1. Import a workflow JSON file into n8n.
2. Replace placeholder credentials.
3. Configure the environment variables listed in `.env.example`.
4. Run the workflow manually once.
5. Enable the trigger when the test output looks correct.

## Validation

This repo includes tests that verify every workflow JSON file has:

- workflow name
- active flag
- nodes
- connections
- pinned metadata notes for customization
- Pydantic schema-valid workflow structure
- catalog entries that point to real workflow files

```bash
pip install -e ".[dev]"
ruff check .
pytest
```

## Scope

These templates are starting points. They avoid account bypassing, credential sharing, and unsafe scraping. Use official APIs and user-owned accounts.
