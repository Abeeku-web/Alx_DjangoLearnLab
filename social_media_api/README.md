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

## Social Media API - Follow and Feed Features

### Endpoints:

#### Follow Users:
- **Follow a User**: `POST /api/follow/<user_id>/` (Requires Authentication)
  - Follows the specified user.
  - Example Response: `{ "message": "You are now following <username>" }`

- **Unfollow a User**: `POST /api/unfollow/<user_id>/` (Requires Authentication)
  - Unfollows the specified user.
  - Example Response: `{ "message": "You have unfollowed <username>" }`

#### Feed:
- **Get Feed**: `GET /api/feed/` (Requires Authentication)
  - Returns a list of posts created by users that the current user follows.
  - The feed is ordered by creation date, with the most recent posts at the top.
  - Example Response:
    ```json
    [
      {
        "id": 1,
        "author": "user1",
        "title": "First Post",
        "content": "This is my first post!",
        "created_at": "2024-09-30T12:00:00Z",
        "updated_at": "2024-09-30T12:00:00Z"
      },
      ...
    ]
    ```

### Testing:
- Ensure that users can follow and unfollow others.
- Ensure that the feed correctly shows posts from followed users.