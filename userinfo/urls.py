from django.conf.urls import url
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^addqueryuser/$', login_required(views.UserRecordView.as_view())),
    url(r'^logout/', views.user_logout, name='user_logout'),
    url(r'^login/$', views.CustomAuthToken.as_view()),
    url(r'^delete/(?P<email>[\w.@+-]+)$', login_required(views.UserOperations.as_view())),
    # url(r'^$', views.WelcomePage.as_view()),
    # url(r'^query/(?P<accountsInfo>[\w.@+-]+)$', views.UserQuery.as_view()),
    # url(r'^updateAccounts/$', views.UserUpdateInfo.as_view()),
    # url(r'^logout/$', auth_views.logout, name='logout'),
]

