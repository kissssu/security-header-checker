#!/usr/bin/python3

import requests
import argparse

SECURITY_HEADERS = {
    "Strict-Transport-Security": "Strict-Transport-Security",
    "Content-Security-Policy": "Content-Security-Policy",
    "X-Frame-Options": "X-Frame-Options",
    "X-Content-Type-Options": "X-Content-Type-Options",
    "Referrer-Policy": "Referrer-Policy",
    "Permissions-Policy": "Permissions-Policy",
}

def check_security_headers(url, verbose=False):
    try:
        response = requests.get(url, timeout=10, allow_redirects=True)
        response.raise_for_status()
        headers = response.headers

        present_count = 0
        missing_headers = []
        present_headers_details = {}

        for header_key, header_name in SECURITY_HEADERS.items():
            if header_key in headers:
                present_count += 1
                present_headers_details[header_name] = headers[header_key]
                if verbose:
                    print(f"- {header_name}: {headers[header_key]}")
            else:
                missing_headers.append(header_name)

        total_headers = len(SECURITY_HEADERS)
        percentage = (present_count / total_headers) * 100 if total_headers > 0 else 0

        print(f"Security Header Check for: {url}")
        print("-" * 40)

        print(f"Present Security Headers: {present_count} / {total_headers}")
        if present_headers_details:
            print("\nPresent Header Details:")
            for header, value in present_headers_details.items():
                print(f"- {header}: {value}")
        else:
            print ("\nPresent Header Details:\n- None")

        print("\nMissing Security Headers:")
        if missing_headers:
            for header in missing_headers:
                print(f"- {header}")
        else:
            print("- None")

        print(f"\nSecurity Score: {percentage:.2f}%")
        print("-" * 40)

        #Additional Information

        print("\nInformational Notes:")
        print("- Strict-Transport-Security (HSTS) ensures browsers only connect via HTTPS.")
        print("- Content-Security-Policy (CSP) controls resources a browser is allowed to load.")
        print("- X-Frame-Options prevents clickjacking attacks.")
        print("- X-Content-Type-Options prevents MIME sniffing.")
        print("- Referrer-Policy controls how much referrer information is sent.")
        print("- Permissions-Policy controls browser features available to the site.")
        print("- Higher Security Score indicates better security posture.")
        print("-" * 40)

        # Rating Section
        print("\nSite's Security Header Rating:")
        if percentage >= 90:
            print("- Damn, this site's security headers are looking pretty tight! They're doing a solid job.")
        elif 70 <= percentage < 90:
            print("- Not too shabby. They've got a decent setup, but could still add a few more security layers.")
        elif 50 <= percentage < 70:
            print("- Meh, it's alright. They're missing some key headers. Needs a bit of work.")
        else:
            print("- Yikes! This site's security headers are kinda weak. They seriously need to step up their game.")
        print("-" * 40)

        # Raw Headers Section
        print("\nRaw Headers:")
        for header, value in headers.items():
            print(f"- {header}: {value}")
        print("-" * 40)

        return percentage

    except requests.exceptions.RequestException as e:
        print(f"Error checking URL: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check security headers of a URL.")
    parser.add_argument("url", help="The URL to check.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output.")
    args = parser.parse_args()

    url = args.url

    if not url.startswith(('http://', 'https://')):
        url = f"https://{url}"

    check_security_headers(url, args.verbose)

# Example Usage
# python3 your_script_name.py https://example.com -v
