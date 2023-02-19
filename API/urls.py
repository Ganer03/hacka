from django.urls import path, include, re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Landlords', views.Landlords)
router.register('Leasers', views.Leasers)
router.register('Buildings', views.Buildings)
router.register('CommercialObjects', views.CommercialObjects)
router.register('Positions', views.Positions)
router.register('Personals', views.Personals)
router.register('Services', views.Services)
router.register('HcsTypes', views.HcsTypes)
router.register('Hcss', views.Hcss)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^get_buildings/(?P<lord_pk>\d+)/$', views.get_buildings, name='get_buildings'),
    re_path(r'^get_com_objects/(?P<building_pk>\d+)/$', views.get_objects, name='get_objects'),
    re_path(r'^get_board/(?P<lord_pk>\d+)/$', views.get_board, name='get_board'),
    re_path(r'^get_incomes/(?P<lord_pk>\d+)/$', views.get_incomes, name='get_incomes'),
    path('counter_agents/', views.counter_agents, name='counter_agents'),
    path('counter_agents.json', views.counter_agents_json, name='counter_agents_json'),
    path('rent_documents/<int:lord_pk>/', views.rent_documents, name='rent_documents'),
    path('set_peoples/<int:a>/', views.set_peoples, name='set_peoples'),
    path('get_peoples/', views.get_peoples, name='get_peoples'),
    path('rent_documents/<int:lord_pk>.json', views.rent_documents_json, name='rent_documents_json')
]
urlpatterns.extend(staticfiles_urlpatterns())
