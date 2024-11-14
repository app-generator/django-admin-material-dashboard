from django.urls import path
from admin_material import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name="index"),
    path('colors/', views.colors, name="colors"),
    path('typography/', views.typography, name="typography"),
    path('charts/', views.charts, name="charts"),
    path('widgets/', views.widgets, name="widgets"),

    # Base
    path('base/accordion/', views.accordion, name="accordion"),
    path('base/breadcrumb/', views.breadcrumb, name="breadcrumb"),
    path('base/cards/', views.cards, name="cards"),
    path('base/carousel/', views.carousel, name="carousel"),
    path('base/collapse/', views.collapse, name="collapse"),
    path('base/list_group/', views.list_group, name="list_group"),
    path('base/navs_tabs/', views.navs_tabs, name="navs_tabs"),
    path('base/pagination/', views.pagination, name="pagination"),
    path('base/placeholders/', views.placeholders, name="placeholders"),
    path('base/popovers/', views.popovers, name="popovers"),
    path('base/progress/', views.progress, name="progress"),
    path('base/spinners/', views.spinners, name="spinners"),
    path('base/tables/', views.base_tables, name="base_tables"),
    path('base/tooltips/', views.tooltips, name="tooltips"),

    # Buttons
    path('buttons/', views.buttons, name="buttons"),
    path('buttons/group/', views.button_group, name="button_group"),
    path('buttons/dropdowns/', views.dropdowns, name="dropdowns"),

    # Forms
    path('form/check-radios/', views.check_radios, name="check_radios"),
    path('form/floating-labels/', views.floating_labels, name="floating_labels"),
    path('form/form-control/', views.form_control, name="form_control"),
    path('form/input-group/', views.input_group, name="input_group"),
    path('form/layout/', views.layout, name="layout"),
    path('form/range/', views.range, name="range"),
    path('form/select/', views.select, name="select"),
    path('form/validation/', views.validation, name="validation"),

    # Icons
    path('icons/brand/', views.icons_brand, name="icons_brand"),
    path('icons/flag/', views.icons_flag, name="icons_flag"),
    path('icons/free/', views.icons_free, name="icons_free"),

    # Notifications
    path('notification/alerts/', views.alerts, name="alerts"),
    path('notification/badge/', views.badge, name="badge"),
    path('notification/modals/', views.modals, name="modals"),
    path('notification/toasts/', views.toasts, name="toasts"),

    # Error
    path('error/404/', views.error_404, name="error_404"),
    path('error/500/', views.error_500, name="error_500"),

    # Authentication
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/logout/', views.user_logout_view, name='logout'),
    path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name="password_change_done" ),
    path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', 
        views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),
]
