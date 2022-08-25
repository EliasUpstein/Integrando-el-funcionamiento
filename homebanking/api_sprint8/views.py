from django.shortcuts import render

from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status

from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from Clientes.models import Cliente 
from api_sprint8.serializers import ClienteSerializer 

from Cuentas.models import Cuenta 
from api_sprint8.serializers import CuentaSerializer  

from Prestamos.models import Prestamo 
from api_sprint8.serializers import PrestamoSerializer   

from Tarjetas.models import Tarjeta 
from api_sprint8.serializers import TarjetaSerializer 

from Clientes.models import Direccion 
from api_sprint8.serializers import DireccionSerializer

from Clientes.models import Sucursal 
from api_sprint8.serializers import SucursalSerializer

from Clientes.models import TipoCliente 
from api_sprint8.serializers import ClienteTipoSerializer

from Prestamos.models import TipoPrestamo 
from api_sprint8.serializers import PrestamoTipoSerializer

from Tarjetas.models import MarcaTarjeta 
from api_sprint8.serializers import MarcaTarjetaSerializer

from Cuentas.models import TipoCuenta
from api_sprint8.serializers import TipoCuentaSerializer

from rest_framework import viewsets
# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('customer_id') 
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def retrieve(self, request, pk=None):
        cliente = Cliente.objects.filter(pk=pk).first()
        if cliente:
            return Response(self.serializer_class(cliente).data, status=status.HTTP_200_OK) 
        return Response(self.serializer_class(cliente).errors, status=status.HTTP_404_NOT_FOUND)

# class ClienteDetail(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     def get(self, request, pk):
#         cliente = Cliente.objects.filter(pk=pk).first()
#         serializer = ClienteSerializer(cliente, context={'request': request})
#         if cliente:
#             return Response(serializer.data, status=status.HTTP_200_OK) 
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

# class ClienteList(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     def get(self, request): 
#         clientes = Cliente.objects.all().order_by('customer_id') 
#         serializer = ClienteSerializer(clientes, many=True, context={'request': request}) 
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
class CuentaViewSet(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all().order_by('customer_id') 
    serializer_class = CuentaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def retrieve(self, request, pk=None):
        cuenta = Cuenta.objects.filter(pk=pk).first()
        if cuenta:
            return Response(self.serializer_class(cuenta).data, status=status.HTTP_200_OK) 
        return Response(self.serializer_class(cuenta).errors, status=status.HTTP_404_NOT_FOUND)

# class CuentaDetail(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     def get(self, request, pk):
#         cuenta = Cuenta.objects.filter(pk=pk).first()
#         serializer = CuentaSerializer(cuenta, context={'request': request})
#         if cuenta:
#             return Response(serializer.data, status=status.HTTP_200_OK) 
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
# class CuentaList(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     def get(self, request): 
#         cuentas = Cuenta.objects.all().order_by('customer_id') 
#         serializer = CuentaSerializer(cuentas, many=True, context={'request': request}) 
#         return Response(serializer.data, status=status.HTTP_200_OK)    

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all().order_by('loan_id') 
    serializer_class = PrestamoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def retrieve(self, request, pk=None):
        prestamo = Prestamo.objects.filter(pk=pk).first()
        if prestamo:
            return Response(self.serializer_class(prestamo).data, status=status.HTTP_200_OK) 
        return Response(self.serializer_class(prestamo).errors, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        prestamo = Prestamo.objects.filter(pk=pk).first()
        if prestamo: 
            # serializer = PrestamoSerializer(prestamo, context={'request': request}) 
            # prestamo.delete() 
            # return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(self.serializer_class(prestamo).delete(), status=status.HTTP_200_OK) 
    
    def create(self, request):
        serializer = PrestamoSerializer(data=request.data, context={'request': request}) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PrestamoDetail(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     def get(self, request, pk):
#         prestamo = Prestamo.objects.filter(pk=pk).first()
#         serializer = PrestamoSerializer(prestamo, context={'request': request})
#         if prestamo:
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
#     def delete(self, request, pk): 
#         prestamo = Prestamo.objects.filter(pk=pk).first() 
#         if prestamo: 
#             serializer = PrestamoSerializer(prestamo, context={'request': request}) 
#             prestamo.delete() 
#             return Response(serializer.data, status=status.HTTP_200_OK) 
#         return Response(status=status.HTTP_404_NOT_FOUND)
    

# class PrestamoList(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     def get(self, request): 
#         prestamos = Prestamo.objects.all().order_by('loan_id') 
#         serializer = PrestamoSerializer(prestamos, many=True, context={'request': request}) 
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request, format=None): 
#         serializer = PrestamoSerializer(data=request.data, context={'request': request}) 
#         if serializer.is_valid(): 
#             serializer.save() 
#             return Response(serializer.data, status=status.HTTP_201_CREATED) 
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PrestamoSucursalViewSet(viewsets.ModelViewSet):
    # queryset = Prestamo.objects.all().order_by('loan_id') 
    serializer_class = PrestamoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def list(self, request, pk=None):
        sucursal = Sucursal.objects.filter(pk=pk).first()
        asociados = Cliente.objects.filter(branch = sucursal).order_by('customer_id')
        prestamos = []
        for cliente in asociados:
            prestamos += Prestamo.objects.filter(customer = cliente)
        serializer = PrestamoSerializer(prestamos, many=True, context={'request': request}) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# class PrestamoSucursalList(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     def get(self, request, pk): 
#         sucursal = Sucursal.objects.filter(pk=pk).first()
#         asociados = Cliente.objects.filter(branch = sucursal).order_by('customer_id')
#         prestamos = []
#         for cliente in asociados:
#             prestamos += Prestamo.objects.filter(customer = cliente)
#         serializer = PrestamoSerializer(prestamos, many=True, context={'request': request}) 
#         return Response(serializer.data, status=status.HTTP_200_OK)

class TarjetasViewSet(viewsets.ModelViewSet):
    # queryset = Tarjeta.objects.filter(customer_id=pk).order_by('card_id') 
    serializer_class = TarjetaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def retrieve(self, request, pk=None):
        tarjeta = Tarjeta.objects.filter(pk=pk) 
        if tarjeta:
            return Response(self.serializer_class(tarjeta).data, status=status.HTTP_200_OK) 
        return Response(self.serializer_class(tarjeta).errors, status=status.HTTP_404_NOT_FOUND)

# class TarjetasList(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     def get(self, request, pk):
#         tarjetas = Tarjeta.objects.filter(customer_id=pk).order_by('card_id') 
#         serializer = TarjetaSerializer(tarjetas, many=True, context={'request': request}) 
#         return Response(serializer.data, status=status.HTTP_200_OK)

# class TarjetasDetail(APIView):
#     def get(self, request, pk):
#         tarjeta = Tarjeta.objects.filter(pk=pk) 
#         serializer = TarjetaSerializer(tarjeta, many=True, context={'request': request}) 
#         return Response(serializer.data, status=status.HTTP_200_OK)

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all().order_by('address_id') 
    serializer_class = DireccionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def retrieve(self, request, pk=None):
        direccion = Direccion.objects.filter(pk=pk).order_by('address_id') 
        if direccion:
            return Response(self.serializer_class(direccion).data, status=status.HTTP_200_OK) 
        return Response(self.serializer_class(direccion).errors, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        direccion = Direccion.objects.filter(pk=pk).first() 
        serializer = DireccionSerializer(direccion, data=request.data, context={'request': request}) 
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class DireccionDetail(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
#     def put(self, request, pk): 
#         direccion = Direccion.objects.filter(pk=pk).first() 
#         serializer = DireccionSerializer(direccion, data=request.data, context={'request': request}) 
#         if serializer.is_valid(): 
#             serializer.save()
#             return Response(serializer.data) 
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def get(self, request, pk):
#         direccion = Direccion.objects.filter(pk=pk).order_by('address_id') 
#         serializer = DireccionSerializer(direccion, many=True,context={'request': request}) 
#         return Response(serializer.data, status=status.HTTP_200_OK)

# class DireccionList(APIView):
#     def get(self, request):
#         direcciones = Direccion.objects.all().order_by('address_id') 
#         serializer = DireccionSerializer(direcciones, many=True, context={'request': request}) 
#         return Response(serializer.data, status=status.HTTP_200_OK)

class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all().order_by('branch_id') 
    serializer_class = SucursalSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def retrieve(self, request, pk=None):
        sucursal = Sucursal.objects.filter(pk=pk).order_by('branch_id') 
        if sucursal:
            return Response(self.serializer_class(sucursal).data, status=status.HTTP_200_OK) 
        return Response(self.serializer_class(sucursal).errors, status=status.HTTP_404_NOT_FOUND)
   
# class SucursalList(APIView):
#     def get(self, request):
#         sucursales = Sucursal.objects.all().order_by('branch_id') 
#         serializer = SucursalSerializer(sucursales, many=True, context={'request': request}) 
#         return Response(serializer.data, status=status.HTTP_200_OK)

# class SucursalDetail(APIView):
#     def get(self, request, pk):
#         sucursal = Sucursal.objects.filter(pk=pk).order_by('branch_id') 
#         serializer = SucursalSerializer(sucursal, many=True, context={'request': request}) 
#         return Response(serializer.data, status=status.HTTP_200_OK)

    
# @api_view(['GET']) 
# def api_root(request, format=None):
#     return Response({ 
#                      'clientes': reverse('clientes-list', request=request, format=format), 
#                      'cuentas': reverse('cuentas-list', request=request, format=format),
#                      'prestamos': reverse('prestamos-list', request=request, format=format),
#                      'direcciones': reverse('direccion-list', request=request, format=format),
#                      'sucursales': reverse('sucursales-list', request=request, format=format)
#                      })
    
    
class ClienteTipoViewSet(viewsets.ModelViewSet):
    # queryset = TipoCliente.objects.filter(pk=pk).order_by('customer_type_id') 
    serializer_class = ClienteTipoSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def retrieve(self, request, pk=None):
        tipo_cliente = TipoCliente.objects.filter(pk=pk).order_by('customer_type_id') 
        if tipo_cliente:
            return Response(self.serializer_class(tipo_cliente).data, status=status.HTTP_200_OK) 
        return Response(self.serializer_class(tipo_cliente).errors, status=status.HTTP_404_NOT_FOUND)


# class ClienteTipoDetail(APIView):
#     def get(self, request, pk):
#         tipo_cliente = TipoCliente.objects.filter(pk=pk).order_by('customer_type_id') 
#         serializer = ClienteTipoSerializer(tipo_cliente, many=True, context={'request': request}) 
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
class TipoPrestamoViewSet(viewsets.ModelViewSet):
    # queryset = Sucursal.objects.all().order_by('branch_id') 
    serializer_class = PrestamoTipoSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def retrieve(self, request, pk=None):
        tipo_prestamo = TipoPrestamo.objects.filter(pk=pk).order_by('type_id')  
        if tipo_prestamo:
            return Response(self.serializer_class(tipo_prestamo).data, status=status.HTTP_200_OK) 
        return Response(self.serializer_class(tipo_prestamo).errors, status=status.HTTP_404_NOT_FOUND)


# class TipoPrestamoDetail(APIView):
#     def get(self, request, pk):
#         tipo_prestamo = TipoPrestamo.objects.filter(pk=pk).order_by('type_id') 
#         serializer = PrestamoTipoSerializer(tipo_prestamo, many=True, context={'request': request}) 
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class MarcaTarjetaViewSet(viewsets.ModelViewSet):
    # queryset = Sucursal.objects.all().order_by('branch_id') 
    serializer_class = MarcaTarjetaSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def retrieve(self, request, pk=None):
        marca = MarcaTarjeta.objects.filter(pk=pk).order_by('card_id') 
        if marca:
            return Response(self.serializer_class(marca).data, status=status.HTTP_200_OK) 
        return Response(self.serializer_class(marca).errors, status=status.HTTP_404_NOT_FOUND)


# class MarcaTarjetaDetail(APIView):
#     def get(self, request, pk):
#         marca = MarcaTarjeta.objects.filter(pk=pk).order_by('card_id') 
#         serializer = MarcaTarjetaSerializer(marca, many=True, context={'request': request}) 
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
class TipoCuentaViewSet(viewsets.ModelViewSet):
    # queryset = Sucursal.objects.all().order_by('branch_id') 
    serializer_class = TipoCuentaSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def retrieve(self, request, pk=None):
        cuenta_tipo = TipoCuenta.objects.filter(pk=pk).first()
        if cuenta_tipo:
            return Response(self.serializer_class(cuenta_tipo).data, status=status.HTTP_200_OK) 
        return Response(self.serializer_class(cuenta_tipo).errors, status=status.HTTP_404_NOT_FOUND)


# class TipoCuentaDetail(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     def get(self, request, pk):
#         cuenta_tipo = TipoCuenta.objects.filter(pk=pk).first()
#         serializer = TipoCuentaSerializer(cuenta_tipo, context={'request': request})
#         if cuenta_tipo:
#             return Response(serializer.data, status=status.HTTP_200_OK) 
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)