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
