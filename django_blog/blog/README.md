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
/posts/ list, /posts/new/ create, /posts/<pk>/ detail,
/posts/<pk>/edit/ update, /posts/<pk>/delete/ delete.

#### Security

CSRF tokens in all POST forms.
Passwords hashed by Django.
Profile protected by login_required.

#### Permissions

Create: logged-in only.
Edit/Delete: author only.

#### Forms

PostForm uses title, content; author is auto set in form_valid.

#### How to run
```python
pip install django Pillow
python manage.py migrate
python manage.py runserver
```

Visit /register to create your first user.