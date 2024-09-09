from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("submissions", views.submissions_view, name="submissions"),
    path("submission-<str:ProjectCode>", views.project_view, name="project"),
    path("submit", views.submit_project, name="submit"),
]