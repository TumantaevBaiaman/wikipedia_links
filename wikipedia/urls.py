from django.urls import path
from . import views

urlpatterns = [
    path('', views.WikipediaLinks.as_view(), name="home page"),
    path('download-logs/', views.download_log_file, name='download-logs')
]
