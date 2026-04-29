# Django E-commerce Store

A fully functional online shopping store built with Django.

## 🚀 Project Overview

**Built by:** Sameer  
**Internship:** CodeAlpha  
**Tech Stack:** Python, Django, HTML, CSS, Bootstrap, SQLite

## Features

- 🛒 **Shopping Cart** — Add/remove items, update quantities
- 👤 **User Authentication** — Register, Login, Logout
- 📦 **Product Catalog** — Browse products by category
- 💳 **Checkout System** — Place orders with shipping details
- 📋 **Order History** — Track past orders
- 🔍 **Product Search** — Filter by category

## Project Structure

```
ecommerce_django/
├── accounts/          # User authentication
├── cart/             # Shopping cart & items
├── orders/           # Order processing
├── store/            # Products & categories
├── templates/        # HTML templates
├── static/           # CSS & JS files
├── ecommerce/        # Django project settings
└── db.sqlite3        # Database
```

## Setup Instructions

```bash
# Clone the repository
git clone https://github.com/yourusername/CodeAlpha_Ecommerce.git
cd CodeAlpha_Ecommerce

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install django crispy-forms crispy-bootstrap4

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

Visit: `http://127.0.0.1:8000`

## Screenshots

> Add your screenshots here

## What I Learned

- Django models, views, and templates
- User authentication system
- Shopping cart logic
- Order processing & management
- Bootstrap for responsive design

## Future Improvements

- Payment gateway integration
- Email notifications
- Admin dashboard
- Product reviews & ratings

---

**Connect with me:**  
LinkedIn: [Your LinkedIn URL]  
GitHub: [Your GitHub URL]

#Django #Python #WebDevelopment #Ecommerce #CodeAlpha #Internship