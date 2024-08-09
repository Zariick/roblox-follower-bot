from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import InvalidSelectorException, NoSuchElementException
from concurrent.futures import ThreadPoolExecutor
import time

# Past the link to your profile which you want to follow
URL = "https://www.roblox.com/users/yourid/profile"

# Here is the dictionary of your accounts, you can write multiple lines of that, but make sure it doesn't crash
accounts = [
    {"username": "YOURUSERNAME", "password": "YOURPASSWORD"},
    {"username": "YOURUSERNAME", "password": "YOURPASSWORD"},
]


# Function to perform actions to your windows
def login_and_register(username, password):
    # Setting up
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    try:
        driver.get(url=URL)
        time.sleep(3)

        login_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div/div[2]/div[2]/ul/li[2]/a')
        login_button.click()

        time.sleep(3)
        username_field = driver.find_element(By.ID, "login-username")
        username_field.send_keys(username)

        password_field = driver.find_element(By.ID, "login-password")
        password_field.send_keys(password)
        password_field.send_keys(Keys.ENTER)

        # Wait for the page to load, if your internet connection good u can reduce the time
        time.sleep(6)

        opt = driver.find_element(By.XPATH, "/html/body/div[3]/main/div[2]/div[1]/div/div[1]/div/div/div/div[3]/div/button/span[2]")
        opt.click()
        time.sleep(2)

        follow_button = driver.find_element(By.XPATH, "/html/body/div[3]/main/div[2]/div[1]/div/div[1]/div/div/div/div[3]/div/ul/li[1]/a")
        follow_button.click()
        print("Followed successfully")
        time.sleep(2)
        print("Closing windows...")
    except InvalidSelectorException:
        print("Something went wrong, please review the requirements for the bot")
    except NoSuchElementException:
        print("Something went wrong, please review the requirements for the bot")
    finally:
        driver.quit()


# Using ThreadPoolExecutor to run multiple tasks, instead of max_forkers=2, place the number that how many accounts you have
with ThreadPoolExecutor(max_workers=2) as executor:
    futures = [executor.submit(login_and_register, acc['username'], acc['password']) for acc in accounts]

    # Wait for all tasks to complete
    for future in futures:
        future.result()