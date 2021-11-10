# Scraping Websites

Get the average time of submissions in all language for a DMOJ problem

## Setup

Clone this repository.

Get Python here: https://www.python.org/downloads/

Get Poetry here: https://python-poetry.org/docs/#installation

Install dependencies using: `poetry install`

Get the Firefox Selenium webdriver here: https://github.com/mozilla/geckodriver/releases

Move the Selenium webdriver into the same folder.

## Run

Run the script using: `poetry run python script.py`

You can also pass a different problem: `poetry run python script.py https://dmoj.ca/problem/aac2p5`

## Notes

For a different browser, you can change the code from `webdriver.Firefox()` to
user some other class, including `Chrome`, `Edge`, `Safari`, and more.

Get other webdrivers: https://selenium-python.readthedocs.io/installation.html#drivers
