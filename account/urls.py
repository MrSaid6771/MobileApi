from django.urls import path
from account.views import *

urlpatterns = [
    path('create_clent/', create_clent),
    path('get_clent/', get_clent),
    path('delete_clent/<int:pk>/', delete_clent),
    path('update_clent/<int:pk>/', update_clent),
    path('search_clent/<int:pk>/', search_clent),
    path('change_status/<int:pk>/', change_status),

]
