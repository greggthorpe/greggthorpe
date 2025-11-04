# Google SERP Screenshot Tool

A simple Python script that takes screenshots of Google Search Engine Results Pages (SERPs) for any keyword or phrase.

## Features

- Search Google for any keyword
- Capture full-page screenshots of search results
- Automatic filename generation with timestamps
- Headless browser support
- Customizable output directory
- Cross-platform compatibility

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Install Playwright browsers:

```bash
playwright install chromium
```

That's it! You're ready to use the tool.

## Usage

### Basic Usage

Simply provide a keyword or phrase:

```bash
python google_serp_screenshot.py "your keyword here"
```

Example:

```bash
python google_serp_screenshot.py "best SEO tools 2024"
```

This will:
1. Search Google for the keyword
2. Take a screenshot of the results
3. Save it to the `screenshots/` directory with a timestamp

### Advanced Options

**Custom Output Directory:**

```bash
python google_serp_screenshot.py "python tutorials" --output my_screenshots
```

**Show Browser Window (non-headless mode):**

```bash
python google_serp_screenshot.py "machine learning" --no-headless
```

**View All Options:**

```bash
python google_serp_screenshot.py --help
```

## Output

Screenshots are saved as PNG files with the following naming format:

```
google_serp_{keyword}_{timestamp}.png
```

Example:
```
screenshots/google_serp_best_SEO_tools_20241104_143022.png
```

## Examples

```bash
# Simple search
python google_serp_screenshot.py "digital marketing tips"

# Save to specific folder
python google_serp_screenshot.py "link building strategies" -o seo_research

# Watch the browser in action
python google_serp_screenshot.py "content marketing" --no-headless
```

## Troubleshooting

**Issue: "playwright not found"**
- Solution: Make sure you've installed the dependencies: `pip install -r requirements.txt`

**Issue: "Browser executable not found"**
- Solution: Install the Playwright browsers: `playwright install chromium`

**Issue: Script hangs or times out**
- Solution: Check your internet connection or try running with `--no-headless` to see what's happening

## Notes

- The script uses a realistic user agent to avoid bot detection
- Screenshots are full-page captures, including content below the fold
- The tool respects Google's robots.txt and terms of service
- Use responsibly and avoid making excessive requests

## License

Free to use for personal and commercial projects.

## Author

Created for SEO and marketing research purposes.
