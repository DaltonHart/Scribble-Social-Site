from django.urls import path
from . import views

urlpatterns = [
    # if we go to '/' got to the views, run the post list function
    path('', views.post_list, name='post_list'),
    path('posts/<int:pk>', views.post_detail, name='post_detail'),
    path('comments/', views.comment_list, name='comment_list')
]