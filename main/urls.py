from django.urls import path, re_path
from .views import index,service_worker,manifest,offline


urlpatterns=[
    path('',index,name='home'),
    re_path(r'^serviceworker\.js$', service_worker, name='sw'),
    re_path(r'^manifest\.json$', manifest, name='manifest'),
    path('offline/',offline,name='offline'),
]