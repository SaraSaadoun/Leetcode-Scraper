from selenium import webdriver
from selenium.webdriver.common.by import By
from storage.file_manager import FileManager

def authenticate_leetcode(driver):
    driver.get("https://leetcode.com/accounts/login/")
    print(driver.title)
    input("Please log in to LeetCode and press Enter here to continue...")
    FileManager.save_cookies(driver, "storage/leetcode_cookies.pkl")

if __name__ == "__main__":
    driver = webdriver.Chrome()
    authenticate_leetcode(driver)
    driver.quit()


