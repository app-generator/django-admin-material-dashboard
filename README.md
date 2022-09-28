# Django Admin Material Dashboard

Modern template for **Django Admin Interface** coded on top of **[Material Dashboard](https://www.creative-tim.com/product/material-dashboard?AFFILIATE=128200)** (free version). 

> UI Kit: [Material Dashboard](https://github.com/creativetimofficial/material-dashboard) **v3.0.4**

<br>

## Why Django Material Dashboard?

- Bootstrap 5 Design (Free version) provided by **Creative-Tim**
- New fresh look
- Responsive mobile interface
- Useful admin home page
- Minimal template overriding
- Easy integration

<br>

## How to use it

<br />

> **Install the package** via `PIP` 

```bash
$ pip install django-admin-material-dashboard
// OR
$ pip install git+https://github.com/app-generator/django-admin-material-dashboard.git
```

<br />

> Add `admin_soft` application to the `INSTALLED_APPS` setting of your Django project `settings.py` file (note it should be before `django.contrib.admin`):

```python
    INSTALLED_APPS = (
        ...
        'admin_material.apps.AdminMaterialDashConfig',
        'django.contrib.admin',
    )
```

<br />

> **Collect static** if you are in `production environment`:

```bash
$ python manage.py collectstatic
```

<br />

> **Start the app**

```bash
$ # Set up the database
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Create the superuser
$ python manage.py createsuperuser
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
```

Access the `admin` section in the browser: `http://127.0.0.1:8000/`

<br />

## Screenshots

@Todo

---
**Django Admin Material Dashboard** - Open-source Admin THEME provided by **[AppSeed](https://appseed.us/)**
