
from django.urls import include, path

from . import views

urlpatterns = [
	path('', views.index, name='index'),

	path('<int:chatroom_id>/', views.room, name="room"),
]
