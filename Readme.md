<!-- Please update value in the {}  -->

<h1 align="center">Project_Django_Template_Pizza_Ordering_App</h1>

<p align="center">🍕 Django ile geliştirilmiş hem backend hem de frontend içeren pizza sipariş uygulaması 🍕</p>

<div align="center">
  <h3>
    <a href="https://umit8111.pythonanywhere.com/">
      Canlı Demo
    </a> 
  </h3>
</div>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
  - [Kullanıcı Kayıt Olma](#kullanıcı-kayıt-olma)
  - [Kullanıcı Login](#kullanıcı-login)
  - [Pizza Siparişi Verme](#pizza-siparişi-verme)
  - [Kullanıcı Password Change](#kullanıcı-password-change)
- [Built With](#built-with)
- [How To Use](#how-to-use)
  - [Test Kullanıcı Bilgileri](#test-kullanıcı-bilgileri)
- [About This Project](#about-this-project)
- [Key Features](#key-features)
- [Contact](#contact)

<!-- OVERVIEW -->

## Overview

### Kullanıcı Kayıt Olma
<!-- ![screenshot](project_screenshot/pizza_app_register.gif) -->
<img src="project_screenshot/pizza_app_register.gif" alt="Kullanıcı Kayıt Olma" width="400"/>
➡ Kullanıcıların uygulamaya kayıt olma sayfası.


---

### Kullanıcı Login
<!-- ![screenshot](project_screenshot/pizza_app_login.gif) -->
<img src="project_screenshot/pizza_app_login.gif" alt="Kullanıcı Login" width="400"/>
➡ Kullanıcıların giriş yaparak blog gönderilerine erişim sağlayabileceği ekran.

---

### Pizza Siparişi Verme
<!-- ![screenshot](project_screenshot/pizza_app_order.gif) -->
<img src="project_screenshot/pizza_app_order.gif" alt="Pizza App Order" width="400"/>
➡ Kullanıcıların boyut ve malzemeler seçerek pizza siparişi verdiği ekran.

---

### Kullanıcı Password Change
<!-- ![screenshot](project_screenshot/password_change.png) -->
<img src="project_screenshot/password_change.png" alt="Kullanıcı Password Change" width="400"/>
➡ Kullanıcıların hesap şifresini değiştirme ekranı.

---

## Built With

<!-- This section should list any major frameworks that you built your project using. Here are a few examples.-->
Bu proje aşağıdaki araçlar ve kütüphaneler kullanılarak geliştirilmiştir:

- [Django Templates](https://docs.djangoproject.com/en/5.1/topics/templates/): Dinamik web sayfaları oluşturmak için.
- [Bootstrap5](https://getbootstrap.com/docs/5.0/getting-started/introduction/): Duyarlı ve modern bir kullanıcı arayüzü sağlamak için.
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/): Formları kolayca stilize etmek için.
- [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/): Kullanıcı doğrulama ve yetkilendirme modülü.


## How To Use

<!-- This is an example, please update according to your application -->

To clone and run this application, you'll need [Git](https://github.com/Umit8098/Project_Django_Templates_Pizza_App_CH-12_V.03)

When installing the required packages in the requirements.txt file, review the package differences for windows/macOS/Linux environments. 

Complete the installation by uncommenting the appropriate package.

---

requirements.txt dosyasındaki gerekli paketlerin kurulumu esnasında windows/macOS/Linux ortamları için paket farklılıklarını inceleyin. 

Uygun olan paketi yorumdan kurtararak kurulumu gerçekleştirin.

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

### Test Kullanıcı Bilgileri

Canlı demo için aşağıdaki test kullanıcı bilgilerini kullanabilirsiniz:
- **Kullanıcı Adı**: testuser
- **Şifre**: testpassword123
- **e-mail**: testuser@gmail.com
Bu kullanıcı sadece sipariş verme ve profil güncelleme işlemlerini gerçekleştirebilir.


## About This Project
This project is used to enable users to place pizza orders online. Users:
- Pizzas can be ordered in various sizes and options.
- Can track and manage their orders.
- User can perform account operations (registration, login, change password).
- It offers both front-end and back-end support with Django Template.

<hr>

Bu proje, kullanıcıların online pizza siparişi vermesini kolaylaştırmak amacıyla geliştirilmiştir. Kullanıcılar:
- Çeşitli boyut ve malzemelerle pizza siparişi verebilir.
- Siparişlerini takip edebilir ve yönetebilir.
- Kullanıcı hesap işlemleri yapabilir (kayıt, giriş, şifre değiştirme).
- Django Template ile hem frontend hem de backend desteği sunmaktadır.



## Key Features

- **Pizza Siparişi Yönetimi**: Kullanıcılar çeşitli boyut ve malzemelerle pizza siparişi verebilir.
- **Kullanıcı Yönetimi**: Kayıt, giriş, profil düzenleme ve şifre değiştirme işlemleri.
- **Sipariş Takibi**: Kullanıcılar verdikleri siparişleri görüntüleyebilir ve yönetebilir.
- **Kullanıcı Bildirimleri**: Başarılı işlemler sonrası kullanıcıya ekran mesajı ile geri bildirim sağlanır.


## Contact

<!-- - Website [your-website.com](https://{your-web-site-link}) -->
- **GitHub** [@Umit8098](https://github.com/Umit8098)

- **LinkedIn** [@umit-arat](https://linkedin.com/in/umit-arat/)
<!-- - Twitter [@your-twitter](https://{twitter.com/your-username}) -->

