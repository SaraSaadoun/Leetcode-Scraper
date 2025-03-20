import argparse
from selenium import webdriver
from scrapers.code_scraper import scrape_solution
from scrapers.description_scraper import get_description
from controllers.file_controller import FileController
from controllers.git_controller import GitController

def main(problem_slug):
    driver = webdriver.Chrome()

    FileController._ensure_problem_dir(problem_slug)
    GitController.initialize_repo()

    meta_data = scrape_solution(driver, problem_slug)
    get_description(driver, problem_slug)
    
    GitController.add_and_commit(problem_slug, meta_data)

    driver.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape a LeetCode problem's solution and description.")
    parser.add_argument("--slug", type=str, required=True, help="The slug of the LeetCode problem (e.g., 'two-sum')")

    args = parser.parse_args()
    
    main(("-").join(args.slug.lower().split()))
