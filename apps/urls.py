from django.urls import path
from apps.views import login_page, product_page, logout_page, register_page, main_page

urlpatterns = [
    path('', main_page, name='main_page'),
    path('product', product_page, name='product_page'),
    path('logout', logout_page, name='logout_page'),
    path('login', login_page, name='login_page'),
    path('register', register_page, name='register_page')
]
