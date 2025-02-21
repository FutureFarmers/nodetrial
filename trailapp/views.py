import requests
from django.shortcuts import render, redirect

NODEMCU_IP = "http://192.168.215.222"  # Update with your NodeMCU IP

def control_led(request, action):
    try:
        response = requests.get(f"{NODEMCU_IP}/led/{action}")
        return redirect("home")
    except requests.exceptions.RequestException:
        return render(request, "home.html", {"error": "NodeMCU Not Reachable"})

def home(request):
    try:
        response = requests.get(f"{NODEMCU_IP}/led/status")
        led_status = response.text
    except requests.exceptions.RequestException:
        led_status = "Unknown"

    return render(request, "home.html", {"led_status": led_status})
