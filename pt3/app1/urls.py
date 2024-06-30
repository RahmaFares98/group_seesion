from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index ),
    path('Istanbul', views. Istanbul ),
    path('Trabzon', views. Trabzon ),
    path('process', views.process ),
    path('register_again', views.register_again ),
        path('register_again', views.register_again )


    

]
