from xml.etree.ElementInclude import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls', namespace='catalog'))
]