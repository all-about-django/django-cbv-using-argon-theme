from django.urls import include, path
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('hello', TemplateView.as_view(template_name='__base.html')),
    path('store/', include('store.urls')),

]
