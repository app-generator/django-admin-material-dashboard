# [Django Admin Material](https://appseed.us/product/material-dashboard/django/)

Modern template for **Django** that covers `Admin Section`, all authentication pages (registration included) crafted on top of **[Material Dashboard](https://appseed.us/product/material-dashboard/django/)**, an open-source `Bootstrap 5` design from `Creative-Tim`.

> Actively supported by [AppSeed](https://appseed.us/) via `Email` and `Discord`.

<br>

**Links & Resources**

- [Django Admin Material](https://appseed.us/product/material-dashboard/django/) - `Product page`
  - `Features`: Fully-configured, `CI/CD` via Render
- UI Kit: [Material Dashboard BS5](https://www.creative-tim.com/product/material-dashboard?AFFILIATE=128200) `v3.0.5` by Creative-Tim
- **Sections Covered**: 
  - `Admin Section`, reserved for `superusers`
  - `All pages` managed by `Django.contrib.AUTH`
  - `Registration` page
  - `Misc pages`: colors, icons, typography, blank-page 
  
<br />

![Material Dashboard 2](https://user-images.githubusercontent.com/51070104/211141345-81631acb-ae77-4b31-ba25-a539505da41a.png)

<br />

## Why `Django Admin Material`

- Modern [Bootstrap 5](https://www.admin-dashboards.com/bootstrap-5-templates/) Design
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

> Add `LOGIN_REDIRECT_URL` and `EMAIL_BACKEND` of your Django project `settings.py` file:

```python
    LOGIN_REDIRECT_URL = '/'
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

<br />

> Add `admin_material` urls in your Django Project `urls.py` file

```python
    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('admin_material.urls')),
    ]
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

## [PRO Version](https://appseed.us/product/material-dashboard2-pro/django/)   

This design is a pixel-perfect [Bootstrap 5](https://www.admin-dashboards.com/bootstrap-5-templates/) Dashboard with a fresh, new design inspired by Google's Material Design. `Material Dashboard 2 PRO` is built with over 300 frontend individual elements, like buttons, inputs, navbars, nav tabs, cards, or alerts, giving you the freedom of choosing and combining.

> Features: 

- `Up-to-date Dependencies`
- `Design`: [Django Theme Material2](https://github.com/app-generator/django-material-dashboard2-pro) - `PRO Version`
- `Sections` covered by the design:
  - **Admin section** (reserved for superusers)
  - **Authentication**: `Django.contrib.AUTH`, Registration
  - **All Pages** available in for ordinary users 
- `Docker`, `Deployment`:
  - `CI/CD` flow via `Render`

<br />

![Material Dashboard 2 Pro](https://user-images.githubusercontent.com/51070104/211141418-6b7886eb-6fb3-433e-91c9-2895c086099a.png)

<br />

---
**[Django Admin Material](https://appseed.us/product/material-dashboard/django/)** - Modern Admin Interface provided by **[AppSeed](https://appseed.us/)**
