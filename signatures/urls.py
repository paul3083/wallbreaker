from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('petition/<int:petition_id>/', views.detail_page, name='detail_page'),
]