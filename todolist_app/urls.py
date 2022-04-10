from django.urls import path
from todolist_app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('drag/<id>',views.drag,name='drag'),
    path('drop/<id>',views.drop,name='drop'),
    path('swap',views.swap,name='swap'), 
    path('delete/<id>',views.delete,name='drop'),
    path('edit/<id>',views.edit,name='drop'),
    path('edit/update/<id>',views.update,name='drop'),

]