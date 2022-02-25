from django.urls import path

from . import views

urlpatterns = [
    path('users',views.ListApiView.as_view()),
    path('users/',views.usersCreateAPIView.as_view()),
    path('users/<int:pk>',views.user_detail),
    

]