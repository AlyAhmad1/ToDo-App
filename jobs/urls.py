from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('completed/<ID>', views.Completed,  name='Completed'),
    path('not_completed/<ID>', views.Not_Completed,  name='Not_Completed'),
    path('Dell', views.Delete_Completed,  name='Delete_Completed'),
    path('Dell_all', views.Delete_all,  name='Delete_all'),
    path('Dell_all_incomplete', views.Delete_incomplete,  name='Delete_incomplete')

]

