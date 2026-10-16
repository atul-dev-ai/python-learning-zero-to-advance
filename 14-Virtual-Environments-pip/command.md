# Virtual Environment & Pip Commands Guide

## Windows (PowerShell / Command Prompt)

### 1. Folder e probesh kora
cd 14-Virtual-Environments-pip

### 2. Python version check
py --version
# ba
python --version

### 3. Virtual environment create kora
py -m venv .venv
# ba
python -m venv .venv

### 4. Environment active kora
# PowerShell er jonno:
.\.venv\Scripts\Activate.ps1

# Command Prompt (CMD) er jonno:
.\.venv\Scripts\activate.bat

### 5. Package / Library install kora
python -m pip install requests

### 6. Install kora package er list dekha
python -m pip list

### 7. requirements.txt file create kora
python -m pip freeze > requirements.txt

### 8. Environment deactivate kora
deactivate

---

## Linux / macOS (Bash / Zsh)

### 1. Folder e probesh kora
cd 14-Virtual-Environments-pip

### 2. Python version check
python3 --version

### 3. Virtual environment create kora
python3 -m venv .venv
# Linux e proyojon hole: sudo apt install python3-venv

### 4. Environment active kora
source .venv/bin/activate

### 5. Package / Library install kora
python3 -m pip install requests
# ba environment active thakle shorashori:
pip install requests

### 6. Install kora package er list dekha
pip list

### 7. requirements.txt file create kora
pip freeze > requirements.txt

### 8. Environment deactivate kora
deactivate

---

## Extra: requirements.txt theke sob install kora
pip install -r requirements.txt