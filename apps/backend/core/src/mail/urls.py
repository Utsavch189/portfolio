from django.urls import path
from .views import EmailApiView

urlpatterns = [
    path('',EmailApiView.as_view(),name="email-api-view")
]
