# DjangoBlog

A Django-based blogging platform for creating, managing, and sharing blog posts through a simple and user-friendly interface.

## Project Overview

DjangoBlog is a web-based blogging application developed using Python and the Django framework. The application provides a platform for managing and displaying blog content through a structured and user-friendly interface.

This project was developed as an academic project to gain practical experience in Python web development, Django, database management, and version control using Git and GitHub.

## Features

* Create and manage blog posts
* Display blog posts through a user-friendly interface
* Support for blog images and media files
* Django-based backend
* SQLite database for development
* Organized Django project and application structure
* Web-based interface for accessing blog content

## Technologies Used

* Python
* Django
* HTML
* CSS
* SQLite
* Git
* GitHub

## Project Structure

```text
DjangoBlog/
│
├── blog/                 # Main blog application
├── config/               # Django project configuration
├── blog_images/          # Blog-related images
├── media/                # Uploaded media files
├── manage.py             # Django management script
├── .gitignore            # Files excluded from version control
└── README.md             # Project documentation
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/shambhavis-24/DjangoBlog.git
```

### 2. Navigate to the Project Directory

```bash
cd DjangoBlog
```

### 3. Create a Virtual Environment

```bash
python3 -m venv .venv
```

### 4. Activate the Virtual Environment

For macOS and Linux:

```bash
source .venv/bin/activate
```

For Windows:

```bash
.venv\Scripts\activate
```

### 5. Install Django

```bash
pip install django
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

Open the following address in a web browser:

```text
http://127.0.0.1:8000/
```

## Learning Objectives

This project provides practical experience with:

* Django project and application structure
* URL routing and views
* Django templates
* Static and media file management
* Database integration
* CRUD operations
* Python-based web development
* Git version control
* GitHub repository management

## Future Enhancements

The application can be further enhanced with:

* User authentication and registration
* User comments and interactions
* Search functionality
* Categories and tags
* Improved responsive design
* Additional content management features
* Deployment to a production environment

## Author

**Shambhavi Singh**

Academic web development project developed using Python and Django.
