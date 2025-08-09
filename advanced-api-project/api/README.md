## API Endpoints

| Method | Endpoint                   | Description              | Permissions         |
|--------|----------------------------|--------------------------|---------------------|
| GET    | /books/                     | List all books           | Public              |
| GET    | /books/<id>/                | Retrieve one book        | Public              |
| POST   | /books/create/              | Create a new book        | Authenticated users |
| PUT    | /books/<id>/update/         | Update a book            | Authenticated users |
| DELETE | /books/<id>/delete/         | Delete a book            | Admin only (optional)|

### Notes
- Uses Django REST Framework Generic Views for simplicity and efficiency.
- Nested serializer in `AuthorSerializer` returns all books for each author.
- Custom validation in `BookSerializer` ensures no future publication years.
