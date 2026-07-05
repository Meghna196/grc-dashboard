"""GRC Risk Register Summary Script.

Loads a COBIT-aligned risk register CSV, recomputes risk scores
(Likelihood x Impact), and writes a summary report covering status
breakdown, average score per COBIT domain, critical risks (score >= 15),
and overdue remediations.
"""

import csv
from collections import defaultdict
from datetime import date

INPUT_FILE = "risk_register.csv"
OUTPUT_FILE = "risk_summary_report.txt"
CRITICAL_THRESHOLD = 15


def load_register(filepath):
    risks = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["Risk_Score"] = int(row["Likelihood"]) * int(row["Impact"])
            risks.append(row)
    return risks


def summarize(risks, today=None):
    today = today or date.today()
    domain_scores = defaultdict(list)
    status_counts = defaultdict(int)
    critical_risks = []
    overdue_risks = []
    for r in risks:
        domain_scores[r["Domain"]].append(r["Risk_Score"])
        status_counts[r["Status"]] += 1
        if r["Risk_Score"] >= CRITICAL_THRESHOLD:
            critical_risks.append(r)
        target = date.fromisoformat(r["Target_Date"])
        if target < today and r["Status"] != "Closed":
            overdue_risks.append(r)
    return domain_scores, status_counts, critical_risks, overdue_risks


def write_report(domain_scores, status_counts, critical_risks, overdue_risks,
                 output_path, total):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("=== GRC RISK REGISTER SUMMARY ===\n")
        f.write(f"Generated: {date.today().isoformat()} | Total risks: {total}\n\n")

        f.write("-- Risk Status Breakdown --\n")
        for status, count in sorted(status_counts.items()):
            f.write(f"  {status}: {count}\n")

        f.write("\n-- Average Risk Score by COBIT Domain --\n")
        for domain, scores in sorted(domain_scores.items()):
            avg = sum(scores) / len(scores)
            f.write(f"  {domain}: {avg:.1f} avg score ({len(scores)} risks)\n")

        f.write(f"\n-- Critical Risks (Score >= {CRITICAL_THRESHOLD}) --\n")
        for r in sorted(critical_risks, key=lambda x: -x["Risk_Score"]):
            f.write(f"  [{r['Risk_ID']}] {r['Risk_Description']}\n")
            f.write(f"    Score: {r['Risk_Score']} | Owner: {r['Risk_Owner']}"
                    f" | Status: {r['Status']} | Target: {r['Target_Date']}\n")

        f.write("\n-- Overdue Remediations (past target, not Closed) --\n")
        if not overdue_risks:
            f.write("  None\n")
        for r in overdue_risks:
            f.write(f"  [{r['Risk_ID']}] {r['Risk_Description']}"
                    f" (target {r['Target_Date']}, {r['Status']})\n")


if __name__ == "__main__":
    risks = load_register(INPUT_FILE)
    domain_scores, status_counts, critical_risks, overdue_risks = summarize(risks)
    write_report(domain_scores, status_counts, critical_risks, overdue_risks,
                 OUTPUT_FILE, len(risks))
    print(f"Report written to {OUTPUT_FILE}")
    print(f"Total risks loaded: {len(risks)}")
    print(f"Critical risks identified: {len(critical_risks)}")
    print(f"Overdue remediations: {len(overdue_risks)}")
