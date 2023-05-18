"""
URL configuration for gazmashina project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from server.views import ProductList, ProductDetail, PartnerList, PartnerDetail, DirectionList, DirectionDetail, \
    ServiceList, ServiceDetail, HistoryList, HistoryDetail, SubServiceList, SubServiceDetail, ContactDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('partners/', PartnerList.as_view(), name='partner_list'),
    path('partners/<int:pk>/', PartnerDetail.as_view(), name='partner_detail'),
    path('directions/', DirectionList.as_view(), name='direction_list'),
    path('directions/<int:pk>/', DirectionDetail.as_view(), name='direction_detail'),
    path('services/', ServiceList.as_view(), name='service_list'),
    path('services/<int:pk>/', ServiceDetail.as_view(), name='service_detail'),
    path('sub_services/', SubServiceList.as_view(), name='sub_service_list'),
    path('sub_services/<int:pk>/', SubServiceDetail.as_view(), name='sub_service_detail'),
    path('history/', HistoryList.as_view(), name='history_list'),
    path('history/<int:pk>/', HistoryDetail.as_view(), name='history_detail'),
    path('contacts/', ContactDetail.as_view(), name='contact_detail')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
