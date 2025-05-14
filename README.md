
---

# **Inventory Management System**

This is a Python-based Inventory Management System built using Tkinter for the graphical user interface (GUI) and SQLite for data storage. The system allows users to manage employees, suppliers, inventory, and users with different roles (Admin, Employee, Supplier). It includes functionalities such as login, user registration, searching records, adding records, and deleting records.

---

## **Table of Contents**

* [Features](#features)
* [Technologies](#technologies)
* [Installation](#installation)
* [Usage](#usage)
* [Database Structure](#database-structure)
* [Screenshots](#screenshots)
* [Contributing](#contributing)
* [License](#license)

---

## **Features**

* **User Authentication:**

  * Login with username and password.
  * User roles: Admin, Employee, Supplier.
  * Admin can manage users (create, delete, and assign roles).

* **Employee Management:**

  * Add, view, search, and delete employee records.
  * Employees are identified by name, date of birth, and email.

* **Supplier Management:**

  * Add, view, search, and delete supplier records.
  * Suppliers are identified by name and invoice number.

* **Inventory Management:**

  * Add, view, search, and delete inventory records.
  * Inventory is managed by product name, quantity, and price.

* **Role-Based Access:**

  * Admin has access to all features and can manage users, employees, suppliers, and inventory.
  * Employee and Supplier have limited access based on their roles.

* **Search Functionality:**

  * Search records by name, email, invoice number, or role across various tabs (Employees, Suppliers, Users).

* **Delete Confirmation:**

  * Confirm deletion of records (employees, suppliers, users) before performing the action.

---

## **Technologies**

* **Python 3.x** – Core programming language.
* **Tkinter** – GUI framework for building the desktop application.
* **SQLite** – Lightweight database for storing application data.
* **Pillow (PIL)** – Used for handling image loading (optional, for icons).

---

## **Installation**

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/Inventory-Managment-System.git
   ```

2. **Install Dependencies:**

   You may need to install Tkinter and Pillow if they are not installed by default. You can install them using pip:

   ```bash
   pip install tk pillow
   ```

3. **Run the Application:**

   After the dependencies are installed, navigate to the project directory and run the application:

   ```bash
   python main.py
   ```

   This will open the login window where you can either log in or create a new account.

---

## **Usage**

* **Login:**

  * Users can log in with their username and password.
  * Admin, Employee, and Supplier roles are available.

* **Account Creation:**

  * New users can create an account by providing a username, password, and role (Admin, Employee, Supplier).

* **Dashboard:**

  * After logging in, the user will be taken to the dashboard with different tabs such as:

    * Employees: Manage employee records (Add, Delete, Search).
    * Suppliers: Manage supplier records (Add, Delete, Search).
    * Users (Admin only): Manage users (Add, Delete, Search).

* **Search:**

  * Each tab includes a search bar that allows users to search records by specific fields like name, email, or invoice number.

* **Role-Based Access:**

  * Admins can manage users, employees, suppliers, and inventory.
  * Employees and Suppliers have limited access based on their roles.

* **Delete Confirmation:**

  * Users will be prompted with a confirmation dialog before any record deletion occurs to prevent accidental data loss.

---

## **Database Structure**

The system uses SQLite with the following tables:

1. **users**

   * `id`: Primary Key (INTEGER)
   * `username`: Unique (TEXT)
   * `password`: (TEXT)
   * `name`: (TEXT)
   * `role`: (TEXT) - Can be `admin`, `employee`, or `supplier`

2. **employees**

   * `id`: Primary Key (INTEGER)
   * `name`: (TEXT)
   * `dob`: (TEXT) - Date of Birth
   * `email`: (TEXT)

3. **suppliers**

   * `id`: Primary Key (INTEGER)
   * `name`: (TEXT)
   * `invoice_no`: (TEXT)

4. **inventory**

   * `id`: Primary Key (INTEGER)
   * `product_name`: (TEXT)
   * `quantity`: (INTEGER)
   * `price`: (REAL)

---


## **Contributing**

1. Fork this repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a pull request.

---

## **License**

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**

* Thanks to the developers and contributors of the libraries used in this project (Tkinter, SQLite, Pillow).
* Special thanks to all contributors who help improve this project through feedback and pull requests.

---
