#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
import os
import models

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id',
                             String(60),
                             ForeignKey('places.id'),
                             nullable=False),
                      Column('amenity_id',
                             String(60),
                             ForeignKey('amenities.id'),
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    name = Column(String(128), nullable=False)

    description = Column(String(128), nullable=True)

    number_rooms = Column(Integer, default=0, nullable=False)

    number_bathrooms = Column(Integer, default=0, nullable=False)

    max_guest = Column(Integer, default=0, nullable=False)

    price_by_night = Column(Integer, default=0, nullable=False)

    latitude = Column(Float, nullable=True)

    longitude = Column(Float, nullable=True)

    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship("Amenity", secondary=place_amenity)

    amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """Get a list of all linked Reviews."""
            reviews = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    reviews.append(review)
            return reviews

        @property
        def amenities(self):
            """Get/set linked Amenities."""
            amenities = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenities.append(amenity)
            return amenities

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
