# AutoHub

Welcome to **AutoHub**, the comprehensive car marketplace platform. This repository, **automarket**, contains the full-stack codebase for the AutoHub application, which is built using Django REST framework for the backend and Vue.js 3 for the frontend.

## Internationalization (i18n)

AutoHub supports internationalization (i18n), allowing users to select their preferred language for the best user experience. This feature is implemented in the Vue.js frontend using the `i18n` plugin, which provides a seamless way to handle translations and locale changes.

### Changing Languages

Users can easily switch languages using the Language Switcher component in the navigation bar. The application currently supports the following languages:

- English
- Georgian (ქართული)

We are constantly working to expand the range of languages supported by AutoHub to cater to our global user base.

## Project Structure

The AutoHub project is structured as follows:

auto-market/ ├── LICENSE - The project license ├── README - The README file ├── automarket_backend/ - Django REST framework backend │ ├── account/ - User account management │ │ ├── models.py - Database models │ │ ├── serializers.py - Data serializers │ │ ├── views.py - View functions │ │ └── … │ ├── automarket_backend/ - Main backend directory │ │ ├── settings.py - Configuration settings │ │ ├── urls.py - URL declarations │ │ └── … │ ├── cars/ - Car management module │ │ ├── models.py - Car database models │ │ ├── serializers.py - Car data serializers │ │ └── … │ ├── filters/ - Search and filtering functionality │ │ └── … │ ├── manage.py - Django command-line utility │ └── vin/ - VIN decoding module │ └── … ├── automarket_frontend/ - Vue.js 3 frontend │ ├── src/ - Source files │ │ ├── App.vue - Main app component │ │ ├── components/ - Reusable components │ │ ├── views/ - Vue views │ │ └── … │ ├── package.json - Frontend dependencies │ └── … └── requirements.txt - Backend dependencies list

This structure provides a high-level overview of your project, making it easier for others to navigate and understand the purpose of each directory and file.

## Backend Dependencies

The backend of AutoHub is powered by Django and Django REST framework. Here is a list of the key dependencies:

For a complete list, see `requirements.txt`.

## Features

AutoHub allows users to:

- Create an account and log in.
- Add and search for cars.
- Use advanced filtering options to find the perfect car.
- Manage their profile, including changing passwords, emails, names, and phone numbers.

## VIN Decode Feature

AutoHub includes a VIN (Vehicle Identification Number) decode feature that allows users to retrieve detailed information about a vehicle by entering its unique VIN. This feature enhances the user experience by providing valuable insights into the car's specifications, history, and authenticity.

### How It Works

- Users can enter a car's VIN into the designated search field.
- The system decodes the VIN and displays a comprehensive report about the vehicle.
- This report includes information such as the make, model, year, engine type, and more.

### API Endpoint for VIN Decode

- `api/vin/` - Decode VIN (GET)

By utilizing this feature, users can make informed decisions when searching for cars on AutoHub.

## Frontend Interaction with Backend

The frontend interacts with the backend through various API endpoints, utilizing Axios for HTTP requests. Here are some of the key API endpoints:


## API Endpoints

Below are the API endpoints available in AutoHub:

### Authentication
- `api/login/` - Obtain token (POST)
- `api/refresh/` - Refresh token (POST)
- `api/signup/` - User registration (POST)
- `api/user/` - User details (GET)
- `api/editprofile/` - Edit user profile (PUT)
- `api/changepassword/` - Change password (PUT)
- `api/forgot/` - Forgot password (POST)
- `api/reset/` - Reset password (POST)

### Car Management
- `api/create/` - Create car listing (POST)
- `api/<uuid:pk>/` - Car details (GET)
- `api/similar/<str:manufacturer>/<uuid:pk>/` - Similar cars (GET)
- `api/recently/` - Recently added cars (GET)
- `api/profile/cars/<uuid:id>/` - User's cars (GET)
- `api/delete/<uuid:id>/` - Delete car (DELETE)

### Search & Filtering
- `api/choices/` - Get choices for car filters (GET)
- `api/filters/` - Filtered search (GET)


## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 12+

### Installation

1. Clone the repository:

```bash
git clone https://github.com/vaanskii/auto-market
```

### Backend

2. Create a virtual environment:
```bash
python3 -m venv virtual-env-name
```
3. Activate the virtual environment:
- On Windows:
  ```
  env\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source env/bin/activate
  ```

4. Install backend dependencies:
```
pip install -r requirements.txt
```

5. Navigate into the project directory:
```bash
cd automarket_backend
```

6. Change settings copy.py name to settings.py


7. Apply migrations:
```
python manage.py migrate
```

8. Run the development server:
```
python manage.py runserver
```

9. Access the application in your web browser at http://127.0.0.1:8000/

### Frontend

1. Navigate into the project directory:
```bash
cd automarket_frontend
```

2. Install frontend dependencies:
```
npm install
```

3. In a new terminal, start the Vue.js frontend:

```
npm run serve
```

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
