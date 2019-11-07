from django.urls import path

from .views import ItemView, OneItemView

app_name = "items"

urlpatterns = [
    path('items/', ItemView.as_view()),

    path('items/<int:pk>', OneItemView.as_view()),
]