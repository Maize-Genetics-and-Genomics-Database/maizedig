from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('taxon_home.views.applications.public',
    # Examples:
    # url(r'^$', 'mycoplasma_site.views.home', name='home'),
    # url(r'^mycoplasma_site/', include('mycoplasma_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', 'Home.Application.renderAction'),
    url(r'^index.html$', 'Home.Application.renderAction'),
    url(r'^images/editor$','EditImage.Application.renderAction'),
    url(r'^images/$', 'Images.Application.renderAction'),
    url(r'^genome_browser/$', 'GBrowse.Application.renderAction'),
    url(r'^blast/$', 'Blast.Application.renderAction'),
    url(r'^login_handler/$', 'Login.Application.renderAction'),
    url(r'^logout_handler/$', 'Logout.Application.renderAction'),
    url(r'^search/$', 'Search.Application.renderAction'),
    url(r'^iSearch/$', 'iSearch.Application.renderAction'),
    url(r'^advancedSearch/$', 'AdvancedSearch.Application.renderAction')
)

urlpatterns += patterns('taxon_home.views.webServices',
    url(r'^api/tags$', 'Tags.Application.renderAction'),
    url(r'^api/tagGroups$', 'TagGroups.Application.renderAction'),
    url(r'^api/geneLinks$', 'GeneLinks.Application.renderAction'),
    url(r'^api/notes$', 'Notes.Application.renderAction'),
    url(r'^api/images$', 'Images.Application.renderAction'),
    url(r'^api/geneLinks/search$', 'SearchGeneLinks.Application.renderAction'),
    url(r'^api/tags/search$', 'SearchTags.Application.renderAction'),
    url(r'^api/tagGroups/search$', 'SearchTagGroups.Application.renderAction'),
    url(r'^api/aggregate/tagGroups$', 'AggregateTagGroups.Application.renderAction'),
    url(r'^api/aggregate/tagGroups/search$', 'AggregateTagGroupsSearch.Application.renderAction'),
    url(r'^api/images/search$', 'SearchImages.Application.renderAction'),
    url(r'^api/organisms/search$', 'SearchOrganisms.Application.renderAction')
)

urlpatterns += patterns('taxon_home.views.applications.registered',
    url(r'^administration/$', 'Administration.Application.renderAction'),
    url(r'^administration/uploadImages/$', 'ImageUploader.Application.renderAction'),
    url(r'^administration/tgManager$', 'TGManager.Application.renderAction')
)

urlpatterns += patterns('taxon_home.views.applications.admin',
    # admin patterns for urls
    url(r'^administration/customize/$', 'Customize.Application.renderAction')
)


urlpatterns += patterns('', 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'taxon_home.views.applications.public.Media.Application.renderAction', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static_site/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATICFILES_DIRS[0]}),
    url(r'^static/admin/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/usr/lib/python2.7/site-packages/django/contrib/admin/media'}),
)
