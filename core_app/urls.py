from django.urls import path
from .views import TrelloApiView

urlpatterns = [
    path('api/v1/', TrelloApiView.as_view(), name='home')
]