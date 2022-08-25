from django.contrib import admin
from django.urls import path, include

from api_sprint8 import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clientes', views.ClienteViewSet, basename='clientes')
router.register(r'cuentas', views.CuentaViewSet, basename='cuentas')
router.register(r'prestamos', views.PrestamoViewSet, basename='prestamos')
router.register(r'prestamos-sucursales', views.PrestamoSucursalViewSet, basename='prestamos-sucursales')
router.register(r'tarjetas', views.TarjetasViewSet, basename='tarjetas')
router.register(r'direcciones', views.DireccionViewSet, basename='direcciones')
router.register(r'sucursales', views.SucursalViewSet, basename='sucursales')
router.register(r'clientes-tipo', views.ClienteTipoViewSet, basename='clientes-tipo')
router.register(r'prestamo-tipo', views.TipoPrestamoViewSet, basename='prestamo-tipo')
router.register(r'tarjeta-marca', views.MarcaTarjetaViewSet, basename='tarjeta-marca')
router.register(r'cuenta-tipo', views.TipoCuentaViewSet, basename='cuenta-tipo')

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#         path('', views.api_root),
#         path('clientes/', views.ClienteList.as_view(), name='clientes-list'),
#         path('clientes/<int:pk>/', views.ClienteDetail.as_view(), name='cliente-detail'),
#         path('cuenta/<int:pk>/', views.CuentaDetail.as_view(), name='cuenta-detail'),
#         path('cuentas/', views.CuentaList.as_view(), name='cuentas-list'),
#         path('prestamo/<int:pk>/', views.PrestamoDetail.as_view(), name='prestamo-detail'),
#         path('prestamos/', views.PrestamoList.as_view(), name='prestamos-list'),
#         path('prestamos-sucursal/<int:pk>/', views.PrestamoSucursalList.as_view()),
#         path('tarjetas/<int:pk>/', views.TarjetasList.as_view()),
#         path('direccion/<int:pk>/', views.DireccionDetail.as_view(), name='direccion-detail'),
#         path('direcciones/', views.DireccionList.as_view(), name='direccion-list'),
#         path('sucursales/', views.SucursalList.as_view(), name='sucursales-list'),
        
#         path('clientes-tipo/<int:pk>/', views.ClienteTipoDetail.as_view(), name='tipocliente-detail'),
#         path('sucursales/<int:pk>/', views.SucursalDetail.as_view(), name='sucursal-detail'),
#         path('prestamo-tipo/<int:pk>/', views.TipoPrestamoDetail.as_view(), name='tipoprestamo-detail'),
#         path('tarjeta/<int:pk>/', views.TarjetasDetail.as_view(), name='tarjeta-detail'),
#         path('marca-tarjeta/<int:pk>/', views.MarcaTarjetaDetail.as_view(), name='marcatarjeta-detail'),
#         path('cuenta-tipo/<int:pk>/', views.TipoCuentaDetail.as_view(), name='tipocuenta-detail'),
#     ]