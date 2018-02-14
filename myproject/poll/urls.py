from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListPoll.as_view()),
    path('<int:pk>/', views.DetailPoll.as_view())
]