from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>", views.PostDetailView.as_view(), name="post-detail"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("topics", views.TopicListView.as_view(), name="topics"),
    path("", views.PostListView.as_view(), name="posts"),
]
