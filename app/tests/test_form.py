from django.test import SimpleTestCase
from app.forms import CustomerRegistrationForm

class testForms(SimpleTestCase):
    def text_customRef_form(self):
        form=CustomerRegistrationForm(date=
        {
            'username':'admin',
            'password1':'hello',
            'password2':'hello',
            'Email':'gowrav@gmail.com',
            'Number':'7999524134'
        })

        self.assertTrue(form.is_valid())

    def testForms_noData(self):
        form=CustomerRegistrationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),5)

