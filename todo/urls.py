from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("add/", views.add_todo),
    path("complete/<todo_id>", views.complete_todo),
    path("deletecompleted/", views.delete_completed),
    path("deleteall/", views.delete_all)
]
