"""Output the average time for all languages on a DMOJ problem"""

import sys
import time
import collections
import statistics

from selenium import webdriver
from selenium.webdriver.common.by import By
import bs4

# The user can specify another problem if they want
if len(sys.argv) == 1:
    url = "https://dmoj.ca/problem/aac1p3"
elif len(sys.argv) == 2 and sys.argv[1] not in "-h --help /?".split():
    url = sys.argv[1]
else:
    sys.exit("Usage: python script.py [DMOJ problem url]")

language_times = collections.defaultdict(list)

driver = webdriver.Firefox()
driver.get(f"{url}/rank/?status=AC")

while True:
    soup = bs4.BeautifulSoup(driver.page_source, "html.parser")

    for row in soup.select("#submissions-table .submission-row"):
        # The title attribute contains the precise submission time
        seconds = float(row.select_one(".sub-usage .time")["title"][:-1])
        language = row.select_one(".sub-result .language").text
        language_times[language].append(seconds)

    # The next page button is the last list item (if it exists)
    next_page_selector = ".top-pagination-bar .pagination li:nth-last-child(1)"
    next_page_el = soup.select_one(next_page_selector)
    if next_page_el is None:  # Button doesn't exist
        break
    if "disabled-page" in next_page_el.get("class", []):  # This is last page
        break

    # Wait a bit because we're nice ~~and cuz we don't wanna get captcha'd~~
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, f"{next_page_selector} a").click()

driver.close()

# Output average time and # of submissions from fastest to slowest language
for language in sorted(
    language_times.keys(),
    key=lambda language: statistics.mean(language_times[language]),
):
    times = language_times[language]
    print(f"{language:8} [{len(times):4}]: {statistics.mean(times):6.2f}")
