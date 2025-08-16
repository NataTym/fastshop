from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from src.general.databases.postgres import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)  # noqa: A003
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    date_joined = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime, nullable=True)
    is_temporary = Column(Boolean, default=False)

    addresses = relationship('UserAddress', back_populates='user')
    basket = relationship('Basket', back_populates='user')

    def __str__(self):
        return self.email


class UserAddress(Base):
    __tablename__ = 'user_addresses'

    id = Column(Integer, primary_key=True, index=True)  # noqa: A003
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String, nullable=True)
    city = Column(String)
    street = Column(String)
    house = Column(String)
    apartment = Column(String, nullable=True)
    post_code = Column(String, nullable=True)
    floor = Column(String, nullable=True)
    additional_info = Column(String, nullable=True)

    user = relationship('User', back_populates='addresses')
