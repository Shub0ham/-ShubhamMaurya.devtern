from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def verify_title():
    chrome_binary_path = "binaries/Google Chrome for Testing 116.app/Contents/MacOS/Google Chrome for Testing"

    options = webdriver.ChromeOptions()
    options.binary_location = chrome_binary_path

    # Automatically download and use the latest ChromeDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(driver_version='116').install()), options=options)

    # Navigate to the website
    driver.get("https://sdetunicorns.com")

    # Get the title of the page
    title = driver.title

    # Verify the title
    expected_title = "Master Software Testing and Automation | SDET Unicorns"
    if title == expected_title:
        print("Title verification successful!")
    else:
        print(f"Title verification failed. Expected '{expected_title}', but got '{title}'.")

    # Close the browser
    driver.quit()


if __name__ == "__main__":
    verify_title()