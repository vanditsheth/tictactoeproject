from django.conf.urls import patterns,url
from tictactoe import views

urlpatterns = patterns('',
    #Actions
    url(r'^$', views.index, name='index'),
    url(r'^login_do/', views.login_do, name='login_do'),
    url(r'^logout_do/', views.logout_do, name='logout_do'),
    url(r'^playturn/', views.playturn, name='playturn'),    
    url(r'^refresh/', views.refresh, name='refresh'),    
    url(r'^giveplayboardpage/', views.giveplayboardpage, name='giveplayboardpage'),    
)
