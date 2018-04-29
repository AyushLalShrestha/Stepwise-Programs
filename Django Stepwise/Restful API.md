

# Expose an API from django using djangorestframework i.e rest_framework

## Make a serializer.py file in the app : 
``` from rest_framework import serializers
 from models import Customer, Product, Sales
 
 class SalesSerializer(serializers.ModelSerializer):
	product = ProductSerializer() //will be in this same file
	customer = CustomerSerializer() //will be in this same file
	
	class Meta:
		model = Sales
		field = ('id', 'product', 'customer') //  fields = '__all__'
```
-----------------------------------------------------------------------------------------------------
## In the views.py file : 
``` from rest_framework import generics
 from serializer import SalesSerializer
 from models import Sales
 
 class SalesList(generics.ListCreateAPIView):
 # class SalesList(viewsets.ModelViewSet):
	queryset = Sale.objects.all()
	serializer_class = SalesSerializer 
	
	#queryset = Sale.objects.all()
    	#serializer_class = SaleSerializer
    	#permission_classes = (IsAdminUser,)
``` 
-----------------------------------------------------------------------------------------------
## In urls.py file :
``` from rest_framework.urlpatterns import format_suffix_patterns
 from . import views
	
	urlpatterns = {
		url(r'^api/$', views.SalesList.as_view(), name = "salesrest"),
	}
	
urlpatterns = format_suffix_patterns(urlpatterns)	
```


 
 
