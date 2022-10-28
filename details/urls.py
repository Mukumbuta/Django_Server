from django.urls import path
from details import views


urlpatterns = [
    path('details/', views.slack_Details),
]