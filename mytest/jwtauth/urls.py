from django.urls import path,re_path,include
from django.conf.urls.static import static
from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView

app_name='jwtauth'
urlpatterns=[
    path('user/',UserRetrieveUpdateAPIView.as_view()),
    path('users/',RegistrationAPIView.as_view()),
    path('users/login/',LoginAPIView.as_view()),
]