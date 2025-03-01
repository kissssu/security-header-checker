#!/usr/bin/python3

import requests
from urllib.parse import urlparse

SECURITY_HEADERS = {
    "Content-Security-Policy": True,
    "Strict-Transport-Security": True,
    "X-Frame-Options": True,
    "X-Content-Type-Options": True,
    "Referrer-Policy": True,
    "Permissions-Policy": False,  # Optional
}

def check_security_headers(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        headers = response.headers

        present_count = 0
        missing_headers = []
        optional_present = 0
        total_required = 0

        for header, required in SECURITY_HEADERS.items():
            if required:
                total_required += 1
                if header in headers:
                    present_count += 1
                else:
                    missing_headers.append(header)
            else:
                if header in headers:
                    optional_present +=1

        total_headers = total_required

        percentage = (present_count / total_headers) * 100 if total_headers > 0 else 0

        print(f"Security Header Check for: {url}")
        print("-" * 40)

        print(f"Present Security Headers: {present_count} / {total_headers}")

        print("\nMissing Security Headers:")
        if missing_headers:
            for header in missing_headers:
                print(f"- {header}")
        else:
            print("- None")

        print(f"\nOptional Headers present: {optional_present}")

        print(f"\nSecurity Score: {percentage:.2f}%")
        print("-" * 40)

        return percentage

    except requests.exceptions.RequestException as e:
        print(f"Error checking URL: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    url = input("Enter the URL to check (including http:// or https://): ")

    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        print("Invalid URL. Please include http:// or https://")
    else:
        check_security_headers(url)
