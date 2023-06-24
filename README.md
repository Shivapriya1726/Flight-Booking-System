# Flight-Booking-System
Flight Booking System Using Django as an backend

Welcome to the Flight Booking Web App repository! This web app allows users to search and book flights online. The current version of the app includes the basic functionality developed within a limited timeframe of 2 days. If time permits, there are plans to extend the UI and add additional features to enhance the overall user experience.

## Features
- User registration and login
- Flight search based on origin, destination, and date
- Flight selection and booking

## Prerequisites
Before getting started, ensure that you have the following prerequisites installed on your machine:
- Python (version 3.11)
- pip (Python package installer)

Sample pages:
![image](https://github.com/Shivapriya1726/Flight-Booking-System/assets/90460346/d9ece7fa-6e74-4734-8265-b6fe1e741d0d)
![image](https://github.com/Shivapriya1726/Flight-Booking-System/assets/90460346/f60e018c-8ebc-4517-9c46-955055d95d6b)

Demo:



https://github.com/Shivapriya1726/Flight-Booking-System/assets/90460346/fec9f1f4-cc60-4f93-a8bf-7d954b217793


## Setup Instructions
To set up the Flight Booking Web App locally, please follow these steps:

1. Clone the repository to your local machine using the following command:
2. Navigate to the project directory:cd flight-booking-web-app
3. Create a virtual environment to isolate the project's dependencies:
- For macOS and Linux:
  ```
  python3 -m venv env
  source env/bin/activate
  ```
- For Windows:
  ```
  python -m venv env
  env\Scripts\activate
  ```

4. Install the required dependencies by running the following command:
pip install -r requirements.txt


5. Set up the database:
- Configure the database settings in the `settings.py` file located in the `flightbooking` directory.
- Run the following command to apply database migrations:
  ```
  python manage.py migrate
  ```

6. Create a superuser account to access the Django admin interface:
python manage.py createsuperuser

7. Start the development server:
python manage.py runserver
8. Access the web app through your browser at `http://localhost:8000`.


