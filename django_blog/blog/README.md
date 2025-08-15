#### Views

UserLoginView / UserLogoutView: built-in Django auth views with custom templates.
register: uses RegistrationForm (extends UserCreationForm to add email, names).
profile (login required): updates User and Profile models; handles POST and file uploads.

#### Forms

RegistrationForm: validates unique email and captures first/last name.
UserUpdateForm, ProfileForm: for profile page edits (bio, optional avatar).

#### Models

Profile: OneToOne with User plus bio and avatar. Auto-created via signals on user creation.

#### URLs

/login, /logout, /register, /profile, and / (home).

#### Security

CSRF tokens in all POST forms.
Passwords hashed by Django.
Profile protected by login_required.

#### How to run
```python
pip install django Pillow
python manage.py migrate
python manage.py runserver
```

Visit /register to create your first user.