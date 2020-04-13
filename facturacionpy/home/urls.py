from django.urls import path, include

from home.views import Home

urlpatterns = [
    path('', Home.as_view(), name="home")
    
]