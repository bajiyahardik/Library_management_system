# Bank Management System

## Description
The **Bank Management System** is a simple desktop application built using Python's Tkinter library and MySQL. This project allows users to create accounts, log in, and perform basic banking operations such as deposits and withdrawals.

---

## Features
- **User Account Management**: Create new user accounts and store them securely in a MySQL database.
- **Login System**: Authenticate users with username and password.
- **Deposit Funds**: Add money to user accounts.
- **Withdraw Funds**: Safely withdraw money, ensuring sufficient balance.
- **Real-Time Balance Update**: Display the updated account balance after every transaction.

---

## Technologies Used
- **Python** (Tkinter for GUI development)
- **MySQL** (for database management)

---

## Prerequisites
- Python 3.x installed on your system.
- MySQL server running locally or on a remote server.
- Python libraries: `tkinter`, `mysql-connector-python`

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/bank-management-system.git
   cd bank-management-system
   ```

2. **Set Up the Database**:
   - Open MySQL Workbench or any MySQL client.
   - Run the following commands to create the database and table:
     ```sql
     CREATE DATABASE bank_management;
     USE bank_management;

     CREATE TABLE users (
         id INT AUTO_INCREMENT PRIMARY KEY,
         username VARCHAR(255) NOT NULL UNIQUE,
         password VARCHAR(255) NOT NULL,
         balance FLOAT DEFAULT 0.0
     );
     ```

3. **Install Dependencies**:
   - Install the required Python libraries:
     ```bash
     pip install mysql-connector-python
     ```

4. **Configure Database Connection**:
   - Update the database credentials in the script:
     ```python
     connection = mysql.connector.connect(
         host="localhost",
         user="your-username",
         password="your-password",
         database="bank_management"
     )
     ```

5. **Run the Application**:
   ```bash
   python main.py
   ```

---

## Usage

1. Launch the application.
2. Use the **Create Account** button to register a new user.
3. Log in with your credentials.
4. Use the dashboard to:
   - Check your account balance.
   - Deposit funds.
   - Withdraw funds.

---

## File Structure
```
project-directory/
├── main.py              # The main script to run the application
├── README.md            # This README file
└── requirements.txt     # List of dependencies (if required)
```

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments
- Thanks to [OpenAI](https://openai.com) for assistance in creating this README.
- Inspired by Python and MySQL integration tutorials.

---

## Download
[Download the Project](https://github.com/your-username/bank-management-system/archive/refs/heads/main.zip)
