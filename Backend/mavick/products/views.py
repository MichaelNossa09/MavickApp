from django.shortcuts import get_object_or_404 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import generics, mixins, viewsets

from products.models import Producto, Talla, Categoria
from products.serializers import ProductoSerializer, TallaSerializer, CategoriaSerializer
from users import serializers

# Create your views here.
# class ProductView(APIView):

#     def get(self, request):
#         prod = Producto.objects.all()
#         serializer = ProductoSerializer(prod, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer  = ProductoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Producto agregado correctamente'}
#             return Response(res)
#         return Response({'msg': serializer.errors})
#     def delete(self, request):
#         prod = request.data
#         id = prod.get('id')
#         prod = Producto.objects.get(id=id)
#         prod.delete()
#         res = {'msg': 'Producto eliminado correctamente.'}
#         return Response(res)
#     def put(self, request):
#         prod = request.data
#         data = JSONParser().parse(prod)
#         id = data.get('id', None)
#         if id is not None:
#             prod = Producto.objects.get(id=id)
#             serializer = ProductoSerializer(prod, data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 res = {'msg': 'Producto actualizado correctamente'}
#                 prod = JSONRenderer().render(res)
#                 return Response(prod)
#             res = {'msg': 'No se pudo actualizar el producto'}
#             prod = JSONRenderer().render(res)
#             return Response(prod)
#         res = {'msg': 'Producto no encontrado'}
#         prod = JSONRenderer().render(res)
#         return Response(prod)

# class TallaView(APIView):

#     def get(self, request):
#         talla = Talla.objects.all()
#         serializer = TallaSerializer(talla, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer  = TallaSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Talla agregada correctamente'}
#             return Response(res)
#         return Response({'msg': serializer.errors})
#     def delete(self, request):
#         talla = request.data
#         id = talla.get('id')
#         talla = Talla.objects.get(id=id)
#         talla.delete()
#         res = {'msg': 'Talla eliminada correctamente.'}
#         return Response(res)
#     def put(self, request):
#         talla = request.data
#         data = JSONParser().parse(talla)
#         id = data.get('id', None)
#         if id is not None:
#             talla = Talla.objects.get(id=id)
#             serializer = TallaSerializer(talla, data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 res = {'msg': 'Talla actualizada correctamente'}
#                 talla = JSONRenderer().render(res)
#                 return Response(talla)
#             res = {'msg': 'No se pudo actualizar la talla'}
#             talla = JSONRenderer().render(res)
#             return Response(talla)
#         res = {'msg': 'Talla no encontrado'}
#         talla = JSONRenderer().render(res)
#         return Response(talla)

# class CategoriaView(APIView):

#     def get(self, request):
#         categ = Categoria.objects.all()
#         serializer = CategoriaSerializer(categ, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer  = CategoriaSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Categoria agregada correctamente'}
#             return Response(res)
#         return Response({'msg': serializer.errors})
#     def delete(self, request):
#         categ = request.data
#         id = categ.get('id')
#         categ = Categoria.objects.get(id=id)
#         categ.delete()
#         res = {'msg': 'Categoria eliminada correctamente.'}
#         return Response(res)
#     def put(self, request):
#         categ = request.data
#         data = JSONParser().parse(categ)
#         id = data.get('id', None)
#         if id is not None:
#             categ = Categoria.objects.get(id=id)
#             serializer = CategoriaSerializer(categ, data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 res = {'msg': 'Categoria actualizada correctamente'}
#                 categ = JSONRenderer().render(res)
#                 return Response(categ)
#             res = {'msg': 'No se pudo actualizar la Categoria'}
#             categ = JSONRenderer().render(res)
#             return Response(categ)
#         res = {'msg': 'Categoria no encontrado'}
#         categ = JSONRenderer().render(res)
#         return Response(categ)


class ProductConcretGenericView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CategoriaConcretGenericView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class TallaConcretGenericView(generics.ListCreateAPIView):
    queryset = Talla.objects.all()
    serializer_class = TallaSerializer

class ProductDetailsGenericView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                                mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class CategoriaDetailsGenericView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                                mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class TallaDetailsGenericView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                                mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Talla.objects.all()
    serializer_class = TallaSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)