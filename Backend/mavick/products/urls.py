from django.urls import path, include

from users import views
from .views import (ProductDetailsGenericView, ProductConcretGenericView,
CategoriaConcretGenericView,TallaConcretGenericView, CategoriaDetailsGenericView, TallaDetailsGenericView)
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'producto', ProductoViewSet, basename='producto')
# router.register(r'producto_corto', ProductoModelViewSet, basename='producto_corto')

urlpatterns = [
    path('producto/', ProductConcretGenericView.as_view()),
    path('categoria/', CategoriaConcretGenericView.as_view()),
    path('talla/', TallaConcretGenericView.as_view()),
    path('producto/<int:pk>', ProductDetailsGenericView.as_view()),
    path('categoria/<int:pk>', CategoriaDetailsGenericView.as_view()),
    path('talla/<int:pk>', TallaDetailsGenericView.as_view()),
    # path('vistas/', include(router.urls))
]
