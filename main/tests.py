from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_name_and_class_are_set_correctly_in_main_template(self):
        name = "Muhammad Daffa Grahito Triharsanto"
        class_name = "PBP A"

        response = Client().get('/main/', {'name': name, 'class': class_name})

        self.assertContains(response, name)
        self.assertContains(response, class_name)