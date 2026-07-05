# ServiceNow Setup Checklist (Steps 4, 5 & 7)

These steps need your own free Personal Developer Instance (PDI) — they can't be done for you.

## 1. Get a PDI (~15 min)
1. Sign up at developer.servicenow.com and request a PDI (latest stable release).
2. Log in. Search `GRC` in the left nav. If the Governance, Risk and Compliance app group isn't there, activate the plugin via **System Applications > All Available Applications**.
3. If Risk Register shows a permission error, assign yourself the `sn_risk.manager` role under **User Administration > Roles**.

## 2. Import risk_register.csv
1. **System Import Sets > Load Data** → target table `sn_risk_risk` → upload `risk_register.csv` → Submit.
2. **System Import Sets > Import Set Tables** → your import set → **Create Transform Map**, mapping:

| CSV Column | ServiceNow Field |
|---|---|
| Risk_Description | Short Description |
| Domain | Category |
| Likelihood | Likelihood |
| Impact | Impact |
| Risk_Score | Risk Score |
| Risk_Owner | Assigned To |
| Status | State |
| Target_Date | Remediation Target Date |
| Notes | Description |

3. **Run Transform**, then verify rows under **GRC > Risk > Risk Register**.
4. If rows error on Assigned To: it expects user records. Either create test users first (CISO, IT Director, IR Lead, Security Engineering Lead, Infrastructure Manager, ERP Program Manager, Compliance Manager, GRC Manager) under **User Administration > Users**, or leave it unmapped and fill in after import.

## 3. Build the dashboard
**Self-Service > Dashboards > New** → name it `Enterprise Risk Posture Dashboard`. Add four report widgets on table `sn_risk_risk`:

1. **Risks by Status** — Donut, grouped by State.
2. **Critical Risks - Action Required** — List, filter `Risk Score >= 15`, columns: Risk ID, Short Description, Assigned To, State, Remediation Target Date. Put this at the top.
3. **Avg Risk Score by Domain** — Bar, grouped by Category, aggregate Average of Risk Score.
4. **Overdue Remediations** — List, filter `Remediation Target Date < Today AND State != Closed`.

Expected results with this register: donut shows 7 Open / 4 In Progress / 1 Closed; critical list shows 5 rows (APO-001, DSS-002, BAI-001, DSS-003, DSS-001); bar chart shows DSS highest at 15.8; overdue list shows DSS-003. If your widgets match these numbers, the import worked. Screenshot the dashboard for your portfolio.
