# entries/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.EntryListView.as_view(),
        name="entry-list"
    ),
    path(
        "entry/<int:pk>",
        views.EntryDetailView.as_view(),
        name="entry-detail"
    ),
    path(
        "create",
        views.EntryCreateView.as_view(),
        name="entry-create"
    ),
    path(
        "entry/<int:pk>/update",
        views.EntryUpdateView.as_view(),
        name="entry-update"
    ),
    path(
        "entry/<int:pk>/delete",
        views.EntryDeleteView.as_view(),
        name="entry-delete"
    ),
    path(
        "register", 
        views.register_request, 
        name="register"
    ),
    path(
        "login", 
        views.login_request, 
        name="login"
    ),
    path(
        "logout", 
        views.logout_view, 
        name="logout"
    ),
    path(
        "profile/<username>", 
        views.user_profile, 
        name="user_profile"
        ),
]