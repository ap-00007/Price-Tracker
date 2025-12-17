# Amazon Price Tracker

A Python script that monitors Amazon product prices and sends email alerts when the price drops below a specified threshold.

## Features

- Scrapes Amazon product pages for current prices
- Sends email notifications when prices drop
- Uses environment variables for secure credential management

## Requirements

- Python 3.11+
- `requests` - HTTP library for web requests
- `beautifulsoup4` - HTML parsing library
- `python-dotenv` - Environment variable management

## Installation

```bash
pip install requests beautifulsoup4 python-dotenv
```

## Setup

1. Create a `.env` file in the project root with the following variables:

```
SMTP_ADDRESS=your_smtp_server
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

2. Update the `BUY_PRICE` variable in `main.py` to your desired price threshold.

3. Update the Amazon product URL to track your desired item.

## Usage

```bash
python main.py
```

The script will check the current price and send you an email alert if it's below your `BUY_PRICE` threshold.

## Notes

- This script uses web scraping - Amazon's page structure may change and break the parser
- Always respect website terms of service when scraping
- Use app-specific passwords for email security (especially with Gmail)
