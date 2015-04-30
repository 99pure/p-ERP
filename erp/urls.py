from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'erp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Initial page
    url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'}),

    url(r'^admin/', include(admin.site.urls)),
]
