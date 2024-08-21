from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.articles, name="articles"),
    path("<int:pk>/", views.article_detail, name="article_detail"),

    path("create/", views.create, name="create"),
    path("update/", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),

    path("<int:pk>/comments/", views.comment_create, name="comment_create"),
    path(
        "<int:pk>/comments/<int:comment_pk>/delete/",
        views.comment_delete,
        name="comment_delete",
    ),

    path("<int:pk>/like/", views.like, name="like"),
]