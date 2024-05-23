from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.service import Service
import time
import os
import re

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get_count(self):
        return self.count


def main(urls, debug, after):
    global driver
    os.remove('./assets/log.txt')
    open('./assets/log.txt', 'x')
    f = open("./assets/log.txt", "a") 
    f.write("Numbers with error(Phone numbers are probably wrong or the internet connection is slow):")
    f.close()
    showMessage("Starting...", "info")

    #appdata_dir = os.path.expanduser("~")
    #chrome_profile_dir = os.path.join(appdata_dir, 'snap', 'chromium', 'common', 'chromium', 'Profile 1')
    appdata_dir = os.getenv('APPDATA')
    chrome_profile_dir = os.path.join(appdata_dir, 'Local', 'Google', 'Chrome', 'User Data', 'Profile 1')
    options = webdriver.ChromeOptions()
    if debug != True:
        options.add_argument("--headless")
    options.add_argument(f"--user-data-dir={chrome_profile_dir}")
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(options=options)
    #driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'), options=options)

    counter = Counter()
    for item in urls:
        navigator_web_driver(item, after, counter)
    driver.quit()
    showMessage(f"Messages Sent! {counter.get_count()}/{len(urls)}", "info", timeout=10000)
    

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

def showMessage(message, type, timeout=3000):
    import tkinter as tk
    from tkinter import messagebox as msgb

    root = tk.Tk()
    root.withdraw()
    try:
        root.after(timeout, root.destroy)
        title = "Whatsapp Message Sender V2"
        if type == 'info':
            msgb.showinfo(title, message, master=root)
        elif type == 'warning':
            msgb.showwarning(title, message, master=root)
        elif type == 'error':
            msgb.showerror(title, message, master=root)
    except:
        pass


def navigator_web_driver(url, after,counter):
    driver.get(f"{url}")

    try:
        send_button = css_selector("span[data-icon='send']")
        if os.path.isfile("./assets/tempIMG.png"):
            if after:
                send_button.click()
                time.sleep(1)
                send_img()
                counter.increment()
                #showMessage(f"Message sent successfully for {re.search(r'phone=(\d+)', url).group(1)}", "info", timeout=1500)

            else:
                send_img()
                counter.increment()
                #showMessage(f"Message sent successfully for {re.search(r'phone=(\d+)', url).group(1)}", "info", timeout=1500)
        else: 
            send_button.click()
            time.sleep(2)
            counter.increment()
            #showMessage(f"Message sent successfully for {re.search(r'phone=(\d+)', url).group(1)}", "info", timeout=1500)

    except Exception as e:
        number = re.search(r'phone=(\d+)', url).group(1)
        #messagebox.showerror("Whatsapp Message Sender V2", f"An error occurred while sending a message to {number}")
        showMessage(f"An error occurred while sending a message to {number}", "error")
        f = open("assets/log.txt", "a")
        f.write(f"\n{number}")
        f.close()
        showMessage(f"Skipping to send the next", "info")
        print(f"Error: {e}")