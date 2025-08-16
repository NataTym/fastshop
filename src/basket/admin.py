from sqladmin import ModelView

from src.basket.model.sqlalchemy import (
    Basket,
)


ADMIN_CATEGORY = 'Basket'


class BasketAdmin(ModelView, model=Basket):
    column_list = [Basket.id, Basket.user_id, Basket.price, Basket.status]
    column_searchable_list = [Basket.user_id, Basket.price, Basket.status]
    icon = 'fa-solid fa-basket-shopping'
    category = ADMIN_CATEGORY


def register_basket_admin_views(admin):
    admin.add_view(BasketAdmin)