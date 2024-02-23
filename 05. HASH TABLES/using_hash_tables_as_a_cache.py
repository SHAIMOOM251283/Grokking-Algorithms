cache = {}

def get_page(url):
    if url in cache:
        return cache[url]  # Returns cached data
    else:
        data = get_data_from_server(url)
        cache[url] = data  # Saves this data in your cache first
        return data

# Example usage
def get_data_from_server(url):
    # Simulated function to get data from the server
    return f"Data from server for URL: {url}"

# Using the get_page function
url1 = "https://example.com/page1"
url2 = "https://example.com/page2"

# First call to get_page, fetching data from server
print(get_page(url1))

# Second call to get_page, retrieving data from cache
print(get_page(url1))

# Another call with a different URL
print(get_page(url2))

