# 🧮 Python Calculator Project

A progressively improved calculator written in Python — built as part of my journey to master the basics of programming, logic handling, and user input validation.

The project went through several iterations. Each version added better input handling, edge-case detection, and smarter features. The final version (v2.1) represents the most stable, usable version so far.

---

## 🚀 Final Version: **V2.1 – Smart Calculator with File History**

### ✅ Key Features
- Accepts full expressions like:
8 +9 *7 /2 +5 - 100
- Auto-corrects messy input:
- Removes repeated operators like `2 +++++ 2 ➝ 2 + 2`
- Normalizes spacing around numbers and operators
- Handles expressions ending in operators (e.g. `2 +` ➝ `2 + 0`)
- Prevents divide-by-zero errors (returns `0` instead of crashing)
- Saves history with timestamps to a `.txt` file in the **Documents folder**

---

## 🔁 Version History

### 🥉 **V1 – Basic Step-by-Step Calculator**
- Prompts: First number ➝ Operator ➝ Second number  
- Supports basic operations: `+ - * /`  
- Adds timestamped calculation history (in memory only)

---

### 🥈 **V2 – Full Expression Parsing**
- Accepts full math expressions as a single line  
- Removes extra spaces and repeated operators  
- Adds input safety and divide-by-zero handling  
- History still stored in memory

---

### 🥇 **V2.1 – Final Version**
- Smarter expression sanitizing (`2 /*- 8 ➝ 2 / 8`)  
- Automatically fixes operator placement issues  
- Saves history to a persistent text file  
- More robust against invalid input

---

## 💡 Lessons Learned

- Expression parsing & cleanup  
- Defensive coding against bad user input  
- File handling in Python  
- Thinking like a user and handling real-world mistakes  
- Writing cleaner, more modular code over time

