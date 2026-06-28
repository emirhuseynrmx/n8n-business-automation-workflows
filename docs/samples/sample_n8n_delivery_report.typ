#set page(margin: 42pt)
#set text(font: "Arial", size: 10pt)
#set heading(numbering: none)

#let accent = rgb("#1457d9")
#let good = rgb("#11845b")
#let muted = rgb("#667085")
#let panel = rgb("#f6f8fb")

#let stat(label, value, color: accent) = block[
  #rect(fill: panel, radius: 5pt, inset: 10pt, width: 100%)[
    #text(size: 8pt, fill: muted, weight: "bold")[#upper(label)]
    #linebreak()
    #text(size: 18pt, fill: color, weight: "bold")[#value]
  ]
]

= n8n Automation Delivery Report

#text(fill: muted)[
  Sample handoff report for small-business automation workflows. The templates
  are designed for forms, emails, sheets, alerts, summaries, and lead routing.
]

#grid(columns: (1fr, 1fr, 1fr, 1fr), gutter: 8pt)[
  #stat("Workflows", "4")
][
  #stat("Schema checks", "Pydantic")
][
  #stat("Credentials", "Placeholders")
][
  #stat("Import-ready", "Yes", color: good)
]

== Workflow Catalog

#table(
  columns: (1.3fr, 2fr),
  inset: 5pt,
  stroke: rgb("#d0d5dd"),
  [*Workflow*], [*Use Case*],
  [lead_form_to_sheets], [Capture web form leads and append rows to Google Sheets],
  [email_to_ai_summary], [Summarize inbound emails and send a short digest],
  [telegram_alert_router], [Route business alerts to Telegram],
  [daily_sales_digest], [Send a scheduled sales summary from spreadsheet rows],
)

== Handoff Checklist

- Workflow JSON files are import-ready.
- Placeholder credentials are easy to replace.
- Catalog entries point to real workflow files.
- Tests verify workflow names, nodes, connections, and metadata notes.

== Scope Notes

- Use official APIs and user-owned accounts.
- Avoid credential sharing, account bypassing, and unsafe scraping.
