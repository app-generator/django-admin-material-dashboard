# [Django Admin Material](https://github.com/app-generator/django-admin-material-dashboard)

Modern template for **Django Admin Interface** coded on top of **Material Dashboard**, an open-source `Boostrap 5` design from `Creative-Tim`.

> Actively supported by [AppSeed](https://appseed.us/) via `Email` and `Discord`.

<br>

**Links & Resources**

- [Django Material Dashboard](https://appseed.us/product/material-dashboard/django/) - free starter with the same design
- [Django Material Dashboard](https://django-material-dashboard.appseed-srv1.com/) - LIVE Demo

<br />

![Django Admin Material Dashboard - Edit users page.](https://user-images.githubusercontent.com/51070104/169301658-6cf27993-c451-4cd4-9ffa-2968b8981167.png)

<br>

## Why `Django Admin Material`

- Modern `Bootstrap 5` Design
- `Responsive Interface`
- `Minimal Template` overriding
- `Easy integration`

<br />

## How to use it

<br />

> **Install the package** via `PIP` 

```bash
$ pip install django-admin-material-dashboard
// OR
$ pip install git+https://github.com/app-generator/django-admin-material-dashboard.git
```

<br />

> Add `admin_material` application to the `INSTALLED_APPS` setting of your Django project `settings.py` file (note it should be before `django.contrib.admin`):

```python
    INSTALLED_APPS = (
        ...
        'admin_material.apps.AdminMaterialDashboardConfig',
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

> **Material Dashboard Theme** - `Admin Section` 

![Django Admin Material Dashboard - Admin dashboard page.](https://user-images.githubusercontent.com/51070104/192813541-14f0eb32-fdbf-415b-ad67-07364784a133.jpg)

<br />

> **Material Dashboard Theme** - `Admin Widgets`

![Django Admin Material Dashboard - New User Page.](https://user-images.githubusercontent.com/51070104/192813655-8772ae21-b707-42a4-b2ba-15d648bf2768.jpg) 

<br />

---
**[Django Admin Material](https://github.com/app-generator/django-admin-material-dashboard)** - Modern Admin Interface provided by **[AppSeed](https://appseed.us/)**
