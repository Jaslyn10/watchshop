# 🕒 WatchShop – Django Web App Demo

🔗 **Live Demo**: [https://watchshop-p34z.onrender.com](https://watchshop-p34z.onrender.com)

---

## About the Project

This is a **Django-based web application** created to showcase my skills in backend development, database modeling, and deployment of dynamic websites using the Django framework.

It simulates a **watch listing and shopping platform** where users can view watches, add them to a cart or wishlist, and also upload their own watches for sale.

⚠️**NOTE**: This project is deployed with `DEBUG = True` for demonstration purposes only. Do not use this as-is for production. See below for production tips.
        **: The website is hosted on **Render using the free plan**. 
        If the app has been inactive for a while, it might take 30–60 seconds to load initially as the server spins back up. Please be patient — the site will load shortly!
---

## Features

- **Home Page**: Displays all watches available on the platform.
- **User Authentication**: 
  - Register / Login to access features like **Add to Wishlist** or **Add to Cart**.
- **Cart and Wishlist**: 
  - Logged-in users can add/remove watches to/from their cart and wishlist.
- **Upload Watch**: 
  - Visitors can upload a watch image and details even without logging in.
- **Image Handling**: 
  - Media uploads handled via Django’s media configuration (Cloudinary optional for production).

---

## Technologies Used

- Django 5.x
- SQLite (for local development)
- Cloudinary (optional for media file hosting)
- Render (for deployment)

---

## Run Locally

To clone and run this project on your local machine:

### 1. Clone the repository:
```bash
git clone https://github.com/Jaslyn10/watchshop.git
cd watchshop        #Navigate to the project folder containing manage.py file
python -m venv env  #Create a virtual environment
# Activate the virtual environment:
# On Windows:
env\Scripts\activate
# On Mac/Linux:
source env/bin/activate
#download the required libraries, dependencies etc using the below command
pip install -r requirements.txt
#To run migrations and start the server use the below commands
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
