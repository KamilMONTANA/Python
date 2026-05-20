# 🐛 Day 13: Learning Debugging

An educational reference summarizing good practices and strategies for debugging and isolating runtime exceptions in Python scripts.

## 🎯 Project Goal
To understand how to read interpreter traceback messages (stack traces), verify variable contents, and isolate sections of code to find and resolve bugs.

## ✨ Key Concepts
- **Debugging with `print()`:** The quickest approach to check the state of variables at specific points during a script's execution.
- **Utilizing the Debugger:** Working with integrated IDE debuggers (e.g. PyCharm or VS Code) to set breakpoints, step through lines (step over, step into), and monitor variables in real-time.
- **Code Isolation:** Reducing complex blocks of code down to minimal reproducible configurations to speed up troubleshooting.

## 📂 Project Structure
- `text.md` – a summary markdown file logging standard debugging workflows.

## 🎓 Key Learnings
- Reading and analyzing standard stack traces thrown by the Python interpreter.
- Using simple print checks and conditional assertions to double-check code calculations.
- Pinpointing common logical bugs (such as *off-by-one* errors, type mismatch warnings, and unwanted object mutations).
