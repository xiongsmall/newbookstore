from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^land/$',views.land,name = 'land'),
    url(r'^landon/$',views.landon,name = 'landon')

]