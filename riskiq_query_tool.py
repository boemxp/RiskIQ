import csv
import requests
import openpyxl
import os
from datetime import datetime

# Set the API endpoint URL
url = 'https://api.riskiq.net/pt/v2/reputation'

# Check if the environment variables for the API credentials are set
if 'RISKIQ_USERNAME' in os.environ and 'RISKIQ_KEY' in os.environ:
    # If the environment variables are set, use them for authentication
    username = os.environ['RISKIQ_USERNAME']
    key = os.environ['RISKIQ_KEY']
    auth = (username, key)
else:
    # If the environment variables are not set, prompt the user to enter them and set them as environment variables
    print("No API credentials found. Please enter your RiskIQ API credentials.")
    while True:
        username = input("Username: ")
        key = input("Key: ")
        auth = (username, key)

        # Test the API credentials
        response = requests.get(url, params={'query': 'test'}, auth=auth)
        if response.status_code == 200:
            break
        else:
            print("Invalid API credentials. Please try again.")

    os.environ['RISKIQ_USERNAME'] = username
    os.environ['RISKIQ_KEY'] = key

# Set the path to the CSV file containing the queries
csv_file = 'query_list.csv'

# Create a list to store the query results
results = []

# Open the CSV file and read the queries
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    query_list = [row[0] for row in csv_reader]

# Loop through each query in the list and make the API request
for query in query_list:
    # Set the API query parameters
    query_params = {
        'query': query
    }

    # Make the API request
    response = requests.get(url, params=query_params, auth=auth)

    # Parse the JSON response
    response_json = response.json()

    # Append the query information to the results list
    results.append({
        'query': query,
        'score': response_json.get('score'),
        'classification': response_json.get('classification'),
        'rules': response_json.get('rules')
    })

# Print the header row to console
print('|{:<20}|{:<6}|{:<15}|{:<20}|'.format('Query', 'Score', 'Classification', 'Rules'))
print('-' * 65)

# Loop through each query result and print the information to console
for result in results:
    # Convert the 'rules' and 'lastSeen' values to strings
    rules_str = str(result['rules'])

    print('|{:<20}|{:<6}|{:<15}|{:<20}|'.format(result['query'], result['score'], result['classification'], rules_str))

# Export the query results to an Excel file
filename = f"query_results_{datetime.now().strftime('%d%m%y-%H%M%S')}.xlsx"
wb = openpyxl.Workbook()
ws = wb.active

# Add the header row to the Excel sheet
ws.append(['Query', 'Score', 'Classification', 'Rules'])

# Add each query result to the Excel sheet
for result in results:
    ws.append([result['query'], result['score'], result['classification'], str(result['rules'])])

# Save the Excel file
wb.save(filename)

print(f"Results exported to {filename}")
