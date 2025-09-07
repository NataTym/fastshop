from src.common.routes import BaseCrudPrefixes


class UserManagementRoutesPrefixes:
    user: str = '/user'


class UserRoutesPrefixes(BaseCrudPrefixes):
    address: str = '/address'
    detail: str = '/detail'
