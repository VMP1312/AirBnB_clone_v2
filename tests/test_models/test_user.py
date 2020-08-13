#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User
        self.user = self.value()
        self.user.first_name = "Victor"
        self.user.last_name = "paz"
        self.user.email = "efrnqwergo@adsfadsf.com"
        self.user.password = "12342546efgh"

    def tearDown(self):
        """ tearDown """
        try:
            os.remove("file.json")
        except Exception:
            pass
        if getenv('HBNB_TYPE_STORAGE') == "db":
            try:
                self.db.close()
            except Exception:
                pass

    def test_first_name(self):
        """ """
        self.assertEqual(type(self.user.first_name), str)

    def test_last_name(self):
        """ """
        self.assertEqual(type(self.user.last_name), str)

    def test_email(self):
        """ """
        self.assertEqual(type(self.user.email), str)

    def test_password(self):
        """ """
        self.assertEqual(type(self.user.password), str)


if __name__ == "__main__":
    unittest.main()
