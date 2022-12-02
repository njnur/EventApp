from django.urls import path

from core import views

app_name = 'core'


urlpatterns = [
    path('ping/', views.PingTestView.as_view()),
    path('', views.HomeView.as_view())
]
