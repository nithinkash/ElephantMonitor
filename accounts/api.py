from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics, permissions, mixins

from .serializer import RegisterSerializer, UserSerializer


class SimpleApi(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {'message': "Elephant tracker initated"}
        return Response(content)


# Register API
class RegistrationApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })