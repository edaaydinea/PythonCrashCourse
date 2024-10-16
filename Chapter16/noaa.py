import requests
from bs4 import BeautifulSoup

# NOAA Climate Data Online URL
base_url = "https://www.ncdc.noaa.gov/cdo-web/"

def search_weather_data(zip_code, start_date, end_date):
    # Step 1: Define search parameters
    search_url = f"{base_url}search"
    params = {
        'datasetid': 'GHCND',  # Daily Summaries dataset
        'locationid': f'ZIP:{zip_code}',
        'startdate': start_date,
        'enddate': end_date,
        'datatypeid': 'TMAX',  # Example of max temperature
        'units': 'standard',
        'limit': 1000  # Maximum number of results to fetch per request
    }
    
    # Step 2: Send request
    response = requests.get(search_url, params=params)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.prettify())  # To inspect and adjust scraping if needed
        # You may need to manually inspect how the data is structured and parse the output
    else:
        print("Failed to retrieve data. Please check your parameters.")

# Set parameters for download
zip_code = "80302"  # Example: Boulder, CO
start_date = "2022-01-01"
end_date = "2022-12-31"

search_weather_data(zip_code, start_date, end_date)
