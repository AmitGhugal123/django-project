from django.urls import path
from . import views

#
urlpatterns = [
    #localhost:8000/firstone
    #localhost:8000/fisrtone/contact
    path('', views.all_firstone, name='all_firstone'),
    # path('contact/', views.contact, name='contact'),
    
]