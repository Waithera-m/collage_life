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

class CategoryModelTests(TestCase):

    """
    class facilitates the creation of automatic tests to monitor model behavior
    """
    def setUp(self):

        """
        method executes before each test
        """
        self.category = Category(category_name='vacation')

    def test_init(self):

        """
        method checks if model's objects are initialized properly
        """
        self.assertTrue(isinstance(self.category, Category))
    
    def test_save_category(self):

        """
        method tests if added category is saved
        """
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_update_category(self):

        """
        method tests if it is possible to update saved category
        """
        category = Category.objects.create(category_name="vacation")
        Category.objects.filter(pk=category.pk).update(category_name="outing")
        category.update_category()
        self.assertEqual(category.category_name, 'outing')
    
    def test_delete_category(self):

        """
        method checks if it is possible to delete save category
        """
        category = Category.objects.create(category_name="vacation")
        Category.objects.filter(pk=category.pk).delete()
        category.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)

class ImageModelTests(TestCase):

    """
    class facilitates the creation of tests to test Image model behavior
    """
    def setUp(self):
        """
        method runs before other tests
        """
        self.new_location = Location(location_name='Naivasha')
        self.new_location.save()

        self.image = Image(image_name="out", image_description="some description", location=self.new_location, pub_date="2020-05-22")
    
    def test_init(self):
        """
        method checks if objects are initialized properly
        """
        self.assertTrue(isinstance(self.image, Image))

    def test_save_image(self):
        """
        method tests model save functionality
        """
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
    
    def test_update_image(self):
        """
        method test if models updates saved image
        """
        self.new_location = Location(location_name='Naivasha')
        self.new_location.save()
        image = Image.objects.create(image_name="out", image_description='some description', location=self.new_location, pub_date='2020-05-22')
        Image.objects.filter(pk=image.pk).update(image_name='random')
        image.update_image()
        self.assertEqual(image.image_name, 'random')

    def test_delete_image(self):
        """
        methods checks delete functionality
        """
        self.new_location = Location(location_name='Naivasha')
        self.new_location.save()
        image = Image.objects.create(image_name="out", image_description='some description', location=self.new_location, pub_date='2020-05-22')
        Image.objects.filter(pk=image.pk).delete()
        image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_get_image_by_id(self):
        """
        method checks retrieval of image by id
        """
        
