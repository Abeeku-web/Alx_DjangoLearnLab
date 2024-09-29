# Social Media API

## Setup Instructions

1. Clone the repository: git clone https://github.com/your-username/Alx_DjangoLearnLab.git

2. Install dependencies:pip install -r requirements.txt

3. Apply migrations: python manage.py migrate

4. Create a superuser for admin: python manage.py createsuperuser

5. Run the server: python manage.py runserver

## API Endpoints

### Register a new user
`POST /api/accounts/register/`

### Login
`POST /api/accounts/login/`

### Profile
`GET /api/accounts/profile/`