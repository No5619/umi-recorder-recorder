from django.urls import path
from .views import RecordVodView

urlpatterns = [
    path('start_recording/', RecordVodView.as_view()),
]