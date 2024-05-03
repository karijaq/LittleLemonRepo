from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import menuSerializer
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create( Title="Soup", Price= 4.50, Inventory= 7)
        Menu.objects.create( Title ="Salad", Price=3.50, Inventory=10)

    def test_getall(self):

        client = APIClient()

        # Make a GET request to retrieve all Menu objects
        response = client.get('/restaurant/menu/')
        menuItems = Menu.objects.all()


        # Serialize the retrieved Menu objects using the serializer
        serializer = menuSerializer(menuItems, many=True)
        print (response.data)

        # Assert that the serialized data matches the response data
        self.assertEqual(response.data, serializer.data)
