from django.urls import path

from . import views

app_name = 'website'
urlpatterns = [
    path('', views.home, name='home'),
    path('dex/', views.DexView.as_view(), name='dex'),
    path('<int:number>/', views.ProfileView.as_view(), name='profile')
]
