from django.urls import path
from . import views

urlpatterns = [
   # path('/upload/', views.upload_receipt, name='upload_receipt'),
    path('', views.upload_receipt, name='upload_receipt'),
   # path('<int:receipt_id>/', views.receipt_detail, name='receipt_detail'),
]