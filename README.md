#  Project 1: Password Generator

## Description
A beginner-friendly **password generator** built with Python. It creates strong, random passwords and evaluates their strength based on character variety and length. 
## Features
- Ensures password complexity (uppercase, lowercase, digits, symbols)
- Checks password strength: Weak, Medium, or Strong
- Option to include/exclude symbols
- GUI version available using Tkinter

---

#  Project 2: IP List Cleaner

## Description
**IP List Cleaner** is a simple Python script to update a list of IP addresses by removing unwanted entries. It's useful for system admins or security teams working with IP allowlists or denylists.

## Features
- Reads IPs from a text file  
- Removes specified IP addresses  
- Overwrites the original file with updated list  


# Project 3 : Port Scanner with Threading and Logging

## Description
A beginner-friendly **Port Scanner** built with Python that scans a range of ports on a given IP address or domain to check which ports are open or closed. It uses **multithreading** to speed up scanning and logs the results to a text file for later analysis.

## Features

- Scan a custom range of ports
- Fast scanning with multithreading
- Logs all open/closed ports to `scan_results.txt`
- User-friendly input prompts
- Works on both IPs and domain names


## 🛠️ How It Works

- Takes user input for the target (IP/domain) and port range
- Scans each port in the range using separate threads
- For each port:
  - If it's open → ✅ printed to terminal and saved to `scan_results.txt`
  - If it's closed → ❌ printed to terminal and saved to `scan_results.txt`

---

## 🚀 How to Run (CLI Version)
```bash
##Project 1
python PassGenerator.py
##Project 2:
python IP-List-cleaner.py
##Project 3
python PortScanner.py
