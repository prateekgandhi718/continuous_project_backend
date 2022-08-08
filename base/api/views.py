from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# import the factory model now.
from base.models import Factory
#importing the serializer as well
from .serializers import FactorySerializer, ProductSerializer

#importing the product model.
from base.models import Product

@api_view(['GET'])
def getRoutes(request):
    routes = ['GET endpoint at /api that is home!',
              'GET endpoint at /api/factories to get the factories',
              'GET endpoint at /api/factories/:id to get details of a particular factory']
    return Response(routes)

@api_view(['GET', 'POST'])
def getFactories(request):
    if request.method == 'GET':
        factories = Factory.objects.all()
        serializer = FactorySerializer(factories, many = True) #this will be query set, therefore to display as JSON, use serializer. many=True just serializes all the objects
        return Response(serializer.data) 
    elif request.method == 'POST':
        serializer = FactorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def getAFactory(request, factoryId):
    if request.method == 'GET':
        try:
            products = Product.objects.filter(factory = factoryId)
        except Product.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def getAProduct(request, factoryId, productId):
    try:
        product = Product.objects.filter(factory = factoryId).get(id = productId)
    except Product.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product, many = False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        serializer = ProductSerializer(product, many=False)
        product.delete()
        return Response(serializer.data, status = status.HTTP_204_NO_CONTENT)
        


