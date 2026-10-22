from django.urls import path
from products import views
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('products/', views.productview,name='products'),
]
