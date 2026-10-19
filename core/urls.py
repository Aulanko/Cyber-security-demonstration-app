from django.urls import path

from . import views

urlpatterns = [
    path("", views.note_list, name="note_list"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("notes/new/", views.note_create, name="note_create"),
    path("notes/<int:note_id>/", views.note_detail, name="note_detail"),
    path("notes/<int:note_id>/delete/", views.note_delete, name="note_delete"),
    path("search/", views.search, name="search"),
]