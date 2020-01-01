
from django.urls import path
from . import views

urlpatterns = [
path('home/',views.home,name='home'),
path('admission/', views.admission, name='admission'),
path('course/',views.course,name='course'),
path('history/',views.history,name='history'),
]
