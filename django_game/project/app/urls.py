from django.urls import path

from .views import home, registration, login_view, logout_view, shop, shop_add, \
    add_money

urlpatterns = [
    path('home', home, name="home"),
    path('registration', registration),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('shop', shop, name="shop"),
    path('skin/<int:id>', shop_add),
    path('money/<int:ball>', add_money)
]