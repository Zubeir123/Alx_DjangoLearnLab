
# Social Media API

## Setup
pip install django djangorestframework djangorestframework-simplejwt Pillow
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

## Endpoints
- POST /api/accounts/register/
- POST /api/accounts/login/
- GET /api/accounts/profile/


# Posts and Comments API

## Endpoints
### Posts
- GET /api/posts/
- POST /api/posts/ (auth required)
- GET /api/posts/{id}/
- PUT /api/posts/{id}/ (author only)
- DELETE /api/posts/{id}/ (author only)

### Comments
- GET /api/comments/
- POST /api/comments/ (auth required)
- GET /api/comments/{id}/
- PUT /api/comments/{id}/ (author only)
- DELETE /api/comments/{id}/ (author only)

## Features
- Pagination (default: 5 posts per page)
- Search posts by `title` or `content` via `?search=keyword`

# Follow & Feed API Documentation

## 1. Follow a User

* Endpoint: POST /api/accounts/follow/<user_id>/
* Authentication: Required (Token or JWT)
* Description: Follow another user by their ID.

* Request Example:
```json
{
  "Authorization": "Token <your_token>"
}
```

* Response Example:
```json
{
  "message": "You are now following john_doe"
}
```

## 2. Unfollow a User

* Endpoint: POST /api/accounts/unfollow/<user_id>/
* Authentication: Required
* Description: Unfollow a user by their ID.

* Request Example:
```json
{
  "Authorization": "Token <your_token>"
}
```

## Response Example:
```json
{
  "message": "You have unfollowed john_doe"
}
```

## 3. Get Feed

* Endpoint: GET /api/posts/feed/
* Authentication: Required
* Description: Retrieve posts from users that the current user follows, ordered by newest first.

* Request Example:
```json
{
  "Authorization": "Token <your_token>"
}
```

* Response Example:
```json
[
  {
    "id": 5,
    "author": 2,
    "author_username": "john_doe",
    "title": "My First Post",
    "content": "Hello world!",
    "comments": [],
    "created_at": "2025-08-22T08:00:00Z",
    "updated_at": "2025-08-22T08:00:00Z"
  },
  {
    "id": 3,
    "author": 3,
    "author_username": "jane_smith",
    "title": "Summer Vacation",
    "content": "Photos from my trip!",
    "comments": [],
    "created_at": "2025-08-21T14:30:00Z",
    "updated_at": "2025-08-21T14:30:00Z"
  }
]
```
## Notes

* Users cannot follow/unfollow themselves.
* Feed shows posts only from users you follow.
* All endpoints require authentication.

# Likes and Notifications
## Like Post

```bash
POST /api/posts/<post_id>/like/
Authorization: Token <user_token>
Response: { "message": "Post liked." }
```

## Unlike Post

```bash
POST /api/posts/<post_id>/unlike/
Authorization: Token <user_token>
Response: { "message": "Post unliked." }
```

## Fetch Notifications

```pgsql
GET /api/notifications/
Authorization: Token <user_token>
Response: [
  {
    "id": 1,
    "actor_username": "john",
    "verb": "liked",
    "target_repr": "My First Post",
    "timestamp": "2025-08-22T08:00:00Z",
    "is_read": false
  }
]
```

# Deployment (Production)

## Environment
* DJANGO_SETTINGS_MODULE=social_media_api.settings_prod
* DJANGO_SECRET_KEY=***
* ALLOWED_HOSTS=api.example.com
* CSRF_TRUSTED_ORIGINS=https://api.example.com
* DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/DB
* SECURE_SSL_REDIRECT=true
* (Optional S3)
  - AWS_ACCESS_KEY_ID=***
  - AWS_SECRET_ACCESS_KEY=***
  - AWS_STORAGE_BUCKET_NAME=***
  - AWS_S3_REGION_NAME=***

## One-time setup
pip install -r requirements.txt
python manage.py collectstatic --noinput --settings=social_media_api.settings_prod
python manage.py migrate --settings=social_media_api.settings_prod
python manage.py createsuperuser --settings=social_media_api.settings_prod

```shell
### Start (Gunicorn)
```
gunicorn social_media_api.wsgi:application --workers 3 --timeout 60

```bash
### Health check
- `GET /health/` → `{ "status": "ok" }`
```