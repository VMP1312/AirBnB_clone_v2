#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place
        self.place = self.value()
        self.place.city_id = "3145-0efrgthe"
        self.place.user_id = "4334521-d34h5ycba"
        self.place.name = "Casita"
        self.place.description = "yu nou babe"
        self.place.number_rooms = 1
        self.place.number_bathrooms = 1
        self.place.max_guest = 3
        self.place.price_by_night = 15
        self.place.latitude = 123450.02345
        self.place.longitude = 1245670.45674567
        self.place.amenity_ids = ["1334524-wt5425gsdfgh235"]

    def test_city_id(self):
        """ """
        new = self.place
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.place
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.place
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.place
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.place
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.place
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.place
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.place
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.place
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.place
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.place
        self.assertEqual(type(new.amenity_ids), list)


if __name__ == "__main__":
    unittest.main()
