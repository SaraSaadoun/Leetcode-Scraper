import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from controllers.file_controller import FileController
from controllers.git_controller import GitController

class LeetCodeScraper:
    def __init__(self, driver):
        self.driver = driver

    def _wait_for(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def _get_accepted_subs(self, slug):
        url = f"https://leetcode.com/problems/{slug}/submissions/"
        self.driver.get(url)
        FileController.load_cookies(self.driver, "storage/leetcode_cookies.pkl")
        self.driver.refresh()
        time.sleep(5)  # Replace with explicit wait if possible
        subs = self.driver.find_elements(By.CSS_SELECTOR, ".h-full.overflow-auto > *")
        for sub in subs:
            print(sub.text)
            print(sub.text.split())
            print('-------------------')
        ac_subs = []
        for sub in subs[:-1]:
            if sub.text.split()[1] == "Accepted":
                ac_subs.append(sub)
        return ac_subs
        

    def _parse_runtime(self, container):
        status = container.find_element(By.XPATH, "./../div[2]/div/div/div[1]/div[2]")
        return {
            "runtime": f"{status.find_element(By.XPATH, './span[1]').text} {status.find_element(By.XPATH, './/span[2]').text}",
            "percentile": status.find_element(By.XPATH, "./span[4]").text
        }

    def _parse_memory(self, container):
        status = container.find_element(By.XPATH, "./../div[2]/div/div/div[2]/div[2]")
        return {
            "memory": f"{status.find_element(By.XPATH, './span[1]').text} {status.find_element(By.XPATH, './/span[2]').text}",
            "percentile": status.find_element(By.XPATH, ".//span[4]").text
        }

    def _parse_language(self, container):
        text = container.find_element(By.XPATH, "./div[1]/div").text
        return text.split()[1]  

    def _click_copy(self, code_elem):
        div = code_elem.find_element(By.XPATH, "./../../div[1]/div/div")
        copy_btn = div.find_element(By.XPATH, "//*[@data-icon='clone']")
        copy_btn.click()

    def _extract_code(self):
        code_elem = self.driver.find_element(By.CSS_SELECTOR, "code")
        code_elem.click()

        container = code_elem.find_element(By.XPATH, "./../../../../..")
        runtime_info = self._parse_runtime(container)
        memory_info = self._parse_memory(container)
        language = self._parse_language(container)

        self._click_copy(code_elem)
        time.sleep(1)  # Replace with explicit wait if possible

        return {
            "language": language,
            "runtime_info": runtime_info,
            "memory_info": memory_info,
            "code": pyperclip.paste()
        }
    
    def _scrape_description(self, slug):
        """Public: Gets and saves the problem description."""
        url = f"https://leetcode.com/problems/{slug}/"
        self.driver.get(url)

        title_elem = self.driver.find_element(By.CSS_SELECTOR, f"a[href='/problems/{slug}/']")
        # Expecting "id. Problem Name" format.
        _, _ = title_elem.text.strip().split('.', 1)
        statement = self.driver.find_element(By.CSS_SELECTOR, "div[data-track-load='description_content']")
        FileController.save_description(slug, title_elem.text.strip(), statement.get_attribute("innerHTML"))
        GitController.add_and_commit(f"{slug}/description.md", f"add {title_elem.text.strip()} description")
        print(f"✅ Description saved for {slug}")
        
    def _scrape_submission(self, slug, index, sub):
        sub.click()
        time.sleep(5)  # Replace with explicit wait if possible

        data = self._extract_code()
        solution_dir = FileController.save_code(slug, index, data['language'], data['code'])

        meta = {
            "runtime": data['runtime_info']['runtime'],
            "runtime_percentile": data['runtime_info']['percentile'],
            "memory": data['memory_info']['memory'],
            "memory_percentile": data['memory_info']['percentile']
        }
        FileController.save_meta_data(slug, index, meta)
        message = f"Time: {meta['runtime']} ({meta['runtime_percentile']}), Space: {meta['memory']} ({meta['memory_percentile']})"

        GitController.add_and_commit(f"{slug}/{solution_dir}", message)
        print(f"✅ Code saved for {slug} submission {index}")
        return meta

    def scrape(self, slug, all_submissions=False):
        """Public: Scrapes accepted submissions.
        
        If all_submissions is True, scrapes every accepted submission;
        otherwise, scrapes only the first one.
        """
        self._scrape_description(slug)
        subs = self._get_accepted_subs(slug)
        if not subs:
            print(f"No accepted solutions found for {slug}.")
            return None

        if all_submissions:
            results = []
            for i, sub in enumerate(subs):
                results.append(self._scrape_submission(slug, i, sub))
            return results
        else:
            return self._scrape_submission(slug, 0, subs[0])

    