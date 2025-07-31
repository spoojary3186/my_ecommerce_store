🛒 My E-Commerce Store

A basic full-stack **E-Commerce web application** built using the **Django framework (Python)**. It supports core functionalities such as user authentication, product listings, cart management, checkout, and order history — with simple HTML templates and no external CSS or JavaScript.

This project is ideal for learning how to structure and build backend-driven applications using Django.


📌 Features

- 🧑‍💼 **User Authentication**
  - Signup & Login
  - Secure session-based login system

- 🛍️ **Storefront**
  - Product listing page
  - Shopping cart (add/view/remove items)

- ✅ **Checkout**
  - Order confirmation page
  - Checkout success screen

- 📦 **Order Management**
  - Order history with user-specific tracking



🔧 Tech Stack

| Layer        | Technology       |
|--------------|------------------|
| Backend      | Python 3.x, Django |
| Frontend     | HTML (No CSS/JS) |
| Database     | SQLite (default Django DB) |
| Dependencies | Listed in `requirements.txt` |



📁 Project Structure
my_ecommerce_store/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── ecommerce_app/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── templates/
│ ├── cart.html
│ ├── checkout.html
│ ├── checkout_success.html
│ ├── login.html
│ ├── order_history.html
│ ├── product_list.html
│ └── signup.html




⚙️ Getting Started

1. Clone the Repository
   git clone https://github.com/spoojary3186/my_ecommerce_store.git
   cd my_ecommerce_store

2. Create Virtual Environment (optional but recommended)
   python -m venv env
   source env/bin/activate        # Linux/macOS
   env\Scripts\activate           # Windows

3. Install Dependencies
   pip install -r requirements.txt

4. Run Database Migrations
   python manage.py migrate

5. Start the Development Server

6. Visit in Browser
   http://127.0.0.1:8000/

🔑 Admin Panel

1. Create a superuser:
   python manage.py createsuperuser

2. Access the admin panel at:
   http://127.0.0.1:8000/admin/

📈 Future Improvements
Add frontend styling using CSS frameworks like Bootstrap or Tailwind
JavaScript-based dynamic cart updates
Payment gateway integration (e.g., Razorpay or Stripe)
Add product filtering, categories, and search
Responsive mobile layout

🙌 Acknowledgements
This project was developed as a hands-on practice to explore Django's core features while building a simplified e-commerce system.

📬 Contact
If you’d like to collaborate or have any suggestions, feel free to open an issue or contact me.

🗃️ License
This project is open-source and free to use under the MIT License.



