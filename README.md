# Security Header Checker

This Python script checks the security headers of a given website and provides a score based on the presence and proper configuration of crucial security headers. It identifies missing, present, and extra headers, offering insights into the website's security posture.

## Features

* Checks for the presence and, to a limited extent, the values of essential security headers, including:
    * `Content-Security-Policy` (CSP)
    * `X-Frame-Options`
    * `X-Content-Type-Options`
    * `Referrer-Policy`
    * `Permissions-Policy`
    * `Strict-Transport-Security` (HSTS)
    * `X-XSS-Protection`
    * `Cache-Control`
    * `Clear-Site-Data`
* Provides a security score with a textual interpretation (e.g., "Good," "Excellent") based on the header configuration.
* Identifies missing and extra headers.
* Handles network errors and other exceptions gracefully.
* Clear and informative, color-coded output for improved readability.
* Basic command-line argument support for specifying the URL.

## Requirements

* Python 3.x
* `requests` library (Install with: `pip install requests`)

## How to Use

1. Clone the repository (or download the script):

   ```bash
   git clone https://github.com/kissssu/security-header-checker.git    
   cd security-header-checker
   ```

2. Run the script:

```Bash
python security_header_checker.py
Enter the URL to check (including http:// or https://): https://www.example.com
```

## Example Output
```
Security Header Check for: https://www.example.com
----------------------------------------
Present Headers:
- Content-Security-Policy: default-src 'self'; script-src 'self' [https://trusted-cdn.com]; ... (truncated)
- X-Frame-Options: SAMEORIGIN
- X-Content-Type-Options: nosniff
- Referrer-Policy: strict-origin-when-cross-origin
- Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
- Server: nginx/1.20.1
- Date: Tue, 24 Oct 2023 12:34:56 GMT
... (other headers)

Missing Headers:
- Permissions-Policy
- X-XSS-Protection
- Cache-Control
- Clear-Site-Data

Extra Headers (Consider reviewing):
- Server
- Date
... (other extra headers)

Security Score: 70 (Good - Most essential headers are present, but there's room for improvement.)
----------------------------------------
```

## Explanation of Output
- **Present Headers**: Lists all the headers found in the response. Long CSP values are truncated for display.
- **Missing Headers**: Lists the required security headers that were not present.
- **Extra Headers**: Lists headers that were present but not in the list of required headers. These might be informational or server-specific headers. Review them to ensure they don't pose a security risk.
- **Security Score**: A numerical score indicating the overall security posture based on the headers, along with a textual interpretation (e.g., "Weak," "Fair," "Good," "Excellent," "Outstanding"). Higher scores are better. Note that the score is just a guide; manual review of the headers is still essential.

## Configuration (Optional)

You can modify the REQUIRED_HEADERS dictionary in the script to customize the headers checked and their associated scores. This allows you to tailor the script to your specific requirements.  For example:

```Python
REQUIRED_HEADERS = {
    "Content-Security-Policy": {"required": True, "score": 20},
    "X-Frame-Options": {"required": True, "score": 15},
    # ...
}
```

## Key Improvements
- **Improved Scoring**: The scoring system has been revised to provide more accurate and meaningful scores. Negative scores are now prevented.
- **Score Messages**: Textual interpretations are now included with the score (e.g., "Good," "Excellent").
- **CSP Truncation**: Long CSP header values are truncated for cleaner output.
- **Basic CLI Support**: The script now accepts the URL as a command-line argument.

## Upcoming Improvements

In the next update, the following enhancements are planned:

* **Detailed Request Information:** An information bar will be added to provide a more in-depth view of the request and response. This will include:
    * The full request URL.
    * HTTP method used (GET, POST, etc.).
    * Response status code.
    * Time taken for the request.
* **Header Details:** For each present header, the information bar will display:
    * The header name and value.
    * A brief description of the header's purpose and its security implications.
    * Recommendations for improvement, if applicable (e.g., suggesting stronger CSP directives, HSTS preload).
* **Improved Recommendations:**  The tool will offer more specific and actionable recommendations for improving the security headers based on best practices and industry standards.  This will go beyond simply listing missing headers and will include suggestions for header values and configurations.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.
