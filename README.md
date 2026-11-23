# LearnHub – Learning Management System

LearnHub is a REST API-based Learning Management System (LMS) developed using Python, Django, and Django REST Framework. It allows authenticated users to manage course categories, create and manage courses, and enroll in courses.

The project uses JWT authentication to secure API endpoints and provides user-based access control.

## Features

- JWT-based user authentication.
- Create, view, update, and delete course categories.
- Create, view, update, and delete courses.
- Enroll in courses.
- View all personal enrollments.
- View individual enrollment details.
- Cancel course enrollments.
- Prevent duplicate enrollments.
- User-based access control.

## Technologies Used

- Python
- Django 6.1.3
- Django REST Framework 3.18.3
- Django REST Framework Simple JWT 5.5.1
- SQLite
- Git and GitHub

## API Endpoints

### 1. Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/jwt_login/` | User login and token generation |
| POST | `/api/refresh/` | Generate a new access token |

### 2. Category Management

| Method | Endpoint | Description |
|---|---|---|
| GET | `/category/` | View all your categories |
| POST | `/category/` | Create a category |
| GET | `/category/<category_id>/` | View a specific category |
| PUT | `/category/<category_id>/` | Update a category |
| PATCH | `/category/<category_id>/` | Partially update a category |
| DELETE | `/category/<category_id>/` | Delete a category |

### 3. Course Management

| Method | Endpoint | Description |
|---|---|---|
| GET | `/course/` | View courses |
| POST | `/course/` | Create a course |
| GET | `/course/<course_id>/` | View a specific course |
| PUT | `/course/<course_id>/` | Update a course |
| DELETE | `/course/<course_id>/` | Delete a course |

### 4. Enrollment Management

| Method | Endpoint | Description |
|---|---|---|
| POST | `/enrollment/` | Enroll in a course |
| GET | `/enrollment/` | View all your enrollments |
| GET | `/enrollment/<enrollment_id>/` | View a specific enrollment |
| DELETE | `/enrollment/<enrollment_id>/` | Cancel an enrollment |

## Authentication

LearnHub uses JSON Web Token (JWT) authentication through Django REST Framework Simple JWT.

After logging in, the user receives an access token and a refresh token.

For accessing protected API endpoints, include the access token in the request header:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/LearnHub-LMS.git
```

### 2. Navigate to the Project Directory

```bash
cd Learning_Management_System
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at:

`http://127.0.0.1:8000/`

## Dependencies

The project uses the following Python packages:

| Package | Version |
|---|---|
| asgiref | 3.13.0 |
| Django | 6.1.3 |
| djangorestframework | 3.18.3 |
| djangorestframework_simplejwt | 5.5.1 |
| PyJWT | 2.15.1 |
| sqlparse | 0.6.1 |
| tzdata | 2026.6 |

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## Learning Outcomes

Through this project, I gained practical experience in:

- Developing REST APIs using Django REST Framework.
- Implementing CRUD operations using APIView.
- Working with Django models and database relationships.
- Using serializers for data validation and serialization.
- Implementing JWT authentication.
- Managing user-specific data and access control.
- Performing database operations using Django ORM.

## Author

**Dheeraj Divakaran**

GitHub: https://github.com/dheerajdivakaran
