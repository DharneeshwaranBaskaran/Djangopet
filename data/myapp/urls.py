from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path('store_id/', views.store_id, name='store_id'),
    path('store_id_page/', views.store_id_page, name='store_id_page'), 
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'), 
    path('logout/', views.logout_view, name='logout'), 
    path('update_like_dislike/', views.update_like_dislike, name='update_like_dislike'), 
    path('add_pet/', views.add_pet, name='add_pet'), 
    path('remove_pet/', views.remove_pet, name='remove_pet'),
]
