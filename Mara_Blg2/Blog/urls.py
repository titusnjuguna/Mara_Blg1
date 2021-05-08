from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView


urlpatterns = [
    path('', PostListView.as_view(), name="Blog-home"),
    path('user/<str:username>', UserPostListView.as_view(), name="user-posts"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="Post-detail"),
    path('post/new/', PostCreateView.as_view(), name="Post-create"),
    path('post/<int:pk>/Update/', PostUpdateView.as_view(), name="Post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="Post-delete"),
    path('contact/', views.contact, name="Blog-contact"),
    path('About/', views.About, name="Blog-About")
    

]
