
from django.urls import path, include
from .import views

urlpatterns = [
   path('', views.index, name='index'),
   path('addimage/', views.add_image, name='add'),
   path('<int:id>/', views.details_img, name='details'),
   path('search/', views.search, name='search'),
]

