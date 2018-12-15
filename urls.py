"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^q1/(\d{8})/(\d+)/$',views.q1),
    url(r'^q2/(\d+)/(\S+)/(\w+)/$',views.q2), 
    url(r'^q3/(\w+)/(\d{8})/$',views.q3),
    url(r'^q4/(\d{8})/$',views.q4),
    url(r'^q5/(\w+)/(\d{8})/$',views.q5),
    url(r'^q6/(\d{8})/(\S+)/(\d+)/$',views.q6),
    url(r'^q7/(\w+)/(\w+)/$',views.q7),
    url(r'^q8/(\w+)/(\w+)/(\S+)/$',views.q8),
    url(r'^q9/(\w+)/$',views.q9),
    url(r'^q10/(\d{8})/$',views.q10),
    url(r'^q11/(\w+)/(\S+)/$',views.q11),
    url(r'^q12/(\w+)/(\w+)/(\d{8})/$',views.q12),
    url(r'^q13/(\w+)/(\w+)/$',views.q13),
    url(r'^q14/(\w+)/$',views.q14),
    url(r'^q15/(\w+)/$',views.q15),
    url(r'^q16/(\S+)/(\S+)/(\S+)/$',views.q16),
    url(r'^q17/(\S+)/(\S+)/$',views.q17),
    url(r'^q18/(\d+)/$',views.q18),
    url(r'^q19/(\S+)/(\d+)/(\S+)/(\d+)/(\S+)/(\d+)/$',views.q19),
    url(r'^q20/(\w+)/(\d{8})/(\w+)/$',views.q20),
    url(r'^q1/$',views.indexQ1),
    url(r'^q2/$',views.indexQ2),
    url(r'^q3/$',views.indexQ3),
    url(r'^q4/$',views.indexQ4),
    url(r'^q5/$',views.indexQ5),
    url(r'^q6/$',views.indexQ6),
    url(r'^q7/$',views.indexQ7),
    url(r'^q8/$',views.indexQ8),
    url(r'^q9/$',views.indexQ9),
    url(r'^q10/$',views.indexQ10),
    url(r'^q11/$',views.indexQ11),
    url(r'^q12/$',views.indexQ12),
    url(r'^q13/$',views.indexQ13),
    url(r'^q14/$',views.indexQ14),
    url(r'^q15/$',views.indexQ15),
    url(r'^q16/$',views.indexQ16),
    url(r'^q17/$',views.indexQ17),
    url(r'^q18/$',views.indexQ18),
    url(r'^q19/$',views.indexQ19),
    url(r'^q20/$',views.indexQ20),
]
