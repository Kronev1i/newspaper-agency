

# Newspaper Agency 📰
Newspaper Agency is a comprehensive web application for managing a news agency's internal operations, built with Python and Django. It allows for efficient tracking of newspapers, topics, and redactors, ensuring a smooth content management workflow.

# 🚀 Key Features
Authentication & Access Control: Secure access ensured by Django’s authentication system; all core features require login.

Advanced Search Engine: Real-time filtering for newspapers by title, topics by name, and redactors by username using icontains logic.

Content Management (CRUD): Full ability to Create, Read, Update, and Delete newspapers, topics, and redactor profiles.

Optimized Database Queries: Implementation of select_related and prefetch_related to minimize database hits and prevent N+1 problems.

Professional UI: Styled with the Lux theme (Bootstrap 5) for a clean, modern, and dark-themed aesthetic.

Custom Pagination: All list views are paginated for better performance and user experience.

# 🔌 REST API Architecture
The project features a fully exposed RESTful API ecosystem powered by Django REST Framework (DRF) to support mobile clients, front-end frameworks, or external integrations.

Authentication: Secure endpoints protected by JSON Web Token (JWT) authentication via Simple JWT. Anonymous access to data-modifying endpoints is strictly denied.

Endpoints Structure:
* `POST /api/schema/token/` — Obtain a pair of JWT access and refresh tokens.
* `POST /api/schema/token/refresh/` — Refresh an expired JWT access token.
* `GET /api/newspapers/` — Retrieve a paginated list of all newspapers with nested topic and publisher structures.
* `POST /api/newspapers/` — Create a new newspaper record (requires authentication, expects `topic_id` and `publisher_ids` payload).

Data Serialization: Optimized with dual-purpose fields to provide rich embedded object representations on read operations (GET) while maintaining high performance using ID arrays for write operations (POST/PUT).

# 🛠 Tech Stack
Backend: Python 3.12+, Django 5.x.

Database: SQLite (Development) / PostgreSQL (Production).

Frontend: HTML5, CSS3, Bootstrap 5 (Lux Bootswatch theme).

Code Quality: Flake8 for linting, PEP 8 compliance.

# 📦 Installation & Setup
Clone the repository:

```bash
git clone <your-repository-url>
cd newspaper-agency
```
Set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
Install dependencies:

```bash
pip install -r requirements.txt
```
Apply migrations:

```bash
python manage.py migrate
```
Load sample data (Fixtures):

```bash
python manage.py loaddata fixtures.json
```
Run the development server:

```bash
python manage.py runserver
```

# 🤖 GitHub Actions CI/CD
The project integrates a Continuous Integration (CI) pipeline powered by GitHub Actions to automate code quality control and testing on every code change.

Automated Workflow: The pipeline is automatically triggered on every push or pull request targeting the main branches.

Execution Stages:
* Environment Setup — Spins up a Linux runner with Python 3.12 and installs all project dependencies from `requirements.txt`.
* Code Linting — Runs Flake8 static analysis across the entire codebase to guarantee absolute compliance with PEP 8 standards.
* Test Automation — Builds an isolated testing environment, initializes the database, and executes the entire Django/DRF test suite.

Status Badges: Ensures that no broken tests or non-compliant code can be merged into production branches unnoticed.

# 🧪 Testing
The project includes a suite of unit tests to verify search functionality, form validation, and access rights.
To run the tests, use:

```bash
python manage.py test
```
## 🐳 Running with Docker

Prerequisites: Docker and Docker Compose installed.

```bash
git clone https://github.com/Kronev1i/newspaper-agency
cd newspaper-agency
cp .env.sample .env
docker-compose up --build
```

The application will be available at http://localhost:8000
# 🧹 Code Quality
This project strictly adheres to PEP 8 standards:

Flake8: The codebase passes all linting checks without any suppressions.

Docstrings: All views, models, and forms are documented using Python docstrings for better maintainability.
