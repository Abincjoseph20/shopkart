from django.urls import path
from . import views


urlpatterns = [
    path('accounts',views.show_account,name='accounts'),
    path('logout',views.sign_out,name='logout')
]