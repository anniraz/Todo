from django.urls import path

from .views import *

urlpatterns = [
    path('create/',TodoCreateApiView.as_view()),
    path('detail/<int:pk>/',TodoDetailApiView.as_view()),
    path('delete/all/',RemoveAllTodoApiView.as_view())
]
