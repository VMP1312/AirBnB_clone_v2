#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review
        self.review = self.value()
        self.review.place_id = "656-ae4hetherthe54-6ertheeh1-erth4"
        self.review.user_id = "4253453hge4yh-asdfgsafgsg"
        self.review.text = "Casi me caigo xD"

    def test_place_id(self):
        """ """
        new = self.review
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.review
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.review
        self.assertEqual(type(new.text), str)
