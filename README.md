# Python Modules & Packages Project

## 📌 Project Name

**Modules & Packages in Python**

## 📖 Introduction

This project is created to understand the basic concepts of **Modules and Packages in Python**.

Python allows us to divide a large program into smaller and reusable files.
A **Module** is a Python file (`.py`) that contains functions, classes, or variables.
A **Package** is a collection of related Python modules organized inside a folder.

---

## 🎯 Objectives

The main objectives of this project are:

* To understand Python Modules.
* To understand Python Packages.
* To create and import custom modules.
* To use functions from another Python file.
* To organize multiple modules inside a package.
* To understand code reusability.
* To make Python projects more structured and maintainable.

---

## 📂 Project Structure

```text
Modules_Packages_Project/
│
├── main.py
│
├── calculator.py
│
└── mypackage/
    ├── __init__.py
    ├── addition.py
    └── multiplication.py
```

---

## 🔹 What is a Module?

A **Module** is a Python file containing Python code such as:

* Functions
* Classes
* Variables

Example:

```python
# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

We can import this module into another Python file.

```python
import calculator

print(calculator.add(10, 20))
print(calculator.subtract(20, 10))
```

---

## 🔹 What is a Package?

A **Package** is a folder that contains multiple Python modules.

Example:

```text
mypackage/
│
├── __init__.py
├── addition.py
└── multiplication.py
```

### addition.py

```python
def add(a, b):
    return a + b
```

### multiplication.py

```python
def multiply(a, b):
    return a * b
```

---

## 🔹 Importing Package Modules

We can import modules from the package:

```python
from mypackage.addition import add
from mypackage.multiplication import multiply

print(add(10, 20))
print(multiply(5, 4))
```

### Output

```text
30
20
```

---

## 🛠️ Technologies Used

* **Python 3**
* Python Modules
* Python Packages
* Functions
* Import Statements

---

## ▶️ How to Run the Project

### Step 1

Install Python 3 on your computer.

### Step 2

Open the project folder in VS Code or another Python IDE.

### Step 3

Open the `main.py` file.

### Step 4

Run:

```bash
python main.py
```

---

## 💡 Advantages of Modules and Packages

1. **Code Reusability** – Code can be reused in different programs.
2. **Easy Maintenance** – Large programs can be divided into smaller files.
3. **Better Organization** – Related modules can be grouped together.
4. **Avoid Code Duplication** – The same code does not need to be written again.
5. **Easy Debugging** – Errors can be found more easily in smaller files.

---

## 📚 Important Concepts Covered

| Concept       | Description                       |
| ------------- | --------------------------------- |
| Module        | A single Python `.py` file        |
| Package       | Collection of related modules     |
| `import`      | Used to import a module           |
| `from`        | Used to import specific items     |
| `__init__.py` | Used to identify/manage a package |
| Function      | Reusable block of code            |

---

## 📝 Conclusion

This project helps in understanding how **Modules and Packages** are used in Python.

By using modules and packages, a large Python application can be divided into smaller and reusable components. This makes the program **clean, organized, reusable, and easy to maintain**.

---

## 👨‍💻 Author

**Name:** Archana
**Subject:** Python
**Project:** Modules & Packages
