from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('solve/<int:a>/+/<int:b>', views.add, name='add'),
    path('solve/<int:a>/-/<int:b>', views.subtract, name='subtract'),
    path('solve/<int:a>/*/<int:b>', views.multiply, name='multiply'),
    path('solve/<int:a>/%/<int:b>', views.divide, name='divide'),
]