import argparse
from selenium import webdriver
import time
import os


def scrape(url):
    """Scrape youtube url for comments"""

    content = get_content(url)

    return content


def get_content(url, headless=True, pause=4):
    """Use selenium browser automation to open a youtube url, scroll to bottom and return the full page source"""

    # Configure selenium webdriver for firefox and headless option if enabled
    options = webdriver.FirefoxOptions()
    options.headless = headless
    driver = webdriver.Firefox(firefox_options=options, service_log_path=os.devnull)

    # Load URL, if url does not exist then selenium will crash out
    driver.get(url)

    print("Successfully, loaded page.")

    time.sleep(pause)

    # Youtube does not load all comments automatically and therefore we need to scroll to the bottom of the page.
    scroll(driver)

    content = driver.page_source

    return content


def scroll(driver, pause=2, delta=300, failed_attempts=5):
    """
    Scroll to the bottom of the automated browser instance using webdriver.
    Depending on number of comments, this may take some time to scroll through to the bottom.
    inspired by https://stackoverflow.com/questions/47039874/scrape-dynamic-html-youtube-comments
    """

    print("Scrolling to bottom of page. This may take a while depending on number of comments.")

    # Try to see if window has a size (i.e not headless) otherwise we will stick with default
    height = driver.execute_script("return window.outerHeight")
    if height > 0:
        delta = height

    landed = 0
    target = delta

    failed = failed_attempts

    while True:
        driver.execute_script("window.scrollTo({},{})".format(landed, target))
        time.sleep(pause)
        landed = driver.execute_script("return window.pageYOffset")

        # i.e haven't moved
        if landed < target:
            if failed == 0:
                break
            else:
                failed -= 1
                continue
        else:
            failed = failed_attempts

        target = landed + delta

    print("Reached Bottom of Page!")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Scrape a youtube video page for all comments and save out source.')
    parser.add_argument('--url', type=str, help='URL for youtube video to scrape', required=True)
    parser.add_argument('--name', type=str, help='Filename to save page_source as.', required=True)

    args = parser.parse_args()

    content = scrape(args.url)

    with open("../../data/{}_source.html".format(args.name), 'w') as flh:
        flh.write(content)
