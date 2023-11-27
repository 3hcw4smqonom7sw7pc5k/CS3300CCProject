from django.test import TestCase, SimpleTestCase
from django.contrib.auth.models import User
from event_app.models import Event
from django.urls import reverse
from django.contrib.auth.models import Group
from event_app.forms import EventForm
# Selenium WebDriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.conf import settings
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time

class EventModelTest(TestCase):
    def setUp(self):
        # Create a user and an event for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.event = Event.objects.create(event_name='Test Event', event_desc='This is a test event')

    def test_event_str(self):
        # Test that the _str_ method returns the event_name of the event
        self.assertEqual(str(self.event), 'Test Event')

#results from 20231125@1832MT
#(my_django_environment) C:\Users\Standard\CS3300CCProject\django_project>python manage.py test event_app.tests.EventModelTest
#Found 1 test(s).
#Creating test database for alias 'default'...
#System check identified no issues (0 silenced).
#.
#----------------------------------------------------------------------
#Ran 1 test in 0.929s
#
#OK
#Destroying test database for alias 'default'...

#200 is a success status code
#302 is an authentication required response
class UrlTest(SimpleTestCase):
#
    def test_url_exists_at_correct_location01(self):
        response = self.client.get("/accounts/register/")
        self.assertEqual(response.status_code, 200)
    def test_url_available_by_name01(self):
        response = self.client.get(reverse("register_page"))
        self.assertEqual(response.status_code, 200)
    def test_template_name_correct01(self):
        response = self.client.get(reverse("register_page"))
        self.assertTemplateUsed(response, "registration/register.html")
#
    def test_url_exists_at_correct_location02(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    def test_url_available_by_name02(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
    def test_template_name_correct02(self):
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "event_app/index.html")
#
    def test_url_exists_at_correct_location03(self):
        response = self.client.get("/events/")
        self.assertEqual(response.status_code, 302)
    def test_url_available_by_name03(self):
        response = self.client.get(reverse("events"))
        self.assertEqual(response.status_code, 302)
    def test_template_name_correct03(self):
        response = self.client.get(reverse("events"))
        self.assertTemplateNotUsed(response, "event_app/event_list.html")
#       ^assertTemplateNotUsed, No template for response
#
    def test_url_exists_at_correct_location04(self):
        response = self.client.get("/event/create_event/")
        self.assertEqual(response.status_code, 302)
    def test_url_available_by_name04(self):
        response = self.client.get(reverse("event_create"))
        self.assertEqual(response.status_code, 302)
    def test_template_name_correct04(self):
        response = self.client.get(reverse("event_create"))
        self.assertTemplateNotUsed(response, "event_app/event_form.html")
#       ^assertTemplateNotUsed, No template for response
#

#(my_django_environment) C:\Users\Standard\CS3300CCProject\django_project>python manage.py test event_app.tests.UrlTest
#Found 12 test(s).
#System check identified no issues (0 silenced).
#............
#----------------------------------------------------------------------
#Ran 12 tests in 0.061s
#
#OK

class StackOverFlowViewTest(TestCase):
    def test_call_view_deny_anonymous01(self):
        response = self.client.get(reverse("events"), follow=True)
        self.assertRedirects(response, "/accounts/login/?next=/events/")
        response = self.client.post(reverse("events"), follow=True)
        self.assertRedirects(response, "/accounts/login/?next=/events/")
    def test_call_view_deny_anonymous02(self):
        response = self.client.get(reverse("event_create"), follow=True)
        self.assertRedirects(response, "/accounts/login/?next=/event/create_event/")
        response = self.client.post(reverse("event_create"), follow=True)
        self.assertRedirects(response, "/accounts/login/?next=/event/create_event/")
    def setUp(self):
        # Create a user for testing, with Editor Role in some way
        # Cannot repeat this with a manual use of the editor_role, or the reader_role for that matter, strange, the groups are empty
        # These commands show an empty list, do not know how to apply the group
        #  group_user_dict = {group.name: group.user_set.values_list('id', flat=True) for group in Group.objects.all()}
        #  print(group_user_dict)
        self.user = User.objects.create_user(username='testuser', password='testpass')
#group = Group.objects.get(name='reader_role') 
#self.user.groups.add(group)
    def test_call_view_load01(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse("event_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, "event_app/event_form.html")
    def test_call_view_load02(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse("events"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "event_app/event_list.html")
    def test_is_invalid(self):
        form = EventForm(data={"event_name": "EventName", "event_desc": "EventDesc", "start_date": "2023-11-26 13:53:27", "end_date": "2023-11-26 13:53:27"})
        self.assertTrue(form.is_valid())
class SeleniumTestCase(StaticLiveServerTestCase):
    #@classmethod
    #def setUpClass(cls):
    #    super().setUpClass()
    #    options = webdriver.ChromeOptions()
    #    options.add_argument("--start-maximized")
    #    service = Service(f"{settings.BASE_DIR}/chromedriver")
    #    cls.driver = webdriver.Chrome(service=service, options=options)
    #    cls.driver.implicitly_wait(10)
    #@classmethod
    #def tearDownClass(cls):
    #    cls.driver.quit()
    #    super().tearDownClass()
    def test_basic_service():
        service = webdriver.ChromeService()
        driver = webdriver.Chrome(service=service)
        driver.quit()
    def test_driver_location(chromedriver_bin, chrome_bin):
        options = webdriver.ChromeOptions()
        options.binary_location = chrome_bin
        service = webdriver.ChromeService(executable_path=chromedriver_bin)
        driver = webdriver.Chrome(service=service, options=options)
        driver.quit()    
    def test_driver_port():
        service = webdriver.ChromeService(port=1234)
        driver = webdriver.Chrome(service=service)
        driver.quit()

#class AuthenticationFormTest(SeleniumTestCase):
#    def test_authentication_form(self):
#        # Create a user to login with
#        user = User.objects.create_user(
#            username="seleniumtest", password="selenium12345"
#        )
#        # Go to the login page
#        self.driver.get(self.live_server_url + "/login/")
#        # Find HTML elements
#        username = self.driver.find_element_by_id("username")
#        password_input = self.driver.find_element_by_id("password")
#        error_message = self.driver.find_element_by_css_selector(".error")
#        login_button = self.driver.find_element_by_id("btn-login")
#        # Ensure that the submit button is disabled
#        self.assertFalse(login_button.is_enabled())
#        # Type in a username that does exist but with the wrong password
#        email_input.clear()
#        email_input.send_keys(user.username)
#        login_button.click()
#        # Wait for request
#        time.sleep(0.5)
#        # Check that the correct error message is displayed
#        self.assertEqual(error_message.text, "You entered the wrong password.")
#        # Type in the correct email and password
#        password_input.clear()
#        password_input.send_keys("12345")
#        login_button.click()
#        # Wait for request
#        time.sleep(0.5)
#        # Check that the user is logged in
#        self.assertEqual(self.driver.current_url, self.live_server_url + "/events/")
        