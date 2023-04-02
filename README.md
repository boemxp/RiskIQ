# RiskIQ 1.0
Python script to work with RiskIQ API to support in cybersecurity

## Feature
- Lookup IP/Domain information from pre-defined CSV 'query_list.csv’
- Export result to XLSX file “query_result_ddmmyy-hhmmss.xlsx”
- Current API can lookup follow data refer Security Intelligence Services: Reputation (riskiq.net)
    - Score
    - Classification
    - Rules (name, description, severity, link)

-	API Key security enhancement
    - Remove embedded API key make script more secured manner.
    - Require user to enter API information for first time use.
    - Validate API information, script will not be able to process if incorrect API.
