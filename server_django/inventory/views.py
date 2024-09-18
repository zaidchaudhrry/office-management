from rest_framework.generics import ListCreateAPIView
from .models import Product
from .serializers import ProductSerializer

# This view will handle GET (list) and POST (create) requests for products
class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()  # Retrieve all products from the database
    serializer_class = ProductSerializer
