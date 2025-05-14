---

# **Inventory Management System**

This Inventory Management System is a comprehensive and user-friendly application designed to manage employees, suppliers, users, and inventory within an organization. It provides functionalities like adding, viewing, searching, and deleting records for employees, suppliers, and users. Additionally, it supports user authentication, including a login system and user role management (Admin, Employee, Supplier).

---

## **Table of Contents**

* [Features](#features)
* [Technologies](#technologies)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Database Schema](#database-schema)
* [Screenshots](#screenshots)
* [Contributing](#contributing)
* [License](#license)

---

## **Features**

* **User Authentication:**

  * Admin, Employee, and Supplier roles.
  * Login functionality.
  * Create new user accounts.

* **Manage Employees:**

  * Add, edit, delete, and view employee details (name, date of birth, email).
  * Search employees by name or email.

* **Manage Suppliers:**

  * Add, edit, delete, and view supplier details (name, invoice number).
  * Search suppliers by name or invoice number.

* **Manage Inventory:**

  * View and manage inventory (product name, quantity, price).
  * Search inventory items by name or price.

* **Manage Users (Admin only):**

  * Add, edit, delete, and view user details (username, name, role).
  * Search users by username, name, or role.

* **Search Functionality:**

  * Search across all tabs (Employees, Suppliers, Users).

---

## **Technologies**

This application is built using the following technologies:

* **Python** – The core programming language.
* **Tkinter** – For building the graphical user interface (GUI).
* **SQLite** – Lightweight database for storing data.
* **Pillow (PIL)** – For handling image operations (optional).
* **SQLAlchemy (optional)** – For ORM database operations (not implemented in this version).

---

## **Requirements**

Before running this application, ensure that you have the following software installed:

* Python 3.x
* SQLite (comes bundled with Python)

You will also need to install the required libraries by running the following:

```bash
pip install -r requirements.txt
```

If `requirements.txt` does not exist, install the required libraries manually:

```bash
pip install tk pillow
```

---

## **Installation**

1. Clone the repository:

```bash
git clone https://github.com/B-6219/Inventory-Manangement-System.git
```

2. Navigate to the project directory:

```bash
cd Inventory-Manangement-System
```

3. Run the application:

```bash
python main.py
```

---

## **Usage**

* **Login/Sign Up:**

  * Upon launching the app, you will be presented with a login screen.
  * You can either log in with an existing user account or create a new one.
  * Admin, Employee, and Supplier roles are supported, and each role has different access permissions.

* **Dashboard:**

  * After logging in, you will be redirected to the dashboard where you can access different tabs such as Employees, Suppliers, Inventory, and Users (Admin only).
  * Each tab has options to view, search, add, and delete records.

* **Search:**

  * You can search through the records in all tabs (Employees, Suppliers, and Users) by typing in the search bar at the top of each tab.

* **Admin Features:**

  * Admin users can manage users by adding, editing, and deleting users. Only Admins can perform these actions.

---

## **Database Schema**

The application uses **SQLite** as its database and has the following tables:

1. **users**

   * `id` (Primary Key)
   * `username` (Unique)
   * `password`
   * `name`
   * `role` (Admin, Employee, Supplier)

2. **employees**

   * `id` (Primary Key)
   * `name`
   * `dob` (Date of Birth)
   * `email`

3. **suppliers**

   * `id` (Primary Key)
   * `name`
   * `invoice_no` (Invoice Number)

4. **inventory**

   * `id` (Primary Key)
   * `product_name`
   * `quantity`
   * `price`

---

## **Screenshots**

![Login Screen](assets/login_screen.png)

*Sample login screen.*

![Employee Management](assets/employee_management.png)

*Employee management tab where you can add, view, search, and delete employees.*

![Supplier Management](assets/supplier_management.png)

*Supplier management tab where you can add, view, search, and delete suppliers.*

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

-
