import requests

def fetch_google_lens_page_token(api_key, image_url, language=None, country=None, no_cache=None, async_param=None):
    """
    Fetches the page token for Google Lens Image Sources API using SerpApi.

    :param api_key: Your SerpApi private key.
    :param image_url: URL of the image to perform the Google Lens search.
    :param language: Optional. Language for the search (e.g., 'en').
    :param country: Optional. Country for the search (e.g., 'us').
    :param no_cache: Optional. Whether to bypass cache (True or False).
    :param async_param: Optional. Whether to submit search asynchronously (True or False).
    :return: Page token for the image sources search.
    """
    base_url = "https://serpapi.com/search"

    params = {
        "engine": "google_lens",
        "api_key": api_key,
        "url": image_url,
        "hl": language,
        "country": country,
        "no_cache": no_cache,
        "async": async_param
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    response = requests.get(base_url, params=params)
    response.raise_for_status()

    search_results = response.json()
    return search_results.get("image_sources_search", {}).get("page_token")

def fetch_google_lens_image_sources(api_key, page_token):
    """
    Fetches image sources from Google Lens using SerpApi with a given page token.

    :param api_key: Your SerpApi private key.
    :param page_token: Token to retrieve image sources.
    :return: Parsed JSON data of the image sources.
    """
    base_url = "https://serpapi.com/search"

    params = {
        "engine": "google_lens_image_sources",
        "api_key": api_key,
        "page_token": page_token
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()

    return response.json()

# Example usage
#api_key = "cbffeb8fa1dd8ae8549f588fc59b30ced4cf50b812435964648de4aff88aa360"  # Replace with your actual API key
#image_url = "https://d.furaffinity.net/art/jianhu/1677393776/1677393776.jianhu_2631660065489__pic_hd.jpg"  # Replace with your actual image URL

# Fetch page token and image sources
#page_token = fetch_google_lens_page_token(api_key, image_url)
#image_sources_results = fetch_google_lens_image_sources(api_key, page_token)
#print(image_sources_results)
