#!/usr/bin/env python3
"""
Google SERP Screenshot Tool
Takes a screenshot of Google search results for a given keyword.
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright


def sanitize_filename(keyword):
    """Convert keyword to a safe filename."""
    return "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in keyword).strip()


def take_google_screenshot(keyword, output_dir="screenshots", headless=True):
    """
    Take a screenshot of Google search results for the given keyword.

    Args:
        keyword: The search keyword/phrase
        output_dir: Directory to save screenshots (default: "screenshots")
        headless: Run browser in headless mode (default: True)

    Returns:
        Path to the saved screenshot file
    """
    # Create output directory if it doesn't exist
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Generate filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_keyword = sanitize_filename(keyword)
    filename = f"google_serp_{safe_keyword}_{timestamp}.png"
    filepath = output_path / filename

    print(f"Searching Google for: {keyword}")
    print(f"Output will be saved to: {filepath}")

    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )
        page = context.new_page()

        try:
            # Navigate to Google
            print("Loading Google...")
            page.goto("https://www.google.com", wait_until="networkidle", timeout=30000)

            # Accept cookies if the dialog appears
            try:
                accept_button = page.locator('button:has-text("Accept all"), button:has-text("I agree")')
                if accept_button.is_visible(timeout=2000):
                    accept_button.first.click()
                    page.wait_for_timeout(1000)
            except:
                pass  # No cookie dialog or already accepted

            # Find search box and enter keyword
            print("Entering search query...")
            search_box = page.locator('textarea[name="q"], input[name="q"]').first
            search_box.fill(keyword)
            search_box.press("Enter")

            # Wait for results to load
            print("Waiting for search results...")
            page.wait_for_load_state("networkidle", timeout=30000)
            page.wait_for_timeout(2000)  # Additional wait for dynamic content

            # Take screenshot
            print("Taking screenshot...")
            page.screenshot(path=str(filepath), full_page=True)

            print(f"✓ Screenshot saved successfully to: {filepath}")
            return filepath

        except Exception as e:
            print(f"✗ Error: {e}", file=sys.stderr)
            raise
        finally:
            browser.close()


def main():
    parser = argparse.ArgumentParser(
        description="Take a screenshot of Google search results for a given keyword.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python google_serp_screenshot.py "python tutorials"
  python google_serp_screenshot.py "best seo tools" --output screenshots/seo
  python google_serp_screenshot.py "machine learning" --no-headless
        """
    )

    parser.add_argument(
        "keyword",
        help="The keyword or phrase to search on Google"
    )

    parser.add_argument(
        "-o", "--output",
        default="screenshots",
        help="Output directory for screenshots (default: screenshots)"
    )

    parser.add_argument(
        "--no-headless",
        action="store_true",
        help="Show the browser window (disable headless mode)"
    )

    args = parser.parse_args()

    try:
        take_google_screenshot(
            keyword=args.keyword,
            output_dir=args.output,
            headless=not args.no_headless
        )
    except KeyboardInterrupt:
        print("\n✗ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Failed to take screenshot: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
