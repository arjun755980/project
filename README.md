---

# **Matrimony Website**

A fully-featured matrimony website built with Django, designed to connect individuals seeking marriage partners. This project provides a seamless platform for users to create profiles and find potential matches.

---

## **Features**

- **User Registration & Login**: Secure user authentication system.
- **Profile Management**: Users can create and update their profiles with detailed information (e.g., name, age, gender, marital status, family details, etc.).
- **Admin Dashboard**: Manage user profiles, monitor activity, and moderate content.
- **Responsive Design**: Optimized for both desktop and mobile devices.

---

### **Prerequisites**

Before running the project, ensure the following are installed on your system:
- Python 3.12.2
- Django
- MySQL 8.0.37 for Win64 on x86_64
- pip (Python package manager)

### **Installation**

To set up the project locally:

```bash
# Clone the repository
git clone https://github.com/username/matrimony-website.git

# Navigate to the project directory
cd matrimony-website

# Create a virtual environment
python -m venv env

# Activate the virtual environment
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure the database
# Ensure MySQL is running and a database is created
# Update the database settings in settings.py (e.g., DB name, username, password)

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver
```

---

## **Usage**

1. Open the website in your browser: `http://127.0.0.1:8000`.
2. Register to create a profile or log in with existing credentials.
3. Search for matches based on your preferences.
4. View and interact with potential matches securely.

---

## **Project Structure**

- `users/`: Contains user management features (e.g., registration, profile).
- `templates/`: HTML templates for pages like home, profile, and search results.
- `static/`: Includes CSS, JavaScript, and images for the website's frontend.
- `settings.py`: Django project settings, including database configurations.

---

## **Database Configuration**

This project uses MySQL 8.0.37. Update the database connection in `settings.py` as follows:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

## **Contributing**

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

---
