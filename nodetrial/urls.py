
from django.urls import path
from trailapp.views import home, control_led

urlpatterns = [
    path("", home, name="home"),
    path("led/<str:action>/", control_led, name="control_led"),
]
