import argparse
from selenium import webdriver
from scrapers.code_scraper import scrape_solution
from scrapers.description_scraper import get_description
from storage.file_manager import FileManager

def main(problem_slug):
    driver = webdriver.Chrome()

    FileManager._ensure_problem_dir(problem_slug)
    scrape_solution(driver, problem_slug)
    get_description(driver, problem_slug)
    
    driver.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape a LeetCode problem's solution and description.")
    parser.add_argument("--slug", type=str, required=True, help="The slug of the LeetCode problem (e.g., 'two-sum')")

    args = parser.parse_args()
    
    main(args.slug)
