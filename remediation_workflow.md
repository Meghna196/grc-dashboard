# GRC Risk Remediation Workflow

## Workflow Overview
This document describes the risk lifecycle from identification through closure,
aligned to COBIT 2019 APO12 (Managed Risk).

## Stages

### 1. Risk Identification
- Source: threat intelligence, audit findings, vulnerability scans, vendor assessments
- Entry point: Risk Register (ServiceNow sn_risk_risk table)
- Required fields: Risk_ID, Domain, Description, Initial Score, Owner

### 2. Risk Assessment
- Likelihood and Impact scored 1-5 by Risk Owner
- Risk Score = Likelihood x Impact
- Scores >= 15 flagged as Critical, requiring immediate escalation to CISO

### 3. Remediation Planning
- Risk Owner assigns remediation tasks in ServiceNow
- Target date set within policy thresholds:
  - Critical (15-25): 30 days
  - High (10-14): 60 days
  - Medium (5-9): 90 days
  - Low (1-4): 180 days

### 4. Tracking and Escalation
- Weekly status updates required for Critical and High risks
- Overdue risks auto-escalate via ServiceNow notification rules
- Dashboard reviewed monthly by GRC team

### 5. Risk Closure
- Evidence of control implementation attached to ServiceNow record
- Risk Owner and GRC Manager both approve closure
- Closed risks retained for audit trail, never deleted

## COBIT Alignment
- APO12.01: Collection of data about risk
- APO12.02: Analysis of risk
- APO12.06: Responding to risk

## Review Cadence
- Full register review: quarterly
- Critical risk review: monthly
- Dashboard review: weekly

## Current Register Snapshot (as of 2026-07-05)
- 12 risks tracked across all five COBIT domains (APO, BAI, DSS, MEA, EDM)
- 5 Critical risks (score >= 15), all with named owners
- 1 overdue remediation (DSS-003, server patching) — escalated per Stage 4
- Highest-exposure domain: DSS (avg score 15.8)
