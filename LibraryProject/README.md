### ✅ Django Models Overview

In Django, models are Python classes that represent tables in a database. 
Each model maps to a single database table, and each attribute of the model 
represents a database field (column).

### 📦 Basic Concepts

Each model is a class that inherits from django.db.models.Model.
Fields are defined using Django field types like CharField, IntegerField, DateField, etc.
Django provides an Object-Relational Mapping (ORM) to interact with the database 
using Python code instead of SQL.

### ⚙️ Common Field Types
```
Field Type	 ----------->  Description
CharField	 ----------->  Short text
TextField	 ----------->  Long text
IntegerField ----------->  Whole numbers
DecimalField ----------->  Fixed-point decimals
FloatField	 ----------->  Floating-point numbers
DateField	 ----------->  Date (YYYY-MM-DD)
DateTimeField----------->  Date and time
BooleanField ----------->  True/False
ForeignKey	 ----------->  One-to-many relationship
ManyToMany   ----------->  Many-to-many relationship
Field	   
```

### ⃣ 🔍 Querying with Django ORM

🔸 Create and save data
```python
p = Product(name="Laptop", price=1200)
p.save()
```

🔸 Fetch all products
```python
products = Product.objects.all()
```

🔸 Filter products
```python
cheap = Product.objects.filter(price__lt=100)
```

🔸 Get one object
```python
p = Product.objects.get(id=1)
```

🔸 Updating Object Properties
```python
p.name = "Iphone"
p.price = 1025
p.save()
```

🔸 Bulk Update (many objects at once)
```python
p.objects.filter(name="laptop").update(name="computer")
```

🔸 Delete a Single Object
```python
p.delete()
```

🔸 Delete Multiple Objects (Bulk Delete)
```python
p.objects.filter(name="phone").delete()
```

🔸 Delete All Objects
```python
p.objects.all().delete()
```

🔸 Order results
```python
Product.objects.order_by('-price')  # Descending
```

### ⃣ 📝 Using Models with Forms

#### Create a ModelForm

```python
# forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']
```

#### Use it in a view

```python
# views.py
from django.shortcuts import render, redirect
from .forms import ProductForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
```

#### Template Example

```html
<!-- add_product.html -->
<h2>Add Product</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
</form>
```