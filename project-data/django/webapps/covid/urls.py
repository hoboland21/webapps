"""webapps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import dashboard,dash2,ChartData,Chart2Data
urlpatterns = [
    path('country', dashboard,name="dashboard"),
    path('state', dash2,name="dash2"),
    
    path('api/country/<country>',ChartData.as_view() ),
    path('api/state/<state>',Chart2Data.as_view() ) 


]
