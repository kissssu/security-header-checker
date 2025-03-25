# Security Header Checker

## Basic Info

This Python script, `security_header_checker.py`, is a command-line tool designed to analyze the HTTP security headers of a given website. It checks for the presence of several recommended security headers and provides a summary of the findings, including a security score and a rating.

*(Privet! This is a simple program to check website security. - Привет! Это простая программа для проверки безопасности веб-сайта.)*

## Features

* Checks for the presence of the following security headers:
    * `Strict-Transport-Security` (HSTS)
    * `Content-Security-Policy` (CSP)
    * `X-Frame-Options`
    * `X-Content-Type-Options`
    * `Referrer-Policy`
    * `Permissions-Policy`
* Provides a count of present and missing security headers.
* Displays details of the present security headers.
* Calculates a percentage-based security score.
* Offers a simple rating of the website's security header configuration.
* Prints raw HTTP headers for detailed inspection.
* Verbose output option to show each present header during the check.
* Handles basic HTTP and HTTPS URLs.
* Includes informational notes about each security header.

## Requirements

* Python 3.6 or higher.
* The `requests` library. You can install it using pip:
    ```bash
    pip install requests
    ```

## How to Use

1.  **Save the script:** Save the provided Python code as `security_header_checker.py`.
2.  **Open your terminal or command prompt.**
3.  **Navigate to the directory** where you saved the script.
4.  **Run the script** with the URL of the website you want to check as an argument.

    ```bash
    python3 security_header_checker.py <URL>
    ```

    Replace `<URL>` with the actual URL of the website (e.g., `https://example.com`).

5.  **Optional verbose output:** To see each present header and its value during the check, use the `-v` or `--verbose` flag:

    ```bash
    python3 security_header_checker.py [https://example.com](https://example.com) -v
    ```

*(Kak ispol'zovat'? Prosto vvedite 'python3 security_header_checker.py' i adres sayta. - Как использовать? Просто введите 'python3 security_header_checker.py' и адрес сайта.)*

## Example Output
```
Security Header Check for: https://example.com
Present Security Headers: 3 / 6

Present Header Details:
Strict-Transport-Security: max-age=31536000
Content-Security-Policy: default-src 'self'
X-Frame-Options: SAMEORIGIN

Missing Security Headers:
X-Content-Type-Options
Referrer-Policy
Permissions-Policy
Security Score: 50.00%

Informational Notes:
Strict-Transport-Security (HSTS) ensures browsers only connect via HTTPS.
Content-Security-Policy (CSP) controls resources a browser is allowed to load.
X-Frame-Options prevents clickjacking attacks.
X-Content-Type-Options prevents MIME sniffing.
Referrer-Policy controls how much referrer information is sent.
Permissions-Policy controls browser features available to the site.
Higher Security Score indicates better security posture.
Site's Security Header Rating:

Meh, it's alright. They're missing some key headers. Needs a bit of work.

Raw Headers:
Content-Type: text/html; charset=UTF-8
Date: Tue, 25 Mar 2025 13:03:00 GMT
Server: Example Server
Strict-Transport-Security: max-age=31536000
Content-Security-Policy: default-src 'self'
X-Frame-Options: SAMEORIGIN
Accept-Ranges: bytes
Connection: close
```

## Explanation of Output

* **Security Header Check for: `<URL>`:** The URL that was analyzed.
* **Present Security Headers: `<count>` / `<total>`:** The number of security headers found out of the total number the script checks for.
* **Present Header Details:** Lists each security header that was found in the website's response headers and its corresponding value. If no security headers from the defined list are present, it will show "None".
* **Missing Security Headers:** Lists the security headers from the defined list that were not found in the website's response headers. If all security headers are present, it will show "None".
* **Security Score: `<percentage>%`:** A calculated percentage representing the ratio of present security headers to the total number of checked headers. *(Etot ochen' vazhno! Vysshiy ball oznachayet lutchshuyu zashchitu. - Это очень важно! Высший балл означает лучшую защиту.)*
* **Informational Notes:** Provides a brief explanation of what each security header does.
* **Site's Security Header Rating:** A simple, human-readable assessment of the website's security header configuration based on the security score.
* **Raw Headers:** Displays all the HTTP headers returned by the server for the given URL. This can be useful for seeing other headers and verifying the security headers.

## Configuration (Optional)

The `SECURITY_HEADERS` dictionary in the script defines the security headers that are checked. If you want to add or remove headers from the check, you can modify this dictionary. The keys of the dictionary are the header names as they appear in the HTTP response, and the values are the human-readable names used in the output.

```python
SECURITY_HEADERS = {
    "Strict-Transport-Security": "Strict-Transport-Security",
    "Content-Security-Policy": "Content-Security-Policy",
    # Add or remove headers as needed
}
```

## Key Improvements

This script provides a basic but useful way to quickly assess a website's security header configuration. Potential improvements could include:
- **More detailed analysis of header values**: Instead of just checking for presence, the script could analyze the values of the headers (e.g., checking the max-age in HSTS or the directives in CSP).
- **Integration with online databases or best practices**: The script could be enhanced to compare the found headers against recommended configurations.
- **Reporting in different formats**: Outputting results in JSON or other formats could be useful for automation or further analysis.
- **Handling more complex scenarios**: Dealing with different types of redirects or error responses more robustly.

## Contribution

Contributions to this script are welcome! If you have suggestions for improvements or find any issues, please feel free to submit a pull request.
