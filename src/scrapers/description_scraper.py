from selenium.webdriver.common.by import By
from storage.file_manager import FileManager

def get_description(driver, problem_slug):
    url = f"https://leetcode.com/problems/{problem_slug}/"
    driver.get(url)

    problem_title = driver.find_element(By.CSS_SELECTOR, f"a[href='/problems/{problem_slug}/']")
    problem_id, problem_name = problem_title.text.strip().split('.')
    problem_statement = driver.find_element(By.CSS_SELECTOR, "div[data-track-load='description_content']")
    
    FileManager.save_description(problem_slug, problem_title.text.strip(), problem_statement.get_attribute("innerHTML"))
    
