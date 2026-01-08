<!-- Please update value in the {}  -->

 <p align="center">
  <img src="https://img.shields.io/badge/Django-5.x-092E20?logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Full--Stack-Django-success"/>
  <img src="https://img.shields.io/badge/Authentication-Session--Based-blue"/>
  <img src="https://img.shields.io/badge/Bootstrap-5-7952B3?logo=bootstrap&logoColor=white"/>
  <img src="https://img.shields.io/badge/Deployment-PythonAnywhere-purple"/>
</p>

<h1 align="center">🍕 Django Pizza Ordering App</h1>

<p align="center">
A full-stack pizza ordering application built with Django Templates, featuring authentication and order management.
</p>


<div align="center">
  <h3>
    <a href="https://umit8111.pythonanywhere.com/">
      🖥️ Live Demo
    </a>
      | 
    <a href="https://github.com/Umit8098/Project_Django_Templates_Pizza_App_CH-12_V.03.git">
      📂 Repository
    </a>

  </h3>
</div>

![Pizza Order](./project_screenshot/pizza_app_order.gif)

## Navigation

- [Overview](#overview)
  - [User Registration](#user-registration)
  - [User Login](#user-login)
  - [Ordering Pizza](#ordering-pizza)
- [Built With](#built-with)
- [How To Use](#how-to-use)
  - [Test User Information](#test-user-information)
- [About This Project](#about-this-project)
- [Key Features](#key-features)
- [Contact](#contact)

<!-- OVERVIEW -->

## Overview

### User Registration
<!-- ![screenshot](project_screenshot/pizza_app_register.gif) -->
<img src="project_screenshot/pizza_app_register.gif" alt="Kullanıcı Kayıt Olma" width="400"/>

➡ User registration page for the application.

---

### User Login
<!-- ![screenshot](project_screenshot/pizza_app_login.gif) -->
<img src="project_screenshot/pizza_app_login.gif" alt="Kullanıcı Login" width="400"/>

➡ The screen where users log in and order pizza.

---

### Ordering Pizza
<!-- ![screenshot](project_screenshot/pizza_app_order.gif) -->
<img src="project_screenshot/pizza_app_order.gif" alt="Pizza App Order" width="400"/>

➡ Screen where users order pizza by selecting size and toppings.



## Built With

<!-- This section should list any major frameworks that you built your project using. Here are a few examples.-->
This project was developed using the following tools and libraries:

- [Django Templates](https://docs.djangoproject.com/en/5.1/topics/templates/): For creating dynamic web pages.
- [Bootstrap5](https://getbootstrap.com/docs/5.0/getting-started/introduction/): To provide a responsive and modern user interface.
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/): To easily style forms.
- Django Authentication (Session-based)



## How To Use

<!-- This is an example, please update according to your application -->

To clone and run this application, you'll need [Git](https://github.com/Umit8098/Project_Django_Templates_Pizza_App_CH-12_V.03)

When installing the required packages in the requirements.txt file, review the package differences for windows/macOS/Linux environments. 

Complete the installation by uncommenting the appropriate package.


```bash
# Clone this repository
$ git clone https://github.com/Umit8098/Project_Django_Templates_Pizza_App_CH-12_V.03.git

# Install dependencies
    $ python -m venv env
    $ python3 -m venv env (for macOs/linux OS)
    $ env/Scripts/activate (for win OS)
    $ source env/bin/activate (for macOs/linux OS)
    $ pip install -r requirements.txt
    $ python manage.py migrate (for win OS)
    $ python3 manage.py migrate (for macOs/linux OS)

# Create and Edit .env
# Add Your SECRET_KEY in .env file

"""
# example .env;

SECRET_KEY =123456789abcdefg...
"""

# Run the app
    $ python manage.py runserver
```

### Test User Information
For the live demo, you can use the following test user information:
- **Username**: testuser
- **Password**: testpassword123
- **email**: testuser@gmail.com
This user can only place orders and update their profile.


## About This Project

This project allows users to order pizzas online through a simple and user-friendly interface.  
It is built as a full-stack Django Template application and includes user authentication and order management features.

Users can:
- Register and log in securely
- Order pizzas with different sizes and toppings
- View and manage their orders
- Update profile information and change passwords



## Key Features

- **Pizza Order Management**: Users can order pizzas with various sizes and toppings.
- **User Management**: Registration, login, profile editing and password change operations.
- **Order Tracking**: Users can view and manage their orders.
- **User Notifications**: After successful transactions, the user is given feedback via an on-screen message.


## Contact

<!-- - Website [your-website.com](https://{your-web-site-link}) -->
- **GitHub** [@Umit8098](https://github.com/Umit8098)

- **LinkedIn** [@umit-arat](https://linkedin.com/in/umit-arat/)
<!-- - Twitter [@your-twitter](https://{twitter.com/your-username}) -->

