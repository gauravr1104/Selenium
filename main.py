from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def scrapping(query):

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(f"https://www.google.com/maps/search/{query}/@28.6198255,77.2983642,15z")

    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Nv2PK")))

    scrollable_div = driver.find_element(By.XPATH, '//div[@role="feed"]')
    for _ in range(3):
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div)
        time.sleep(2)

    data = []

    cards = driver.find_elements(By.CLASS_NAME, "Nv2PK")

    card_links = []
    for card in cards:
        try:
            link = card.find_element(By.TAG_NAME, 'a').get_attribute('href')
            card_links.append(link)
        except:
            continue

    for index, link in enumerate(card_links):
        try:
            driver.get(link)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "DUwDvf")))
            time.sleep(2)

            name = driver.find_element(By.CLASS_NAME, "DUwDvf").text

            try:
                address = driver.find_element(By.XPATH, '//button[@data-item-id="address"]//div[contains(@class, "Io6YTe")]').text.strip()
            except:
                address = "N/A"

            try:
                phone = driver.find_element(By.XPATH, '//button[contains(@data-item-id, "phone")]//div[contains(@class, "Io6YTe")]').text.strip()
            except:
                phone = "N/A"

            data.append({"Name": name, "Address": address, "Phone": phone})
            print(f"Scraped: {name}")
            time.sleep(1)

        except Exception as e:
            print(f"Error with card {index}: {e}")
            continue

    pd.DataFrame(data).to_csv("map_data.csv", index=False)
    driver.quit()