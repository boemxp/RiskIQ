# RiskIQ API Query Tool

## Description

This program allows you to lookup IP/Domain information from a pre-defined CSV file using the RiskIQ API. The results can be exported to an XLSX file. The program can retrieve the following data from the RiskIQ Security Intelligence Services: Reputation:

- Score
- Classification
- Rules (name, description, severity, link)

API credentials are required to use this program. The credentials can be entered when prompted during the program's first use. The credentials are validated before the program can be run.

## Usage

- For Windows users:
1. Download file in 'dist'
2. Place in your computer.
3. Run "RiskIQ.exe" make sure you place 'query_list.csv' in same as program directory.

or

- For non-Windows users (Self compile):
1. Clone or download this repository to your local machine.
2. Create a CSV file called `query_list.csv` in the root directory of the program. The CSV file should contain a list of queries to be executed.
3. Run the program using Python 3. The program can be run using the following command:

    ```
    python3 riskiq_query_tool.py
    ```

4. Follow the prompts to enter your RiskIQ API credentials if you haven't already done so.

## Output

The program outputs the query results to the console and exports them to an XLSX file called `query_result_ddmmyy-hhmmss.xlsx`, where `ddmmyy-hhmmss` is the date and time that the file was created.

## License

This program is licensed under the MIT License. See the `LICENSE` file for more information.
