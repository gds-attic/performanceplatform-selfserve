from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns(
    '',
    url(r'^$',
        'performanceplatformselfserve.submissions.views.default',
        name='default'),
    url(r'^question1/',
        'performanceplatformselfserve.submissions.views.question1',
        name='question1'),
    url(r'^dashboard/',
        'performanceplatformselfserve.submissions.views.dashboard',
        name='dashboard'),
    url(r'^question2/',
        'performanceplatformselfserve.submissions.views.question2',
        name='question2'),
    url(r'^question3/',
        'performanceplatformselfserve.submissions.views.question3',
        name='question3'),
    url(r'^question4/',
        'performanceplatformselfserve.submissions.views.question4',
        name='question4'),
    url(r'^question5/',
        'performanceplatformselfserve.submissions.views.question5',
        name='question5'),
    url(r'^summary/',
        'performanceplatformselfserve.submissions.views.summary',
        name='summary'),
    url(r'^confirmation/',
        'performanceplatformselfserve.submissions.views.confirmation',
        name='confirmation'),
    url(r'^goals/',
        'performanceplatformselfserve.submissions.views.goals',
        name='goals'),
    url(r'^views/',
        'performanceplatformselfserve.submissions.views.views',
        name='views'),
    url(r'^view_template/',
        'performanceplatformselfserve.submissions.views.view_template',
        name='view_template'),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
