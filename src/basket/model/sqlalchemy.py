from src.basket.model.enums import Status

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    DECIMAL,
    Enum
)

from sqlalchemy.orm import relationship

from src.general.databases.postgres import Base

from src.users.models.sqlalchemy import User

class Basket(Base):
    __tablename__ = 'baskets'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    price = Column(DECIMAL)
    status = Column(Enum(Status))

    user = relationship('User', back_populates='basket')