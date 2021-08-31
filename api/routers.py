from django.urls import path
from .views import ConvertView

app_name = 'api'

urlpatterns = [
    path('converts', ConvertView.as_view()),
]
