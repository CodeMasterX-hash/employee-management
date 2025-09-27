# Employee Data Management System 👨‍💼👩‍💼

A full **Django application** to manage employee data with CRUD (Create, Read, Update, Delete) functionality.  
This project is built for the ASE Challenge 2025 and demonstrates fullstack skills using **Django templates** and **Bootstrap**.

---

## Features
- Add, view, edit, and delete employees
- Search/filter employees by name
- Form validation (valid email, required fields)
- Success/error messages after actions
- Bootstrap styled UI for better look
- Fully responsive interface

---

## Tech Stack
- Backend: Django (Python)
- Frontend: Django Templates + Bootstrap
- Database: SQLite (default Django DB)
## Project Structure
employee_management/ <- Project root
│── manage.py
│── db.sqlite3
│── README.md <- This file
│── employee_management/ <- Django settings folder
│ ├── urls.py
│ ├── settings.py
│── employees/ <- Django app
├── models.py
├── views.py
├── urls.py
├── forms.py
├── templates/employees/
├── index.html
├── add.html
├── edit.html
## Setup &1. **Clone the repository**
```bash
git clone https://github.com/<your-username>/employee-management.git
cd employee-management
 Run Locally
Usage

View all employees in a table

Add new employee → fill the form → submit

Edit employee → click "Edit" → update → save

Delete employee → click "Delete" → confirm

Search employee → enter name → filter results

Form Validation & Business Logic

Name: Required, max 100 characters

Email: Required, unique, valid email format

Position: Required, max 100 characters

Success/Error messages appear after actions

Search: Case-insensitive, matches anywhere in employee name
Testing

You can manually test your app:

Add an employee → check it appears in the list

Edit an employee → check data updates

Delete an employee → check it is removed

Search → enter name → table filters results

Form validation → try empty or invalid email → should show error
Design Choices & Assumptions

Django templates used instead of React for simplicity

Bootstrap used for clean UI and responsive design

SQLite chosen for easy local setup

Each employee email must be unique

Future Improvements

Pagination for large employee lists

Employee profile pictures

Roles and permissions for admin/staff

Switch to PostgreSQL/MySQL for production

Author

Tammineni Kishore reddy

ASE Challenge 2025 Submission 🚀
