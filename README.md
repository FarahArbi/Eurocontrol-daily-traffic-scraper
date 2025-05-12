# ✈️ Eurocontrol Daily Traffic Scraper
This project is a simple Python-based web scraper that automates the extraction of daily air traffic statistics from Eurocontrol's Daily Traffic Variation by State webpage.

The scraper uses Selenium and BeautifulSoup to navigate the site, extract the latest air traffic data, and save it to a CSV file for further analysis.
---

## 🚀 Features

- Scrapes daily air traffic variation data from Eurocontrol's public dashboard.
- Extracts both table data and the associated report date.
- Saves the results as a clean, structured `.csv` file.
- Automatically handles Edge WebDriver installation using `webdriver-manager`.

---

## 🧰 Technologies Used

- Python
- Selenium (for browser automation)
- BeautifulSoup (for HTML parsing)
- pandas (for data handling)
- webdriver-manager (for EdgeDriver setup)

---

## 📁 Files

- `scraper.py`: The main scraping script.
- Output: A `.csv` file named with the report date (e.g., `Monday 6 May 2024.csv`).

---

## 🔧 Setup & Installation

1. **Clone the repo**:
   ```bash
   git clone https://github.com/your-username/data-scraping-using-selenium.git
   cd data-scraping-using-selenium

2. **Install dependencies:**:
   ```bash
   pip install -r requirements.txt

3. **Install dependencies:**:
   ```bash
   python scraper.py

## ⚠️ Notes: 
- The script includes a time.sleep(5) delay to ensure the page loads fully before scraping. You may adjust this delay if needed.
- Data scraped is for research and educational purposes only.
- Please ensure compliance with Eurocontrol’s data usage policy before redistributing scraped content.