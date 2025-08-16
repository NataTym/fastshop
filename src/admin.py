from src.users.admin import register_hr_admin_views
from src.basket.admin import register_basket_admin_views


def register_admin_views(admin):
    register_hr_admin_views(admin=admin)
    register_basket_admin_views(admin=admin)
