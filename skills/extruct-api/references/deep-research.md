# Deep Research Playbook

Deep Research turns a free-text brief about one research target — a company, a person, or a team — into a cited report.
A reasoning agent plans the research, fans out research agents that gather evidence,
and synthesizes the result. This playbook covers writing briefs, choosing depth,
designing output schemas, and reading reports honestly.

## When this path, when another

- One target, deep sourced report (account plan, buyer research, diligence): Deep Research.
- A person or team — research a lead before outreach or a meeting: Deep Research.
- Many companies matching criteria: Deep Search.
- The same questions across a list of companies, repeatably: a company table.
- One company's profile facts, instantly: company lookup.

## Write the brief like a request to an analyst

Good briefs are detailed paragraphs that name the target, the requester's own context,
and the decision the report should support. One-liners produce unfocused reports.

- Good: "We sell a cloud cost-optimization platform to large enterprises; typical
  buyers are VPs of Infrastructure and FinOps leads. I am preparing outreach to Shell.
  Research how Shell's IT and digital organization is structured, who owns cloud
  infrastructure and FinOps decisions, which cloud, data, or efficiency initiatives
  they announced in the last 18 months, and which vendors or system integrators they
  already work with. I want practical conversation angles tied to live initiatives,
  plus any signals of cost-cutting programs or budget pressure."
- Good: "We are a seed-stage investor evaluating Acme Robotics for a follow-on round.
  Build a diligence brief: funding history and investors, key customers and revenue
  signals, the competitive landscape for warehouse automation, recent leadership
  changes, and open risks we should pressure-test in the partner meeting."
- Good: "Here is my company: example.com. We sell AI-powered sales-enablement software to mid-market B2B teams. Research this person and the team they work with: https://www.linkedin.com/in/example-profile. I want their role and scope, what their team owns, recent initiatives or public statements, tools they already use, and the best angle to open a conversation."
- Bad: "Help me break into Shell." (no context about what you sell or who you target)
- Bad: "Tell me about Stripe." (no decision to support; the report will be unfocused)

Include everything the research agents cannot guess: what you sell, who your buyer is,
the angle you care about, time windows when freshness matters, what you already know.
For people targets, include the LinkedIn profile URL (or full name plus company) and
your own company and offer — the report is only as targeted as the brief.
The brief can be long (up to 20,000 characters) — pasting context is encouraged, and
more specific briefs reliably produce better reports.

Vague-but-valid briefs run; truly targetless or unusable briefs are rejected
asynchronously with suggestions in `failure_reason`, and nothing is charged.

## Choose depth deliberately

- `medium` (25 agents): default. Right for most account plans and single-question research.
- `high` (50): multi-angle research on a large target, or schema mode with many fields.
- `xhigh` (75): exhaustive coverage; use when the user explicitly wants maximum depth.

Creating a task requires the full budget in available credits, but billing is per agent
that actually runs — a focused brief at `high` often finishes well under budget. If
create fails with `insufficient_credits`, the error includes `required_credits` and
`available_credits`; offer a lower depth.

## Design output schemas narrowly

Schema mode (`output_schema`) is for machine-readable reports. Rules of thumb:

- A handful of fields, each naming one decision-relevant fact or bounded list.
- Use arrays of strings for angles, risks, initiatives; strings for summaries; numbers
  only for genuinely numeric facts.
- The schema must be a JSON Schema object (`"type": "object"`); it is validated in
  full at creation time, so a malformed nested schema fails fast.
- A `done` schema report is guaranteed to conform. Per-field `basis` (source ids) is
  the audit trail — treat fields with an empty basis as unsupported.

## Run and read

```bash
<extruct_api_cli> deep-research create --payload-file research.json
<extruct_api_cli> deep-research poll <task_id>
```

Reading the report honestly:

- Markdown reports cite sources as `[1]`-style ids resolving against `report.sources`.
  Do not strip the citations when relaying to the user.
- **Always check `report.degradation_reasons`** and show them with the report. They say,
  in plain language, when research stopped early (budget or step limit) or when some
  research agents failed. An empty list means a clean run.
- On `failed`, relay `failure_reason`. Rejected briefs include concrete suggestions —
  offer to retry with a fixed brief. Failed tasks refund all their charges.
- Progress while running: `iterations` (analysis steps), `agents` (billed research
  agents), `sources` (unique sources collected).
