from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),  # 메인 페이지
    path('petition/<int:petition_id>/', views.detail_page, name='detail_page'),  # 청원 상세 페이지
    path('petition/<int:petition_id>/sign/', views.sign_petition, name='sign_petition'),  # 서명 처리
]