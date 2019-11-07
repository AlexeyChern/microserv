from django.urls import path

from .views import ItemView

app_name = "items"

urlpatterns = [
    path('items/', ItemView.as_view()),
]