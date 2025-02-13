#!/usr/bin/python3

import requests
from urllib.parse import urlparse

REQUIRED_HEADERS = {
    "Content-Security-Policy": {"required": True, "score": 20},
    "X-Frame-Options": {"required": True, "score": 15},
    "X-Content-Type-Options": {"required": True, "score": 10},
    "Referrer-Policy": {"required": True, "score": 10},
    "Permissions-Policy": {"required": False, "score": 5},
    "Strict-Transport-Security": {"required": True, "score": 20},
    "X-XSS-Protection": {"required": False, "score": 1},  # Still included for completeness
    "Cache-Control": {"required": False, "score": 2},
    "Clear-Site-Data": {"required": False, "score": 2},
}

def check_security_headers(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        headers = response.headers

        present_headers = set(headers.keys())
        required_headers = set(REQUIRED_HEADERS.keys())

        missing_headers = required_headers - present_headers
        extra_headers = present_headers - required_headers

        score = 0
        for header, details in REQUIRED_HEADERS.items():
            if header in headers:
                score += details["score"]
            elif details["required"]:
                score -= details["score"]  # Deduct if required and missing

        # Ensure score doesn't go below 0
        score = max(0, score)  # Fixes negative score bug

        print(f"Security Header Check for: {url}")
        print("-" * 40)

        print("Present Headers:")
        for header, value in headers.items():
            # Truncate long CSP values for display
            if header == "Content-Security-Policy" and len(value) > 100:
                value = value[:100] + "..."  # Truncate CSP
            print(f"- {header}: {value}")

        print("\nMissing Headers:")
        if missing_headers:
            for header in missing_headers:
                print(f"- {header}")
        else:
            print("- None")

        print("\nExtra Headers (Consider reviewing):")
        if extra_headers:
            for header in extra_headers:
                print(f"- {header}")
        else:
            print("- None")

        score_message = get_score_message(score)  # Get message
        print(f"\nSecurity Score: {score} ({score_message})")  # Include message
        print("-" * 40)

        return score

    except requests.exceptions.RequestException as e:
        print(f"Error checking URL: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def get_score_message(score):
    if score >= 90:
        return "Outstanding"
    elif score >= 70:
        return "Excellent"
    elif score >= 50:
        return "Good"
    elif score >= 30:
        return "Fair"
    else:
        return "Weak"

if __name__ == "__main__":
    url = input("Enter the URL to check (including http:// or https://): ")

    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        print("Invalid URL. Please include http:// or https://")
    else:
        check_security_headers(url)