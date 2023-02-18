from djangofiles.urls import path
from .views import *

urlpatterns = [
    path('get_credit/', get_credit),
    path('create_credit/', create_credit),
    path('search_credit/<int:pk>/', search_credit),
    path('delete_credit/<int:pk>/', delete_credit),
    path('confirmate/<int:pk>/', confirmate),
]