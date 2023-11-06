from django.urls import path
from .views import *

app_name='crm'


urlpatterns = [
        path('home/',home,name="home_show"),
        path('products/',products,name="products_show"),
        path('customers/',customers,name="customers_show"),
]