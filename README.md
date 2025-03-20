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

## 📂 Project Structure 
``` 
│── LeetCodeSolutions/ 
│── src/ │ 
├── controllers/ 
│ │ ├── file_controller.py 
│ │ ├── git_controller.py 
│ ├── scrapers/ 
│ │ ├── code_scraper.py 
│ │ ├── description_scraper.py 
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
python auth.py
python main.py --slug problem-slug-here
```
