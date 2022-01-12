from django.urls import re_path, include
from django.contrib import admin

urlpatterns = [
    re_path(r'^', include('myapp.urls')),
    re_path(r'^admin/', admin.site.urls),

]