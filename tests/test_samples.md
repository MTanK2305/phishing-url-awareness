# Phishing URL Awareness Checker – Test Results

## Project Overview

The Phishing URL Awareness Checker is a Python-based project that identifies selected warning signs in URL text. It checks for suspicious URL characteristics without opening or accessing the website.

## Testing Objectives

The objective of testing is to verify that the program identifies the warning signs defined in the project requirements and handles normal URLs and empty input correctly.

## Test Cases and Results

### Test Case 1: Empty Input
**Input:** No URL entered.

**Expected Result:** The program displays a message indicating that no URL was entered.

**Status:** Passed

### Test Case 2: HTTPS URL Without Listed Warning Signs
**Input:** `https://example.com`

**Expected Result:** The program reports that no listed warning signs were found and clarifies that this does not prove the URL is safe.

**Status:** Passed

### Test Case 3: URL Containing an At Symbol
**Input:** `http://example.com@fake.com`

**Expected Result:** The program identifies the `@` symbol and reports the use of HTTP.

**Status:** Passed

### Test Case 4: URL Using an IP Address
**Input:** `http://192.0.2.10/account`

**Expected Result:** The program identifies the IP address in the hostname and reports the use of HTTP.

**Status:** Passed

### Test Case 5: URL With Multiple Hostname Segments
**Input:** `http://login.account.verify.shop.example.com`

**Expected Result:** The program identifies the hostname as having five or more segments and reports the use of HTTP.

**Status:** Passed

### Test Case 6: Punycode-Style Hostname
**Input:** `http://xn--example-ova.com`

**Expected Result:** The program identifies the `xn--` pattern and reports the use of HTTP.

**Status:** Passed

### Test Case 7: Unusually Long URL
**Input:** A sample URL longer than 100 characters.

**Expected Result:** The program displays a warning about the URL length and reports the use of HTTP.

**Status:** Passed

## Conclusion

Testing confirmed that the checker identifies the selected URL warning signs and handles empty input. The project demonstrates basic Python programming, string processing, URL parsing, regular expressions, conditional statements, and functional testing.

The checker is intended for educational awareness purposes. Its results do not establish whether a website is malicious or safe.