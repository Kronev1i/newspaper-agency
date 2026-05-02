

# Newspaper Agency 📰
Newspaper Agency is a comprehensive web application for managing a news agency's internal operations, built with Python and Django. It allows for efficient tracking of newspapers, topics, and redactors, ensuring a smooth content management workflow.

# 🚀 Key Features
Authentication & Access Control: Secure access ensured by Django’s authentication system; all core features require login.

Advanced Search Engine: Real-time filtering for newspapers by title, topics by name, and redactors by username using icontains logic.

Content Management (CRUD): Full ability to Create, Read, Update, and Delete newspapers, topics, and redactor profiles.

Optimized Database Queries: Implementation of select_related and prefetch_related to minimize database hits and prevent N+1 problems.

Professional UI: Styled with the Lux theme (Bootstrap 5) for a clean, modern, and dark-themed aesthetic.

Custom Pagination: All list views are paginated for better performance and user experience.

# 🛠 Tech Stack
Backend: Python 3.12+, Django 5.x.

Database: SQLite (Development) / PostgreSQL (Production).

Frontend: HTML5, CSS3, Bootstrap 5 (Lux Bootswatch theme).

Code Quality: Flake8 for linting, PEP 8 compliance.

# 📦 Installation & Setup
1. Clone the repository:
git clone 
cd newspaper-agency

2. Set up a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Apply migrations:
python manage.py migrate

5. Load sample data (Fixtures):
python manage.py loaddata fixtures.json

6. Run the development server:
python manage.py runserver

# 🧪 Testing
The project includes a suite of unit tests to verify search functionality, form validation, and access rights.

To run all tests, execute the following command:
python manage.py test

Bash
python manage.py test

# 🧹 Code Quality
- This project strictly adheres to PEP 8 standards:

- Flake8: The codebase passes all linting checks without any suppressions.

- Docstrings: All views, models, and forms are documented using Python docstrings for better maintainability.
# Link
https://newspaper-agency-2.onrender.com
Test-user:
Username: Kirill
Password: Kirill@@@2006
