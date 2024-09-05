
from django.urls import  path
from app import views
urlpatterns = [ 
    path('',views.index,name='index'),
     path('',views.about,name='about'), 
     path('insert',views.insertData,name='insertData')# type: ignore
]
