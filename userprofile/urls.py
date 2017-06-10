
from django.conf.urls import url
from . import views

app_name='userprofile'

urlpatterns = [
    url(r'^edit', views.editprofile, name="edit"),
    url(r'^(?P<username>[0-9A-Za-z_]+)/board', views.board, name="board"),
    url(r'^(?P<username>[0-9A-Za-z_]+)', views.profile, name="profile"),
    url(r'^', views.profile, name="profile"),

]
