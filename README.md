# RiskIQ
Python script to work with RiskIQ API to support in cybersecurity

-	Feature
o	Lookup IP/Domain information from pre-defined CSV 'query_list.csv’
o	Export result to XLSX file “query_result_ddmmyy-hhmmss.xlsx”
o	Can lookup follow data refer Security Intelligence Services: Reputation (riskiq.net)
	Score
	Classification
	Rules (name, description, severity, link)

-	API Key security enhancement
o	Remove embedded API key make script more secured manner.
o	Require user to enter API information for first time use.
o	Validate API information, script will not be able to process if incorrect API.
