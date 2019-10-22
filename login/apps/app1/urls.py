from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^success$', views.success),
	url(r'^clear$', views.clear),
	url(r'^wall$', views.wall),
	url(r'^postm$', views.postm),
	url(r'^postc$', views.postc),
	url(r'^delete$', views.delete)
]