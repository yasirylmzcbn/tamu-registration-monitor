from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import random
import os
from dotenv import load_dotenv
from plyer import notification

load_dotenv("credentials.env")
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(
    "https://tamu.collegescheduler.com/terms/Spring%202025%20-%20College%20Station/courses/5246404"
)

# enter email
email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@type="email"]'))
)
email_input.send_keys(email)
email_input.send_keys(Keys.RETURN)
sleep(1)
passw_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))
)
passw_input.send_keys(password)
sleep(1)
passw_input.send_keys(Keys.RETURN)

trust_browser = WebDriverWait(driver, 25).until(
    EC.presence_of_element_located((By.ID, "trust-browser-button"))
)
trust_browser.click()

stay_signed_in = WebDriverWait(driver, 25).until(
    EC.presence_of_element_located((By.ID, "idSIButton9"))
)
stay_signed_in.click()

fall2025 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "fall-2025---college-station-options"))
)
fall2025.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//button[.//span[text()="Save and Continue"]]')
    )
).click()

crns = {"POLS 207": ["33048", "45758"], "VIST 386": ["59721"]}


def send_notif(class_name, crn, seats_open):
    notification.notify(
        title=f"{crn} Available",
        message=f"{class_name} has {seats_open} seats open",
        timeout=10,  # Notification stays up for 10 seconds
    )


def check_for_updates():
    title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1"))
    )
    class_name = title.text[0:5] + title.text[-3:]
    for _ in range(6):
        try:
            table = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//table"))
            )
            rows = table.find_elements(By.XPATH, "//tbody")
            for row in rows:
                class_info = row.text.split("\n")[1].split(" ")
                crn = class_info[0]
                seats = class_info[5]
                if crn in crns[class_name]:
                    print("found:", crn)
                    print("seats open:", seats)
                    send_notif(class_name, crn, seats)
        except Exception as e:
            print("error:", e)
        sleep(10)
        driver.refresh()


sleep(5)
tbodies = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//tbody"))
)

for key in crns:
    try:
        tbody = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, f"//tbody[contains(., '{key}') and contains(., 'Sections')]")
            )
        )
        WebDriverWait(tbody, 10).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Sections"))
        ).click()
        check_for_updates()
        driver.back()
        sleep(5)
    except Exception as e:
        print("error:", e)
