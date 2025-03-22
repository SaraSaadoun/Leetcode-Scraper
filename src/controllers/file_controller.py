import os
import pickle
import json
from config import LANGUAGE_EXTENSIONS

class FileController:
    BASE_DIR = "./../LeetCodeSolutions"

    @staticmethod
    def _ensure_problem_dir(problem_slug):
        """Ensures that the directory for the problem exists."""
        problem_dir = os.path.join(FileController.BASE_DIR, problem_slug)
        os.makedirs(problem_dir, exist_ok=True)
        return problem_dir

    @staticmethod
    def save_cookies(driver, filepath):
        """Saves browser cookies to a file."""
        with open(filepath, 'wb') as file:
            pickle.dump(driver.get_cookies(), file)

    @staticmethod
    def load_cookies(driver, filepath):
        """Loads browser cookies from a file and adds them to the driver."""
        if os.path.exists(filepath):
            with open(filepath, 'rb') as file:
                for cookie in pickle.load(file):
                    driver.add_cookie(cookie)

    @staticmethod
    def save_code(problem_slug, solution_index, language, code):
        """Saves the extracted solution code to a file inside the problem's directory."""
        problem_dir = FileController._ensure_problem_dir(problem_slug)
        solution_subdir = os.path.join(problem_dir, f"solution_{solution_index}")
        os.makedirs(solution_subdir, exist_ok=True)
        extension = LANGUAGE_EXTENSIONS.get(language, "txt")
        filepath = os.path.join(solution_subdir, f"solution{extension}")
        with open(filepath, "w", newline='',encoding="utf-8") as f:
            f.write(code)
        return f"solution_{solution_index}"

    @staticmethod
    def save_description(problem_slug, title, html_content):
        """Saves the problem description as a markdown file inside the problem's directory."""
        problem_dir = FileController._ensure_problem_dir(problem_slug)
        filepath = os.path.join(problem_dir, "description.md")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# [{title}](https://leetcode.com/problems/{problem_slug}/)\n\n")
            f.write(html_content)

    @staticmethod
    def save_meta_data(problem_slug, solution_index, metadata):
        """Saves the problem metadata (runtime, memory, language) as a JSON file inside the problem's directory."""
        problem_dir = FileController._ensure_problem_dir(problem_slug)
        # ensure solution dir for each solutiion
        solution_subdir = os.path.join(problem_dir, f"solution_{solution_index}")
        os.makedirs(solution_subdir, exist_ok=True)

        filepath = os.path.join(solution_subdir, f"metadata.json")

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=4)
