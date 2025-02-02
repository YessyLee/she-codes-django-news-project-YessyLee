"""she_codes_news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path #path argument is used to find the URL
from users import views as user_views

urlpatterns = [
    path('news/', include('news.urls')),
    path('admin/', admin.site.urls),
    # path('<int:pk>/', include('socialShare.urls')),
    # path('create-account/', user_views.CreateAccountView.as_view()), 
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
]
