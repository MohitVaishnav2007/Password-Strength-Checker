## 🔒 Password Strength Checker Tool

This Python-based Password Strength Checker evaluates the security of your passwords by checking for:

Password length

Uppercase & lowercase characters

Digits

Special characters

Common password usage (against a dictionary file)


It provides actionable suggestions to improve password strength and helps raise cybersecurity awareness.


---

## 🚀 Features

✅ Password length check (minimum 8 characters)

✅ Checks for uppercase, lowercase, digits, and special characters

✅ Warns if password is too common (from common_passwords.txt)

✅ Suggests improvements for weak passwords

✅ Masked password input for privacy

✅ Option to save a detailed password report in a text file



---

## 🔧 Technologies Used

Python 3

re (Regular Expressions)

getpass (Secure Password Input)

File Handling (open)



---

## 📂 Project Structure
```
📂 Password Strength Checker/
🔁
🐃 password_checker.py           # Main Python script
🐃 common_passwords.txt          # List of common weak passwords
🐃 password_report.txt           # Saved password reports (Optional, auto-generated)
```

---

## 📝 How to Use

1. Clone this repo or download the script.


2. Ensure common_passwords.txt is present with some common passwords like:


```
123456
password
admin
qwerty
letmein
```
3. Run the script:



python password_checker.py

4. Enter your password (input will be hidden).


5. View password strength and suggestions.


6. Optionally, save a report.




---

## 💡 Example Output

Password Strength: Moderate
Suggestions to Improve:
- Include at least one special character.
- Avoid using common passwords.


---

## 👑 Sample Report (password_report.txt)

Password Tested: ************
Strength Level: Moderate
Remarks:
- Include at least one special character.
- Password is too common. Avoid using easily guessable passwords.
----------------------------------------


---

## 🌟 Learning Outcome

Password Security Fundamentals

Regular Expressions (Regex)

Secure Input Handling

File Operations in Python

Cybersecurity Tool Development



---

## 👨‍💼 Author

Mohit Vaishnav


---

## ✅ License

This project is for educational purposes only. Please do not use it for malicious activities.


---