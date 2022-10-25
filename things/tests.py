from django.test import TestCase
from django import forms
from things.forms import ThingForm

class TestThingForm(TestCase):
    def setUp(self):
        self.form_input = {
            'name': 'charlie',
            'description': 'moderately useful',
            'quantity': 8
        }

    def test_form_has_required_fields(self):
        form = ThingForm()
        self.assertIn('name', form.fields)
        self.assertIn('description', form.fields)
        self.assertIn('quantity', form.fields)

    def test_form_accepts_valid_data_entry(self):
        form = ThingForm(data = self.form_input)
        self.assertTrue(form.is_valid())
