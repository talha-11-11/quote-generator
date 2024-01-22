import requests

def get_random_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    if response.status_code == 200:
        quote_data = response.json()
        content = quote_data.get("content")
        author = quote_data.get("author")
        source = quote_data.get("tags", {}).get("source", "Unknown")
        return f'"{content}" - {author} (Source: {source})'
    else:
        return "Failed to fetch a random quote."

if __name__ == "__main__":
    print("Random Quote Generator")
    print(get_random_quote())
