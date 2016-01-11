from django.conf.urls import patterns, url

from surgery.views import SurgeryCreate, SurgeryDelete, SurgeryDetail, SurgeryList, \
    SurgeryUpdate

urlpatterns = patterns('',
    url(
        r'^new/$',
        SurgeryCreate.as_view(),
        name='surgery_create'
    ),
    url(
        r'^delete/(?P<pk>\d+)$',
        SurgeryDelete.as_view(),
        name='surgery_delete'
    ),
    url(
        r'^(?P<pk>\d+?)$',
        SurgeryDetail.as_view(),
        name='surgery_detail'
    ),
    url(
        r'^update/(?P<pk>\d+)$',
        SurgeryUpdate.as_view(),
        name='surgery_update'
    ),
    url(
        r'^$',
        SurgeryList.as_view(),
        name='surgery_list'
    ),
)
