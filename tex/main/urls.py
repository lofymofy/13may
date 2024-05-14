from django.urls import path
from .views import RegisterUserView, AuthUser, AllTovarView, CreateOrderView, ListOrderView
from . import views

urlpatterns = [
    path('reg/', RegisterUserView.as_view(), name='reg'),
    path('', views.main_page, name='main_page'),
    path('auth/', AuthUser.as_view(), name='auth'),
    path('logout', views.logout_user, name='logout'),
    path('tovar/', AllTovarView.as_view(), name='tovar'),
    path('create/<int:tovar_id>/', CreateOrderView.as_view(), name='create'),
    path('orders/', ListOrderView.as_view(), name='orders')

]