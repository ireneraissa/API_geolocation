from django.conf.urls import url
from pharmacie_chat import views

urlpatterns = [
    url(r'^pharmacie_chat/$', views.chatbot_list),
    url(r'^pharmacie_chat/(?P<pk>[0-9]+)/$', views.pharmacie_detail),
    url(r'^proche/$', views.position_list)
]
