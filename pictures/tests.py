from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.
class LocationModelTests(TestCase):

    """
    class facilitates the creation of tests to test location model behavior
    """
    def setUp(self):

        """
        method defines the instructions to be executed before each test
        """
        self.location = Location(location_name='Naivasha')
    
    def test_init(self):

        """
        test checks if model's object is initialized properly
        """
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):

        """
        test checks if entered location is saved
        """
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_update_location(self):

        """
        method checks if it is possible to update location name
        """
        location = Location.objects.create(location_name="Naivasha")
        Location.objects.filter(pk=location.pk).update(location_name="Nakuru")
        location.update_location()
        self.assertEqual(location.location_name, 'Nakuru')

    def test_delete_location(self):

        """
        methods tests if one can delete a location
        """
        location = Location.objects.create(location_name="Naivasha")
        Location.objects.filter(pk=location.pk).delete()
        location.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)


