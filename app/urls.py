
from django.contrib import admin
from django.urls import path
from app.views import change_todo, delete_todo, home,Login,Signup,add_todo,signout

urlpatterns = [ 
    path('', home, name='home' ),
    path('Login/',Login, name='Login'),
    path('Signup/',Signup),
    path('add-todo/',add_todo),
    path('logout/',signout),
    path('delete-todo/<int:id>' , delete_todo ), 
   path('change-status/<int:id>/<str:status>' , change_todo ), 
]