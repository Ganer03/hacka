from django.urls import path, include
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
    path(r'^dashboard/link/(?P<pk>\d+)-(?P<code>\w+)/$', views.free_home, name='free_home')
]
urlpatterns.extend(staticfiles_urlpatterns())
