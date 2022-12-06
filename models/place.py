#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

association_table = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True,
                                 nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    reviews = relationship('Review', backref='place', cascade='delete')
    amenities = relationship('Amenity', secondary='place_amenity',
                             back_populates="place_amenities",
                             viewonly=False)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') != 'db':

        @property
        def reviews(self):
            """get a list of all related review instances
            with review.places_id = to the current place.id
            """
            reviews_list = []

            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        @property
        def amenities(self):
            """get a list of all related amenity instances
            with amenity.id = to the current self amenity ids
            """
            amenities_list = []

            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, obj):
            """Function that handles append method for adding an amenity"""
            if type(obj) == Amenity:
                self.amenities_ids.append(obj.id)
