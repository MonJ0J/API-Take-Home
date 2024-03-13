import requests
from collections import defaultdict


def fetch_company_ticker_info():
    url = "https://www.sec.gov/files/company_tickers_exchange.json"
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Host': 'www.sec.gov',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Cookie': 'ak_bmsc=171A8B8B20DC3BAE692B24C3652E41DB~000000000000000000000000000000~YAAQVsX3ve6VEC2OAQAADmtzNBdd2f1n/qbGIVPlK83PM5AX2tyYjjRyYeMT1WW05iSIaq0gDDxBmixJ4EF2haQnKe5Kp1P8Bf11h8fTXjiTgENFn4VtmwyC7LBrKfrnrYUVKlb4wdfGgBES88NwEFs42WXxtJW83jxLlgDCDnwBlSDp4AJOl01wIXoDyV/SvwwoRwEw1HUfUtdZb6vT/jQH509hLFQBe8vBi6aikqq11p9YhlZsAI2zrLrGBvUoa6I5cJ9waXkPXcDWsKp0uXQe3tm6IHXeoyiXMsf1qtnZJPTdTEE0QBA75PfdA2+Gw71/ONQ+9tRRv1mcFtFq+8r5ouU8f4WTCqm5VRHiNvd/1vnlTi+t/UFMPtgLx7w+s5DF+l2mlrdLYexzY8nK5xFzhZ+XmsfX0Agxxg=='
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return list(data.items())
        else:
            return f"Failed to retrieve data: Status code {response.status_code}"
    except Exception as e:
        return str(e)


def format_company_response(response):
    data = response[1][1]
    Nasdaq = []
    filtered = []
    # Filter for Nasdaq
    for exchange in data:
        if exchange[3] == 'Nasdaq':
            Nasdaq.append(exchange)
    # Filter for first 10
    for i in range(10):
        filtered.append(Nasdaq[i])
    return filtered


def getStateIncorporation(filtered):
    # Prepare for grouping by state
    state = defaultdict(int)

    for cik, name, ticker, exchange in filtered:
        formatted_cik = str(cik).zfill(10)
        # print(formatted_cik)
        url = f"https://data.sec.gov/submissions/CIK{formatted_cik}.json"
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Cookie': 'ak_bmsc=B0CE433FE4F23527CDBEEAFD5B0C080C~000000000000000000000000000000~YAAQEJUgF0+8vi2OAQAAcADnNRdO1ub0d+mMaNyxyIHarHWeixN5bMZfGM8SLS6xyNdl9RhtiT4swGxz9svO4ps1la9szFAGOP4SlwWiqKMDaiZdhJE8ruEknGQvLOrkhAoHUbwKDFmIqa7+LBUPsQ7GFufT2j09ke8hm4uQ3Gi2G2tXaZEPXIO0xgzO3SgFBiNouauYwlVsa+LTVNgZxXRmGvTh1C1PqYn5AVSBPJks+zAvW8V+8rghJ3XuZO8SgCcgWKfAiNUIKWu0a18uKlemYFmweH6hKwbk3DV3N0qpRW9grfdXYuCcMh3dZQTe50T3mBzVs8FYLwrYPo1mlKMvuPzeEW93b4kxlgvFaNbrCbyWI3AI66CSwPyjQK4V3J3Cyrb0NGU=; Domain=.sec.gov; Path=/; Expires=Wed, 13 Mar 2024 05:41:55 GMT; Max-Age=7200; HttpOnly'
        }
        try:
            response = requests.get(url, headers=headers, timeout=10)
            # Check if the request was successful
            if response.status_code == 200:
                res = response.json()
                state_indorporation = res["stateOfIncorporationDescription"]
                if state_indorporation == '':
                    state_indorporation = "No State Present"
                state[state_indorporation] += 1
        except Exception as e:
            print(f"An error occurred while retrieving data for {name} (CIK: {formatted_cik}): {e}")

    return state


def main():
    # Fetch ticket information
    response = fetch_company_ticker_info()
    
    if not isinstance(response, str):  # Check if the response is not an error message
        # Format and filter
        filtered_companies = format_company_response(response)
        
        # Get the states of incorporation
        states_of_incorporation = getStateIncorporation(filtered_companies)
        
        # Print the states of incorporation and their counts
        print("States of Incorporation:")
        for state, count in states_of_incorporation.items():
            print(f"{state}: {count}")
    else:
        # If there was an error fetching company info, print the error
        print(response)

if __name__ == "__main__":
    main()
