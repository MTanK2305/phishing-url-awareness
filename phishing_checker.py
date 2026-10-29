import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    """Check visible URL text for selected warning signs."""
    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["This text is not a valid URL format."]

    if not host:
        return ["Could not identify a hostname."]

    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")

    if len(host.split(".")) >= 5:
        findings.append("Hostname has 5 or more segments.")

    if "xn--" in host:
        findings.append("Hostname contains a punycode-style label.")

    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")

    if not findings:
        return ["No listed warning signs found."]

    return findings



def main():
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - this program does not open URLs.")

    raw_url = input("\nEnter a sample URL: ")

    print("\nResult:")
    findings = inspect_url(raw_url)

    for finding in findings:
        print("- " + finding)

    if findings and not findings[0].startswith(
        (
            "No URL entered.",
            "Could not identify a hostname.",
            "This text is not a valid URL format.",
            "No listed warning signs found."
        )
    ):
        print(f"\nREVIEW CAREFULLY: {len(findings)} warning sign(s) found.")


if __name__ == "__main__":
    main()






