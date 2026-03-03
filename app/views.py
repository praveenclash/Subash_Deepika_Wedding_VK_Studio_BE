from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Wedding
from .serializers import WeddingSerializer


class WeddingAPIView(APIView):

    def get(self, request, pk=None):
        # If ID is provided → single detail
        if pk:
            try:
                wedding = Wedding.objects.get(pk=pk)
                serializer = WeddingSerializer(wedding)
                return Response(serializer.data)
            except Wedding.DoesNotExist:
                return Response(
                    {"error": "Wedding not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

        # If no ID → return all data
        weddings = Wedding.objects.all()
        serializer = WeddingSerializer(weddings, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = WeddingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
