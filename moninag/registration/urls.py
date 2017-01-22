from django.conf.urls import url
from registration.views import activate, inactive_account,login, auth_view, logout, loggedin, invalid_login, register_user, register_success

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # auth
    url(r'^$', login, name='login'),
    url(r'^auth/$', auth_view, name='auth_view'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^loggedin/$', loggedin, name='loggedin'),
    url(r'^invalid/$', invalid_login, name='invalid_login'),
    url(r'^inactive_account/$', inactive_account, name='inactive_account'),
    url(r'^activate/(?P<activation_key>[0-9]+)/$', activate, name='activate'),
    url(r'^register/$', register_user, name='register_user'),
    url(r'^register_success/$', register_success, name='register_success'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
