# Django User Authentication API

## Overview

This project is a Django-based API that provides user authentication functionality using Django Rest Framework (DRF). It supports:

- **Custom user roles**: `admin`, `coach`, `agent`, `football player`
- **User registration**: Sign-up and social sign-up (Google, Facebook)
- **User login**: Traditional login and social login
- **Password management**: Password reset functionality

The project uses `django-allauth` and `dj-rest-auth` to handle authentication and integrates with social authentication providers like Google and Facebook.

## Features

- **Custom User Roles**: Each user has a specific role (`admin`, `coach`, `agent`, `football player`) assigned during registration.
- **Traditional User Registration**: Users can register with a username, email, password, and role.
- **Social Authentication**: Users can sign up or log in using Google or Facebook.
- **Password Reset**: Users can reset their password via email.

## Requirements

- Python 3.x
- Django 4.x
- Django Rest Framework
- django-allauth
- dj-rest-auth
- social-auth-app-django

You can install all dependencies listed in the `requirements.txt` file.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-repo/django-auth-api.git
    cd django-auth-api
    ```

2. **Install dependencies**:

    Create a virtual environment and install the required packages:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Set up the database**:

    Run the following commands to set up the database:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Create a superuser**:

    This will create an admin user to access the Django admin panel:

    ```bash
    python manage.py createsuperuser
    ```

5. **Run the server**:

    Start the development server:

    ```bash
    python manage.py runserver
    ```

6. **Configure Environment Variables**:

    You may need to configure environment variables for social authentication (Google and Facebook). Create a `.env` file if necessary and add:

    ```bash
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=your-google-client-id
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=your-google-client-secret
    SOCIAL_AUTH_FACEBOOK_KEY=your-facebook-app-id
    SOCIAL_AUTH_FACEBOOK_SECRET=your-facebook-app-secret
    ```

    Replace the `your-google-client-id`, `your-google-client-secret`, `your-facebook-app-id`, and `your-facebook-app-secret` with the actual credentials from your Google and Facebook developer consoles.

## API Endpoints

### 1. **User Registration**

- **Endpoint**: `/api/v1/auth/registration/`
- **Method**: `POST`
- **Payload**:
    ```json
    {
        "username": "john_doe",
        "email": "john@example.com",
        "password1": "your_password",
        "password2": "your_password",
        "role": "football_player"
    }
    ```

- **Response**:
    ```json
    {
        "key": "token"
    }
    ```

### 2. **User Login**

- **Endpoint**: `/api/v1/auth/login/`
- **Method**: `POST`
- **Payload**:
    ```json
    {
        "username": "john_doe",
        "password": "your_password"
    }
    ```

- **Response**:
    ```json
    {
        "key": "token"
    }
    ```

### 3. **Password Reset**

- **Endpoint**: `/api/v1/auth/password/reset/`
- **Method**: `POST`
- **Payload**:
    ```json
    {
        "email": "john@example.com"
    }
    ```

- This will send a password reset email to the user.

### 4. **Social Login (Google/Facebook)**

- **Google Login**:
    - **Endpoint**: `/api/v1/auth/registration/social/login/google/`
    - Use the OAuth flow to authenticate with Google.

- **Facebook Login**:
    - **Endpoint**: `/api/v1/auth/registration/social/login/facebook/`
    - Use the OAuth flow to authenticate with Facebook.

### 5. **User Information**

- **Endpoint**: `/api/v1/auth/user/`
- **Method**: `GET`
- **Response**:
    ```json
    {
        "id": 1,
        "username": "john_doe",
        "email": "john@example.com",
        "role": "football_player"
    }
    ```

## Custom User Roles

The app uses a custom user model with predefined roles. These roles are:

- `admin`: Full access to all functionalities.
- `coach`: Limited access to specific data.
- `agent`: Can manage football players.
- `football_player`: Standard user role for players.

### Changing User Roles

You can set a user's role during registration or update it through the Django admin panel.

## Admin Panel

To manage users and their roles, you can use the Django admin panel. Log in with the superuser credentials created earlier:

- **URL**: `/admin/`

## Social Authentication Setup

### Google

1. Go to the [Google Developer Console](https://console.developers.google.com/).
2. Create a new project and set up OAuth credentials.
3. Add the credentials to your `.env` file as shown above.

### Facebook

1. Go to the [Facebook for Developers](https://developers.facebook.com/).
2. Create a new app and set up OAuth credentials.
3. Add the credentials to your `.env` file as shown above.

## Running Tests

To run tests:

```bash
python manage.py test
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing

Feel free to submit issues and pull requests. Contributions are welcome!

## Contact

For any questions or issues, please reach out at [antenehh1031@gmail.com].