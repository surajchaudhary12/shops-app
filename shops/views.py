# shops/views.py

from rest_framework import generics, status
from rest_framework.response import Response
from .models import Shop
from .serializers import ShopSerializer, ShopRegistrationSerializer
from rest_framework.views import APIView
from math import radians, cos, sin, asin, sqrt

class ShopRegistrationView(generics.CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopRegistrationSerializer

class UserSearchView(APIView):
    def get(self, request, format=None):
        try:
            user_lat = float(request.query_params.get('latitude'))
            user_lon = float(request.query_params.get('longitude'))
        except (TypeError, ValueError):
            return Response({"error": "Invalid or missing latitude/longitude."},
                            status=status.HTTP_400_BAD_REQUEST)
        
        shops = Shop.objects.all()
        shops_with_distance = []

        for shop in shops:
            distance = self.haversine(user_lon, user_lat, shop.longitude, shop.latitude)
            shops_with_distance.append({
                'id': shop.id,
                'name': shop.name,
                'latitude': shop.latitude,
                'longitude': shop.longitude,
                'distance_km': distance
            })

        # Sort shops by distance
        sorted_shops = sorted(shops_with_distance, key=lambda x: x['distance_km'])
        return Response(sorted_shops, status=status.HTTP_200_OK)

    def haversine(self, lon1, lat1, lon2, lat2):
        """
        Calculate the great circle distance between two points 
        on the earth (specified in decimal degrees)
        """
        # Convert decimal degrees to radians 
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        # Haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 6371  # Radius of earth in kilometers
        return c * r