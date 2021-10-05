from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('test/', test)
]

# К test обращаемся, как /news/test

