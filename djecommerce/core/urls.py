from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name= 'home'),
    path('search', views.search, name='search'),
    path('category-list', views.category_list, name= 'category-list'),
    path('brand-list', views.brand_list, name= 'brand-list'),
    path('product-list', views.product_list, name= 'product-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
