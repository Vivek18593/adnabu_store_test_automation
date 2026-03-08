# Test Automation Framework (Selenium-Python-PyTest)

## Technologies Used
- Python
- Selenium WebDriver
- PyTest
- WebDriver Manager
- PyTest HTML Reports

---

## Creating a Virtual Environment (Windows)
```bash
pip install virtualenv
python -m venv .venv
.venv\Scripts\activate
deactivate
```
    
## Creating a Virtual Environment (Linux)
```bash
pip3 install virtualenv
python3 -m venv .venv
source .venv/bin/activate
deactivate
```

## Install Project Dependencies
```bash
pip install -r requirements.txt
```

---

##  Command to Run the Tests and Generate HTML Report
```bash
pytest -v -rA tests/ --html=./reports/report.html
```








