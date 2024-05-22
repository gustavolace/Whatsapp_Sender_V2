from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import os 


def main(urls, debug, after):
    global count, driver
    appdata_dir = os.path.expanduser("~")
    chrome_profile_dir = os.path.join(appdata_dir, 'snap', 'chromium', 'common', 'chromium', 'Profile 1')
    options = webdriver.ChromeOptions()
    if debug != True:
        options.add_argument("--headless")
    options.add_argument(f"--user-data-dir={chrome_profile_dir}")
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    options.add_argument(f'user-agent={user_agent}')
    #driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'), options=options)
    #appdata_dir = os.getenv('APPDATA')
    #chrome_profile_dir = os.path.join(appdata_dir, 'Local', 'Google', 'Chrome', 'User Data', 'Profile 1')
    for item in urls:
        navigator_web_driver(item, after)
    driver.quit()
    

def css_selector(selector):
    return WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CSS_SELECTOR, f"{selector}")))

def send_img():
    attach_icon = css_selector("span[data-icon='attach-menu-plus']")
    attach_icon.click()
    input_file = css_selector("input[accept='image/*,video/mp4,video/3gpp,video/quicktime']")
    input_file.send_keys(rf"{os.path.abspath("./assets")}/tempIMG.png")

    time.sleep(1)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(2)
    print()


def navigator_web_driver(urls, after):
    driver.get(f"{urls}")

    try:
        send_button = css_selector("span[data-icon='send']")
        if os.path.isfile("./assets/tempIMG.png"):
            if after:
                send_button.click()
                time.sleep(1)
                send_img()

            else:
                send_img()

        else: 
            send_button.click()
            time.sleep(2)

    except Exception as e:
        print(f"Erro durante a interação: {e}")