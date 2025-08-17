from sqladmin import ModelView

from src.basket.model.sqlalchemy import (
    Basket,
    BasketLine,
)


ADMIN_CATEGORY = 'Basket'


class BasketAdmin(ModelView, model=Basket):
    column_list = [Basket.id, Basket.user_id, Basket.price, Basket.status]
    column_searchable_list = [Basket.user_id, Basket.price, Basket.status]
    icon = 'fa-solid fa-basket-shopping'
    category = ADMIN_CATEGORY


class BasketLineAdmin(ModelView, model=BasketLine):
    column_list = [BasketLine.id, BasketLine.basket_id, BasketLine.quantity, BasketLine.price]
    column_searchable_list = [BasketLine.basket_id, BasketLine.quantity, BasketLine.price]
    icon = 'fa-solid fa-chart-line'
    category = ADMIN_CATEGORY


def register_basket_admin_views(admin):
    admin.add_view(BasketAdmin)
    admin.add_view(BasketLineAdmin)