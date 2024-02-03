from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('products/', views.products, name="products"),
    path('about/', views.about, name="about"),
    path('order/', views.order, name="order"),
    path('addProduct/', views.addProduct, name="addProduct"),
    path('editProduct/<int:pk>/', views.editProduct, name="editProduct"),
    path('deleteProduct/<int:pk>/', views.deleteProduct, name="deleteProduct"),
    path('addOrder/', views.addOrder, name="addOrder"),
    path('editOrder/<int:pk>/', views.editOrder, name="editOrder"),
    path('deleteOrder/<int:pk>/', views.deleteOrder, name="deleteOrder"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
