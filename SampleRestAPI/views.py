from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import RestAPI
from .serializers import RestAPISerializer

class RestAPIListAppView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        restapi = RestAPI.objects,filter(user = request.user.id)
        serializer = RestAPISerializer(restapi, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        data = {

            'task' : request.data.get('task'),
            'completed' : request.data.get('completed'),
            'user' : request.user.id,

        }

        serializer = RestAPISerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errros, status=status.HTTP_400_BAD_REQUEST)
