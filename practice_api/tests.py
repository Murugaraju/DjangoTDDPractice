from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Dog
from .serializers import DogModelSerializer
# Create your tests here.





class DogModelViewSetTest(APITestCase):

    def setup(self):
        Dog.objects.create(name='sample1')

        


        return super().setup()

    
    def test_list_of_dogs_end_point(self):


        res=self.client.get(reverse('dog-list'))

        l=Dog.objects.all().count()
        

        self.assertEqual(l,len(res.data))





