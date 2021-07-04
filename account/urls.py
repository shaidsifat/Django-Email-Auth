from django.urls import path
from account import views


urlpatterns = [
   path('product/', views.product , name='product'),
    path('product/<int:pk>/',views.product_detail,name='product_detail'), 
    

]