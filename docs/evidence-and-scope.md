# Evidence & Disclosure

[Portfolio](../README.md) · [한국어](evidence-and-scope.ko.md)

This guide explains what the portfolio demonstrates and what requires separate verification.

## Reporting Principles

1. Describe the question, approach, outcome, and individual role separately.
2. Distinguish training performance, cross-validation, public leaderboard scores, and final rankings.
3. Compare improvements directly only when the data, split, and metric are comparable.
4. Disclose AI-assisted development without presenting all code as unaided work.
5. Do not equate a team's output with one account's commit history.
6. Date historical candidate, contract, and market information instead of presenting it as current.

## Evidence by Case Study

| Case | Public Evidence | Private or Unverified Scope |
|---|---|---|
| SSG analysis | Code, result CSVs, report, presentation, validation and change records | Separate source data; actual adoption or recruitment by a club |
| SDA | Live website, curriculum, projects, magazine | Member records, administrator accounts, private operating repository |
| AI research tool | Code, installation guide, tests, offline demo | Personal research data; unmeasured commercial outcomes |
| Statiz, warehouse, mosquito, wind | Shareable descriptions of questions, methods, results, and lessons | Raw data, credentials, private submissions, independent verification beyond the summary |
| MLB clustering | Analysis summary and public SDA archive | Equating latent-space metrics with proven strategy effects |
| K League | Classifier-comparison learning record | Pre-match prediction claims before timing and split checks |

## Privacy & Publication

Private source data and credentials are not moved into public repositories to improve presentation. Files containing accounts, member lists, or restricted submissions require a separate publication check. Contact details are limited to the email address already used publicly.

English case studies provide an accessible entry point. Original Korean reports, operational documents, and experiment logs are preserved rather than silently rewritten.

## Maintenance

- Update completion status, reference dates, and final artifact links together.
- Record the evaluation split, metric, and evidence whenever adding a score.
- Distinguish retired functionality from features that are still in use.
- Keep English and Korean summaries aligned when changing substantive claims.
- Run `python3 scripts/check_links.py` after changing links.
