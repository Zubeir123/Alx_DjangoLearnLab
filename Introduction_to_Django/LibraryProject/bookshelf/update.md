```python
book = Book.objects.get(title="1984")
book.publication_year = 1950
book.save()
print(book.publication_year)
# Expected Output: 1950
```