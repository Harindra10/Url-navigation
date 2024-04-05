from django.urls import path
from drinks.views import *
app_name='drinks'

urlpatterns=[
path('bacarid/',bacarid,name='bacarid'),
path('black_white/',black_white,name='black_white'),
]