import time
import pyperclip
from selenium.webdriver.common.by import By
from controllers.file_controller import FileController

def extract_runtime_details(main_div):
    status_div = main_div.find_element(By.XPATH, "./../div[2]/div/div/div[1]/div[2]") # run + mem
    return {
        "runtime": f"{status_div.find_element(By.XPATH, './span[1]').text} {status_div.find_element(By.XPATH, './/span[2]').text}",
        "percentile": status_div.find_element(By.XPATH, "./span[4]").text
    }

def extract_memory_details(main_div):
    status_div = main_div.find_element(By.XPATH, "./../div[2]/div/div/div[2]/div[2]")
    return {
        "memory": f"{status_div.find_element(By.XPATH, './span[1]').text} {status_div.find_element(By.XPATH, './/span[2]').text}",
        "percentile": status_div.find_element(By.XPATH, ".//span[4]").text
    }
def extract_language(main_div):
    return main_div.find_element(By.XPATH, "./div[1]/div").text.split()[1]

def click_copy_button(code_element):
    div = code_element.find_element(By.XPATH, "./../../div[1]/div/div")
    copy_button = div.find_element(By.XPATH, "//*[@data-icon='clone']")
    copy_button.click()

def extract_leetcode_code(driver):
    code_element = driver.find_element(By.CSS_SELECTOR, "code")
    code_element.click()

    main_div = code_element.find_element(By.XPATH, "./../../../../..") # main full code (lang + code)
    runtime_details = extract_runtime_details(main_div)
    memory_details = extract_memory_details(main_div)
    language = extract_language(main_div)

    click_copy_button(code_element)
    time.sleep(1)

    return {
        "language": language,
        "runtime_details": runtime_details,
        "memory_details": memory_details,
        "code": pyperclip.paste()
    }

def scrape_solution(driver, problem_slug):
    driver.get(f"https://leetcode.com/problems/{problem_slug}/submissions/")
    FileController.load_cookies(driver, "storage/leetcode_cookies.pkl")

    driver.refresh()
    time.sleep(5)

    submissions = driver.find_elements(By.CSS_SELECTOR, ".h-full.overflow-auto > *")

    for i, submission in enumerate(submissions[:-1]):
        status = submission.find_element(By.CSS_SELECTOR, "div > div:nth-of-type(2) > div > div > span").text.strip()

        if status == "Accepted":
            submission.click()
            time.sleep(5)

            extracted_data = extract_leetcode_code(driver)
            FileController.save_code(problem_slug, i, extracted_data['language'], extracted_data['code'])
            meta_data = {
                "runtime": extracted_data['runtime_details']['runtime'],
                "runtime_percentile": extracted_data['runtime_details']['percentile'],
                "memory": extracted_data['memory_details']['memory'],
                "memory_percentile": extracted_data['memory_details']['percentile'],
            }
            FileController.save_meta_data(problem_slug, meta_data)
            print(f"✅ Code saved successfully for {problem_slug}")
            return meta_data
    else:
        print(f"No accepted solutions found for {problem_slug}.")
        return None


