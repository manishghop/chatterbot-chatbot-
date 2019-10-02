from django.conf.urls import url
from chatapp import views
from django.views.generic.base import RedirectView
virtusa_url={'ac':'https://virtusa.service-now.com/sp?id=sc_cat_item&sys_id=329ba0efdbeff240a8d4f2adbf961995',
             'hk':'https://virtusa.service-now.com/sp?id=sc_cat_item&sys_id=06d1816bdbef7a405eb551b0cf96197c',
             'rb':'https://virtusa.service-now.com/sp?id=sc_cat_item&sys_id=517fbb3adb2f3a405eb551b0cf9619f7'}
urlpatterns=[
    url(r'^api/chatterbot/', views.ChatterBotApiView.as_view(), name='chatterbot'),
    url(r'ac',RedirectView.as_view(url=virtusa_url['ac'])),
    url(r'hk',RedirectView.as_view(url=virtusa_url['hk'])),
    url(r'rb',RedirectView.as_view(url=virtusa_url['rb'])),
]