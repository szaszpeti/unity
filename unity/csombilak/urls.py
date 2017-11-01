from django.conf.urls import url
from . import views


# SET THE NAMESPACE!
app_name = 'csombilak'


urlpatterns=[
    url(r'^$',views.index, name='index'),
]