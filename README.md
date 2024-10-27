# ProxyScrape Proxy Fetcher and Validator

This Python script fetches HTTP and HTTPS proxies from the ProxyScrape API, validates their functionality, and saves the working proxies to a text file. It uses multithreading to quickly validate a large number of proxies by checking their responsiveness.

## Features

- **ProxyScrape API Integration**: Fetches both HTTP and HTTPS proxies from ProxyScrape.
- **Proxy Validation**: Validates the proxies by sending a test request to httpbin.org.
- **Multithreading**: Uses `ThreadPoolExecutor` to validate proxies in parallel, speeding up the process.
- **Save Valid Proxies**: The working proxies are saved to a `proxies.txt` file for later use.

## Requirements

- Python 3.x
- Required Libraries:
  - `requests`
  - `concurrent.futures` (part of the Python standard library)

## How to Use

1. **Install Dependencies**:
   - Install the required Python package by running:
     ```bash
     pip install requests
     ```

2. **Run the Script**:
   - Execute the script using Python:
     ```bash
     python main.py
     ```

3. **Results**:
   - The script will:
     1. Fetch HTTP and HTTPS proxies from ProxyScrape.
     2. Validate each proxy by sending a test request.
     3. Save valid proxies to a file named `proxies.txt`.

## Proxy Validation

The script checks whether a proxy is valid by sending a GET request to `https://httpbin.org/ip`. If the request is successful and the proxy responds with status code `200`, it is considered valid.

## Customization

- **Timeout**: The timeout for each proxy validation is set to 5 seconds. You can change this value in the `check_proxy()` function if you want to give proxies more or less time to respond.
- **Multithreading**: The script uses 100 threads by default for validating proxies. You can adjust this number in the `ThreadPoolExecutor(max_workers=100)` line depending on your system's performance.

## Output

- **proxies.txt**: This file will contain the list of valid proxies, one per line, after the script finishes.

## Notes

- The script fetches both HTTP and HTTPS proxies. Both types are validated and saved to the `proxies.txt` file.
- You can modify the ProxyScrape API URLs or adjust the multithreading for different performance needs.
