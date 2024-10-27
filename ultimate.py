import requests
from concurrent.futures import ThreadPoolExecutor

# ProxyScrape API URLs for HTTP and HTTPS proxies
PROXYSCRAPE_HTTP_URL = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=1000&country=all&ssl=all&anonymity=all'
PROXYSCRAPE_HTTPS_URL = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=1000&country=all&ssl=all&anonymity=all'

# Function to get proxies from ProxyScrape (both HTTP and HTTPS)
def get_proxies_from_proxyscrape():
    http_proxies = []
    https_proxies = []
    
    try:
        print("Fetching HTTP proxies from ProxyScrape...")
        response_http = requests.get(PROXYSCRAPE_HTTP_URL)
        http_proxies = response_http.text.splitlines()

        print("Fetching HTTPS proxies from ProxyScrape...")
        response_https = requests.get(PROXYSCRAPE_HTTPS_URL)
        https_proxies = response_https.text.splitlines()

    except Exception as e:
        print(f"Error fetching proxies: {e}")

    # Combine both HTTP and HTTPS proxies
    all_proxies = http_proxies + https_proxies
    return all_proxies

# Function to check if a proxy is valid
def check_proxy(proxy):
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }
    try:
        # Test the proxy with a GET request to httpbin
        response = requests.get('https://httpbin.org/ip', proxies=proxies, timeout=5)
        if response.status_code == 200:
            print(f"Valid proxy: {proxy}")
            return proxy
    except requests.RequestException:
        pass
    return None

# Main function to fetch, check, and save valid proxies
def get_valid_proxies():
    # Get proxies from ProxyScrape
    proxies = get_proxies_from_proxyscrape()
    
    print(f"Total proxies fetched: {len(proxies)}")

    # Use multithreading to speed up proxy validation
    valid_proxies = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = list(executor.map(check_proxy, proxies))

    # Filter valid proxies (non-None results)
    valid_proxies = [proxy for proxy in results if proxy]

    # Save valid proxies to a file
    with open('proxies.txt', 'w') as f:
        for proxy in valid_proxies:
            f.write(f"{proxy}\n")

    print(f"Total valid proxies: {len(valid_proxies)}")

if __name__ == "__main__":
    get_valid_proxies()
