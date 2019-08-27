from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name = 'post_list'), # assigning a vew called 'post_list' to the root URL
                                                   # this URL pattern is going to match an empty string and the
                                                   # Django URL resolver is going to ignore the domain name (127.0.0.1:8000/)
]
