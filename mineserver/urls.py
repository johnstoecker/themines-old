"""mineserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from mines import views as mine_views


urlpatterns = [
    path('dashboard/', include('mines.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.login, name='login'),
    path('password_reset/', auth_views.login, name='password_reset'),
    path('logout/', auth_views.logout, name="logout"),
    path('signup/', mine_views.signup, name="signup"),
    path('', mine_views.home, name="home"),
    path('home/', mine_views.home, name="home"),
    path('mining/', mine_views.mining, name="mining")
]

# from django.conf.urls import url
#
# urlpatterns = [
#     ...
#     url(r'^signup/$', core_views.signup, name='signup'),
# ]
