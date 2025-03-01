# Security Header Checker

This Python script checks the security headers of a given website and provides a percentage-based score based on the presence of crucial security headers. It identifies missing and present headers, offering insights into the website's security posture.

## Features

* Checks for the presence of essential security headers, including:
    * `Content-Security-Policy` (CSP)
    * `Strict-Transport-Security` (HSTS)
    * `X-Frame-Options`
    * `X-Content-Type-Options`
    * `Referrer-Policy`
    * `Permissions-Policy` (optional)
* Provides a security score as a percentage based on the presence of required headers.
* Identifies missing security headers.
* Identifies the amount of optional headers present.
* Handles network errors and other exceptions gracefully.
* Clear and informative output for improved readability.
* Basic command-line argument support for specifying the URL.

## Requirements

* Python 3.x
* `requests` library (Install with: `pip install requests`)

## How to Use

1.  Clone the repository (or download the script):

    ```bash
    git clone [https://github.com/kissssu/security-header-checker.git](https://github.com/kissssu/security-header-checker.git)
    cd security-header-checker
    ```

2.  Run the script:

    ```bash
    python security_header_checker.py
    ```

## Example Output
```
Enter the URL to check (including http:// or https://): https://www.google.com/
Security Header Check for: https://www.google.com/
----------------------------------------
Present Security Headers: 1 / 5

Missing Security Headers:
- Content-Security-Policy
- Strict-Transport-Security
- X-Content-Type-Options
- Referrer-Policy

Optional Headers present: 0

Security Score: 20.00%
----------------------------------------
```

## Explanation of Output

* **Present Security Headers**: Displays the count of present *required* security headers out of the total required headers.
* **Missing Security Headers**: Lists the *required* security headers that were not present.
* **Optional Headers present**: Displays the count of optional headers that were present.
* **Security Score**: A percentage indicating the overall security posture based on the presence of required headers.

## Configuration (Optional)

You can modify the `SECURITY_HEADERS` dictionary in the script to customize the headers checked and whether they are considered required or optional. This allows you to tailor the script to your specific requirements. For example:

```python
SECURITY_HEADERS = {
    "Content-Security-Policy": True, #Required
    "Strict-Transport-Security": True, #Required
    "Permissions-Policy": False, #Optional
    # ...
}
```

## Key Improvements
- **Simplified Header List**: The SECURITY_HEADERS dictionary is now used to define required and optional headers.
- **Accurate Percentage Calculation**: The score is now a percentage based on the presence of required headers.
- **Clearer Output**: The output clearly shows the number of present, missing, and optional headers.
- **Focused Functionality**: The script now strictly focuses on checking the presence of headers from the given list.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.
