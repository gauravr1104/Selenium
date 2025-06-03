# Selenium Web Scraping Project

This project is a Python-based web scraping tool that uses **Selenium** to collect data from websites. It is divided into **Backend** and **Frontend** components for better modularity and maintainability.

---

## 📁 Project Structure

Selenium-main/
├── Web Scraping/
│ ├── Backend/
│ │ ├── main.py
│ │ ├── map_data.csv
│ ├── Frontend/
│ │ ├── frontend.py

---

## ⚙️ Features

- Automated web scraping using Selenium.
- Modular backend for handling scraping and data processing.
- Simple frontend interface for interaction or control.
- CSV export of scraped data.

---

## 🚀 Getting Started

### 1. **Clone the repository**
bash
git clone https://github.com/gauravr1104/Selenium-main.git
cd Selenium-main/Web\ Scraping
2. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is not available, manually install:

bash
Copy
Edit
pip install selenium
3. Run the Backend
bash
Copy
Edit
cd Backend
python main.py
4. Run the Frontend (if needed)
bash
Copy
Edit
cd ../Frontend
python frontend.py
🛠️ Dependencies
Python 3.7+

Selenium

CSV (standard library)

📊 Output
Scraped data is saved in a CSV file: map_data.csv

