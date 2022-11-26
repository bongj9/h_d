from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home_view, name= 'home_view'),
    path('login/', views.login_view, name='login_view'),
    # path('login/validate', views.login_validate, name='login_validate'),
    # path('logout/', views.logout, name='logout'),
    path('nav_list/', views.nav_list_view, name='nav_list_view'),
    path('product_detial/', views.product_detail_view, name='product_detail_view'),
    path('search/', views.search_view, name='search_view'),
    path('signup/', views.signup_view, name='signup_view'),
    # path('join/', views.join_page, name='join_page'),
    # path('edit/', views.edit_user_info, name='edit_user_info'),
]
