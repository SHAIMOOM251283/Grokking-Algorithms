cache = {}

def get_page(url):
    if url in cache:
        return cache[url]  # Returns cached data
    else:
        data = get_data_from_server(url)
        cache[url] = data  # Saves this data in your cache first
        return data

def retrieve_page(url):
    if url in cache:
        return cache[url]
    else:
        return "URL not found in cache."

def get_data_from_server(url):
    # Simulated function to get data from the server
    return f"Data from server for URL: {url}"

def view_cache():
    print("\nCached URLs and data:")
    for url, data in cache.items():
        print(f"URL: {url} - Data: {data}")

def quit_program():
    print("Exiting the program.")
    exit()

def main():
    while True:
        print("\nEnter a command:")
        print("1. Get data for a URL")
        print("2. Retrieve data for a URL from cache")
        print("3. View cached items")
        print("4. Quit")
        
        choice = input("> ").strip()

        if choice == '1':
            url = input("Enter URL: ").strip()
            print(get_page(url))
        elif choice == '2':
            url = input("Enter URL: ").strip()
            print(retrieve_page(url))
        elif choice == '3':
            view_cache()
        elif choice == '4':
            quit_program()
        else:
            print("Invalid choice. Please enter a valid command.")

if __name__ == "__main__":
    main()
