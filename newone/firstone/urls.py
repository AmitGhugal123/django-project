from django.urls import path
from . import views

#
urlpatterns = [
    #localhost:8000/firstone
    #localhost:8000/fisrtone/contact
    path('', views.all_firstone, name='all_firstone'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    # path('contact/', views.contact, name='contact'),
    
]