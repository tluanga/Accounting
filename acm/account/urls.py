from django.urls import path
from .views import RegisterView, CreateTokenView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('token/', CreateTokenView.as_view(), name='token')
]
