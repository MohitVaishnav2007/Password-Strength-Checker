# 🔐 Password Strength Checker

A user-friendly web application that evaluates the strength of passwords in real-time. Built using **Flask** for the backend and **HTML, CSS, JavaScript (jQuery)** for the frontend, this tool provides instant feedback, helping users create secure passwords.

---

## 📋 Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

---

## 🚀 Features

- **Real-Time Analysis**: Instantly evaluates password strength as users type.
- **Password Visibility Toggle**: Allows users to show or hide their password input.
- **Secure Password Generation**: Generates strong, random passwords.
- **Copy to Clipboard**: Easily copy generated passwords with a single click.

---


## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/MohitVaishnav2007/Password-Strength-Checker.git
cd Password-Strength-Checker
```

### 2. Create a Virtual Environment

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📈 Usage

### 1. Run the Application

```bash
python app.py
```

### 2. Access the Application

Open your web browser and navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📁 Project Structure

```plaintext
Password-Strength-Checker/
├── .streamlit/
├── controllers/
├── services/
├── utils/
├── app.py
├── generated-icon.png
├── pyproject.toml
├── uv.lock
└── README.md
```

- `.streamlit/`: Configuration files for Streamlit (if used).
- `controllers/`: Handles the routing and logic for different endpoints.
- `services/`: Contains the core functionality and business logic.
- `utils/`: Utility functions used across the application.
- `app.py`: Main application file that initializes and runs the Flask app.
- `generated-icon.png`: Icon used in the application.
- `pyproject.toml`: Project metadata and dependencies.
- `uv.lock`: Lock file for dependencies.

---

## 🧰 Technologies Used

- **Frontend**: HTML, CSS, JavaScript (jQuery)
- **Backend**: Flask (Python)
- **Version Control**: Git & GitHub

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---
