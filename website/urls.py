from django.urls import path

from . import views

app_name = 'website'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:number>/', views.ProfileView.as_view(), name='profile')
]
