from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Profile, Signup
from .serializer import ProfileSerializer, SignupSerializer


class SignupView(APIView):

    def post(self, request):
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Signup successful"},
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class LoginView(APIView):

    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = Signup.objects.filter(
            username=username,
            password=password
        ).first()

        if user:
            return Response(
                {"message": "Login Success"},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"message": "Invalid User"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
class ProfileView(APIView):

    def get(self, request):
        try:
            username = request.GET.get('username')

            if not username:
                return Response({"error": "Username missing"}, status=400)

            profile, created = Profile.objects.get_or_create(username=username)

            serializer = ProfileSerializer(profile)
            return Response(serializer.data)

        except Exception as e:
            return Response({"error": str(e)}, status=500)

    def post(self, request):
        try:
            username = request.data.get('username')

            if not username:
                return Response({"error": "Username required"}, status=400)

            profile, created = Profile.objects.get_or_create(username=username)

            serializer = ProfileSerializer(profile, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Profile saved successfully",
                    "data": serializer.data
                })

            return Response(serializer.errors, status=400)

        except Exception as e:
            return Response({"error": str(e)}, status=500)