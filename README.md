# Enterprise GRC Risk Tracking Dashboard

A COBIT 2019-aligned risk register with Python automation, heat map visualization, and ServiceNow GRC dashboard workflow. Built to mirror the day-to-day tooling of enterprise GRC/risk analysts.

## What's Here

| File | Purpose |
|---|---|
| `risk_register.csv` | 12 realistic risks across all five COBIT domains (APO, BAI, DSS, MEA, EDM), scored on a 5x5 likelihood/impact scale |
| `risk_summary.py` | Loads the register, recomputes risk scores, and reports status breakdown, per-domain averages, critical risks (score >= 15), and overdue remediations |
| `risk_summary_report.txt` | Generated summary report |
| `heatmap.py` | Generates the 5x5 risk heat map from the register (matplotlib) |
| `risk_heatmap.png` / `risk_heatmap.drawio` | Heat map — image and editable draw.io source |
| `remediation_workflow.md` | Risk lifecycle documentation aligned to COBIT APO12 (Managed Risk) |
| `servicenow_setup_guide.md` | Steps to import the register into a ServiceNow PDI (`sn_risk_risk` table) and build the executive dashboard |

## Usage

```bash
python3 risk_summary.py   # writes risk_summary_report.txt
python3 heatmap.py        # writes risk_heatmap.png (requires matplotlib)
```

## Risk Model

- **Score** = Likelihood (1-5) x Impact (1-5)
- **Zones**: Low (1-4), Medium (5-9), High (10-14), Critical (15-25)
- Every risk maps to a COBIT 2019 control objective (e.g., `DSS05.04`) and a named owner
- Remediation SLAs by severity: Critical 30d, High 60d, Medium 90d, Low 180d

## Current Posture Snapshot

12 risks tracked; 5 critical, all owned; 1 overdue remediation (server patching, escalated). Highest-exposure domain: DSS (avg score 15.8).
