# Phishing URL Awareness Checker

## Project Overview

The Phishing URL Awareness Checker is a Python-based cybersecurity awareness project that examines URL text for selected warning signs commonly associated with suspicious links.

The program uses Python's built-in libraries to parse URLs, identify specific patterns, and display warning messages. It does not open URLs or connect to external websites.

## Project Objectives

- Identify selected warning signs in URL text.
- Apply Python string processing, conditional statements, and regular expressions.
- Use URL parsing to examine hostnames and schemes.
- Test the program with different URL samples and document the results.
- Promote awareness of suspicious links and safer browsing practices.

## Features

- Detects URLs containing an `@` symbol.
- Flags URLs longer than 100 characters.
- Identifies IPv4-style IP addresses used as hostnames.
- Flags hostnames containing five or more segments.
- Identifies hostnames containing the `xn--` punycode prefix.
- Flags URLs that use HTTP.
- Handles empty input and URLs without an explicitly provided scheme.
- Displays warning messages in the terminal.
- Uses Python's built-in libraries without requiring additional packages.

## Technologies Used

- **Programming Language:** Python
- **Libraries:** `re`, `urllib.parse`
- **Development Environment:** Visual Studio Code
- **Testing:** Manual testing with sample URLs

## Limitations

This project checks selected characteristics of URL text. It does not access websites, verify domain reputation, detect every phishing technique, or guarantee that a URL is safe. HTTPS alone does not establish trustworthiness.

## Prerequisites

- Python 3 installed on your system.
- Visual Studio Code or another code editor.
- A terminal or command prompt.

## Project Setup

1. Clone or download this repository.
2. Open the project folder in Visual Studio Code.
3. Open the terminal in the project directory.
4. Run the program using the command below.

## How to Run

python phishing_checker.py

When prompted, enter a sample URL to inspect. The program displays any warning signs identified by its checks.

### Example

**Input:**

http://192.0.2.10/account

**Expected output:**

Result:
- Uses an IP address instead of a familiar domain.
- Uses HTTP. HTTPS alone does not prove trust.

The exact output depends on the URL entered.

## Testing

Sample URL tests are documented in `tests/test_samples.md`. The test cases cover empty input, HTTP and HTTPS URLs, IP-address hostnames, the `@` symbol, long URLs, multiple hostname segments, and punycode-style hostnames.

## Future Improvements

1. **Enhanced URL Validation:** Improve URL validation to handle malformed URLs and different input formats more reliably.
2. **Expanded Warning Checks:** Add more URL analysis checks to identify additional suspicious patterns while clearly explaining the limitations of each check.