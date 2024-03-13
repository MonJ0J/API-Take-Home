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
bash
pip install requests
```
