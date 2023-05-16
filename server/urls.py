from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from server.views import ProductList, ProductDetail, PartnerList, PartnerDetail, DirectionList, DirectionDetail, \
    ServiceDetail, ServiceList, HistoryList, HistoryDetail, SubServiceList, SubServiceDetail

urlpatterns = [
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    path('products/', ProductList.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('partners/', PartnerList.as_view(), name='partner_list'),
    path('partners/<int:pk>/', PartnerDetail.as_view(), name='partner_detail'),
    path('directions/', DirectionList.as_view(), name='direction_list'),
    path('directions/<int:pk>/', DirectionDetail.as_view(), name='direction_detail'),
    path('services/', ServiceList.as_view(), name='service_list'),
    path('services/<int:pk>/', ServiceDetail.as_view(), name='service_detail'),
    path('sub_services/', SubServiceList.as_view(), name='sub_service_list'),
    path('sub_services/<int:pk>/', SubServiceDetail.as_view(), name='sub_service_detail'),
    path('history/', HistoryList.as_view(), name='history_list'),
    path('history/<int:pk>/', HistoryDetail.as_view(), name='history_detail')
]
