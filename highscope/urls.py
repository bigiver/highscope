"""highscope URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from reports.views import view_index as vi
from reports.views import view_form as vf

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',vi.index,name='index'),
    url(r'^index/',vi.index,name='index'),
    url(r'^indexM/',vi.indexMain,name='indexMain'),
    url(r'^login/',vi.login,name='login'),
    url(r'^editTesting/',vf.formView,name='formView'),
    url(r'^chartData/',vi.eChart,name='chartData'),
    url(r'^testingView/',vf.testingView,name='testingView'),
    url(r'^reportView/',vf.reportView,name='reportView'),
]
