from django.urls import path
from .views import TodoWorkView


urlpatterns = [
    path("work/", TodoWorkView.as_view(), name="todo"),
]
