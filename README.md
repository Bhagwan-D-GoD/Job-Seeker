# Django Job Finder Application (Backend Only)

## Overview

This Django-based backend-only application provides core functionalities for a job finder service. It includes features for job seekers to search and apply for jobs, as well as for admins to manage job postings and applications. The application uses Django REST Framework for building the API and includes token-based authentication.

## Features

### For Job Seekers
- **Registration & Login**: User authentication using Django's built-in system.
- **Profile Management**: Create and update user profiles including name, skills, and experience.
- **Job Search**: Search for jobs with filters like job title, location, and salary.
- **Job Application**: Apply for jobs via API endpoints and track applications.

### For Admins/Employers
- **Job Management**: Create, edit, and delete job postings via API.
- **Application Management**: View and manage job applications.

## Installation

To get started with the Django Job Finder application, follow these steps:

1. **Clone the Repository**
    ```bash
    git clone https://github.com/Bhagwan-D-GoD/Job-Seeker
    cd job-finder-app
    ```

2. **Set Up a Virtual Environment**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**
    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**
    ```bash
    python manage.py runserver
    ```

The application should now be running at `http://127.0.0.1:8000/`.

## API Endpoints

### Authentication
- **Register User**: `register/` (POST)
  - **Request Body**:
    ```json
    {
      "username": "testuser",
      "password": "password123"
    }
    ```
  - **Response**:
    ```json
    {
      "token": "your_auth_token_here"
    }
    ```

- **Login**: `login/` (POST)
  - **Request Body**:
    ```json
    {
      "username": "testuser",
      "password": "password123"
    }
    ```
  - **Response**:
    ```json
    {
      "token": "your_auth_token_here"
    }
    ```

### Job Management
- **List Jobs**: `jobs/` (GET)
- **Create Job**: `jobs/create/` (POST)
  - **Request Body**:
    ```json
    {
      "title": "Software Developer",
      "description": "A job description",
      "location": "Remote",
      "salary": 60000
    }
    ```

- **Update/Delete Job**: `jobs/<int:pk>/` (PUT, DELETE)

### Application Management
- **Apply for Job**: `jobs/apply/` (POST)
  - **Request Body**:
    ```json
    {
      "job": 1  # Job ID
    }
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to open issues or pull requests on the [GitHub repository](https://github.com/yourusername/job-finder-app).
