# API-Take-Home

This script fetches company ticker information from the SEC (Securities and Exchange Commission) and groups companies based on their state of incorporation. 

## Features

- Fetches company ticker information from the SEC's public JSON file.
- Filters out the first 10 companies listed on the Nasdaq exchange.
- Retrieves additional data about these companies from the SEC's EDGAR database using their CIK numbers.
- Groups these companies by their state of incorporation.
- Outputs the count of companies incorporated in each state.

## Requirements

- Python 3
- `requests` library

## Setup

Ensure Python 3 and pip are installed on your machine. Install the `requests` library using pip:

```
pip install requests
```

## Usage

Ensure Python 3 and pip are installed on your machine. Install the `requests` library using pip:

```
python3 API.py
```
## Function Descriptions

- fetch_company_ticker_info(): Fetches the initial set of company ticker information from the SEC's JSON file.

- format_company_response(response): Takes the response from fetch_company_ticker_info and formats it, extracting only the necessary details for Nasdaq-listed companies.

- getStateIncorporation(filtered): Takes the list of filtered Nasdaq companies and fetches additional information from the SEC's EDGAR database for each one. It then groups these companies by their state of incorporation in a defaultdict.

- main(): Calls functions to acheive the goal

## Sources:

- requests library [https://pypi.org/project/requests/]
- Padd with 0's [https://www.w3schools.com/python/ref_string_zfill.asp]
