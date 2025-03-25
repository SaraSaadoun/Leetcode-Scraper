import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

class GitController:
    """Handles Git operations for tracking new problem directories."""
    LEETCODE_SOLUTIONS_DIR = os.getenv("LEETCODE_SOLUTIONS_DIR_PATH")

    @staticmethod
    def initialize_repo():
        """Initializes a Git repository if not already initialized."""
        if not os.path.exists(os.path.join(GitController.LEETCODE_SOLUTIONS_DIR, ".git")):
            subprocess.run(["git", "init"], cwd=GitController.LEETCODE_SOLUTIONS_DIR, check=True)
            print("Initialized a new Git repository.")

    @staticmethod
    def add_and_commit(path, message):
        """Adds a file to Git tracking and commits it."""
        
        try:
            subprocess.run(["git", "add", path], cwd=GitController.LEETCODE_SOLUTIONS_DIR, check=True)
            subprocess.run(["git", "commit", "-m", message], cwd=GitController.LEETCODE_SOLUTIONS_DIR, check=True)
            print("committed successfully..")
            print(message)
        except subprocess.CalledProcessError as e:
            print(f"Git operation failed: {e}")
