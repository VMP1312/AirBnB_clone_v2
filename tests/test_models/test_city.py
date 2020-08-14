#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City
        self.city = self.value()
        self.city.name = "Santiago de Cali"
        self.city.state_id = "adfgrg23-245g78f278g"

    def test_state_id(self):
        """ """
        new = self.city
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.city
        self.assertEqual(type(new.name), str)
