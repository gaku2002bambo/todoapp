from django.urls import path
from .views import TodoList,TodoDetail,DetailView,TodoCreate,TodoUpdate,TodoDelete,events

urlpatterns = [
  path('',TodoList.as_view(), name='list'),
  path("detail/<int:pk>",TodoDetail.as_view(), name="detail"),
  path('create/', TodoCreate.as_view(), name='create'),
  path('update/<int:pk>',TodoUpdate.as_view(), name="update"),
  path('delete/<int:pk>',TodoDelete.as_view(),name='delete'),
  path('api/events', events, name='events'),
]