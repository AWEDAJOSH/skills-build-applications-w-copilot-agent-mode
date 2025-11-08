# Octofit Tracker

## Overview
The Octofit Tracker is a fitness application designed to help users log and track their activities, manage teams, and receive personalized workout suggestions. The application includes user authentication, activity logging, a competitive leaderboard, and more.

## Project Structure
The project is organized as follows:

```
octofit-tracker/
├── backend/
│   ├── venv/                     # Python virtual environment
│   ├── octofit_tracker/          # Django project directory
│   │   ├── manage.py             # Command-line utility for the Django project
│   │   ├── octofit_tracker/      # Main application package
│   │   │   ├── __init__.py       # Indicates the directory is a Python package
│   │   │   ├── asgi.py           # ASGI configuration for handling asynchronous requests
│   │   │   ├── settings.py       # Project settings and configuration
│   │   │   ├── urls.py           # URL routing for the application
│   │   │   └── wsgi.py           # WSGI configuration for serving HTTP requests
│   └── requirements.txt           # List of required Python packages
└── README.md                      # Documentation for the project
```

## Setup Instructions

1. **Create a Python Virtual Environment**
   Navigate to the `backend` directory and create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

2. **Activate the Virtual Environment**
   Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

3. **Install Required Packages**
   Install the necessary Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   Apply the initial migrations:
   ```bash
   python octofit_tracker/manage.py migrate
   ```

5. **Run the Development Server**
   Start the Django development server:
   ```bash
   python octofit_tracker/manage.py runserver
   ```

## Usage
Once the server is running, you can access the application at `http://127.0.0.1:8000/`. Follow the on-screen instructions to create an account, log activities, and manage your fitness journey.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.