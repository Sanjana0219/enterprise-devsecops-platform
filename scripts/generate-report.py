from openpyxl import Workbook
from openpyxl.styles import Font

# Create workbook
wb = Workbook()

# Remove default sheet
default_sheet = wb.active
wb.remove(default_sheet)

# -----------------------------
# TRIVY SHEET
# -----------------------------
trivy_sheet = wb.create_sheet("Trivy Scan")

headers = ["Severity", "Package", "Vulnerability", "Status"]

for col, header in enumerate(headers, 1):
    cell = trivy_sheet.cell(row=1, column=col)
    cell.value = header
    cell.font = Font(bold=True)

sample_data = [
    ["CRITICAL", "protobufjs", "CVE-2025-41422", "FAIL"],
    ["HIGH", "mongoose", "CVE-2025-42334", "FAIL"],
    ["MEDIUM", "qs", "CVE-2025-15284", "WARN"]
]

for row in sample_data:
    trivy_sheet.append(row)

# -----------------------------
# CHECKOV SHEET
# -----------------------------
checkov_sheet = wb.create_sheet("Checkov Scan")

headers = ["Policy", "File", "Status"]

for col, header in enumerate(headers, 1):
    cell = checkov_sheet.cell(row=1, column=col)
    cell.value = header
    cell.font = Font(bold=True)

checkov_data = [
    ["CKV_K8S_21", "configmap.yml", "FAIL"],
    ["CKV_K8S_8", "mongodb-deployment.yaml", "FAIL"],
    ["CKV_K8S_15", "mongodb-deployment.yaml", "FAIL"]
]

for row in checkov_data:
    checkov_sheet.append(row)

# -----------------------------
# SUMMARY SHEET
# -----------------------------
summary_sheet = wb.create_sheet("Summary")

summary_sheet["A1"] = "Enterprise DevSecOps Security Report"
summary_sheet["A1"].font = Font(bold=True)

summary_sheet["A3"] = "Tool"
summary_sheet["B3"] = "Status"

summary_sheet["A4"] = "GitLeaks"
summary_sheet["B4"] = "Completed"

summary_sheet["A5"] = "SonarCloud"
summary_sheet["B5"] = "Completed"

summary_sheet["A6"] = "Snyk"
summary_sheet["B6"] = "Completed"

summary_sheet["A7"] = "Trivy"
summary_sheet["B7"] = "Critical Vulnerabilities Found"

summary_sheet["A8"] = "Checkov"
summary_sheet["B8"] = "Policy Violations Found"

summary_sheet["A9"] = "OPA Policy Gate"
summary_sheet["B9"] = "Deployment Blocked"

# Save workbook
wb.save("security-report.xlsx")

print("Excel security report generated successfully.")