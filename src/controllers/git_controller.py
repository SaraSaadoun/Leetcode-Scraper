import os
import subprocess

class GitController:
    """Handles Git operations for tracking new problem directories."""
    LEETCODE_SOLUTIONS_DIR = "./../LeetCodeSolutions"

    @staticmethod
    def initialize_repo():
        """Initializes a Git repository if not already initialized."""
        if not os.path.exists(os.path.join(GitController.LEETCODE_SOLUTIONS_DIR, ".git")):
            subprocess.run(["git", "init"], cwd=GitController.LEETCODE_SOLUTIONS_DIR, check=True)
            print("Initialized a new Git repository.")

    @staticmethod
    def add_and_commit(problem_slug, meta_data):
        """Adds a file to Git tracking and commits it."""
        
        try:
            subprocess.run(["git", "add", problem_slug], cwd=GitController.LEETCODE_SOLUTIONS_DIR, check=True)
            message = f"Time: {meta_data['runtime']} ({meta_data['runtime_percentile']}), Space: {meta_data['memory']} ({meta_data['memory_percentile']})"
            subprocess.run(["git", "commit", "-m", message], cwd=GitController.LEETCODE_SOLUTIONS_DIR, check=True)
            print("committed successfully..")
            print(message)
        except subprocess.CalledProcessError as e:
            print(f"Git operation failed: {e}")
