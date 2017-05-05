from django.conf.urls import patterns, url
from . import views

#from wkhtmltopdf.views import PDFTemplateView

import os
from django.conf.urls.static import static
from django.conf import settings
#from numpy.distutils.from_template import template_name_re

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^get-all-items/$', views.get_all_items, name='get_all_items'),
        url(r'^get-all-items-en/$', views.get_all_items_en, name='get_all_items_en'),
        url(r'^handle/$', views.handle, name='handle'),

        #url(r'^login/$', views.user_login, name='login'),
)

if settings.DEBUG:
    media_root = os.path.join(settings.PROJECT_PATH, 'media')
    urlpatterns += static('/media/', document_root=media_root)
