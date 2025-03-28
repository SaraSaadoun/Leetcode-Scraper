# 🚀 LeetCode Scraper  

Automate the process of saving your LeetCode solutions with ease! This scraper **authenticates**, **extracts solutions**, **saves metadata**, and **commits automatically using Git**.  

## 🔹 Features  
✅ **Authenticates** on LeetCode  
✅ **Scrapes** code, language, runtime, memory, and problem description  
✅ **Adjusts file extensions** based on the detected programming language  
✅ **Saves metadata** (runtime & memory) in a JSON file  
✅ **Stores problem descriptions** in a Markdown file  
✅ **Organizes everything** in a directory named after the problem slug  
✅ **Commits** automatically using Git after scraping 🎯  
✅ Choose what to scrape → Select all submissions or just the latest one! 🔄 

## 📂 Project Structure 
``` 
│── LeetCodeSolutions/ 
│── src/ │ 
├── controllers/ 
│ │ ├── file_controller.py 
│ │ ├── git_controller.py 
│ ├── scrapers/ 
│ │ ├── scraper.py 
│ ├── storage/ 
│ │ ├── leetcode_cookies.pkl 
│ ├── auth.py 
│ ├── config.py 
│ ├── main.py 
│── .gitignore 
│── README.md 
│── requirements.txt
```

## 🛠️ Installation  

```bash
git clone https://github.com/SaraSaadoun/Leetcode-Scraper.git  
cd Leetcode-Scraper  
pip install -r requirements.txt
```

### 🔹 Setup `.env` File  
Before running the script, create a `.env` file in the project directory and define the absolute path where you want to save the scraped solutions:

```
LEETCODE_SOLUTIONS_DIR_PATH=/absolute/path/to/save/solutions
```

---

## 🚀 Running the Scraper  

```bash
cd src
python auth.py
python main.py --slug problem-slug-here
```

### 🔹 Usage Notes  
- The `--slug` argument accepts both **problem slugs** (e.g., `two-sum`) and **problem names** (e.g., `"Two Sum"`).  
- If you want to scrape **all accepted solutions** instead of just the latest one, pass the `--all_submissions` flag:  

```bash
python main.py --slug problem-slug-here --all_submissions
```

---

## 🖥️ Running with UI  
For a simpler experience, you can run the scraper with a graphical user interface:  

```bash
python main_ui.py
```

This will allow you to input the problem name/slug and choose options interactively.

