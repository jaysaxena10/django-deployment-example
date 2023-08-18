from django.urls import path
from basicapp import views

app_name='basicapp'

urlpatterns=[
    path('Registration/',views.Registration,name='Registration'),
    path('login/',views.user_login,name='user_login')

]