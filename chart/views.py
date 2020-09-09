from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
# https://www.django-rest-framework.org/api-guide/views/
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'customers': 10
        }
        return render(request, 'charts.html', context)

# def get_data(request,*args, **kwargs):


def get_data(request):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data, safe=False)


class ChartData(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [qs_count, 23, 2, 3, 12, 2]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)
    # def get(self, request, format=None):
    #     qs_count = User.objects.all().count()
    #     labels = ['Users', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
    #     default_items = [qs_count, 1234, 1233, 32, 12, 2]
    #     data = {
    #         "labels": labels,
    #         "default": default_items,
    #         "users": User.objects.all().count(),
    #         "username": [user.username for user in User.objects.all()]
    #     }
    #     return Response(data)
