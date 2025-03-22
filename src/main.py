import argparse
from selenium import webdriver
from scrapers.scraper import LeetCodeScraper
from controllers.file_controller import FileController
from controllers.git_controller import GitController

def main(problem_slug, all_submissions):
    driver = webdriver.Chrome()

    FileController._ensure_problem_dir(problem_slug)
    GitController.initialize_repo()
    scraper = LeetCodeScraper(driver)
    
    try:
        result = scraper.scrape(problem_slug, all_submissions)
        print(result)
    finally:
        driver.quit()
    # solutions_meta_data = scrape_solution(driver, problem_slug)
    # get_description(driver, problem_slug)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape a LeetCode problem's solution and description.")
    parser.add_argument("--slug", type=str, required=True, help="The slug of the LeetCode problem (e.g., 'two-sum')")
    parser.add_argument("--all_submissions", action="store_true", help="Scrape all accepted submissions")

    args = parser.parse_args()
    print(args)
    main(("-").join(args.slug.lower().split()), args.all_submissions)
