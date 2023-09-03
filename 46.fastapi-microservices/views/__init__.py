__all__ = (
    "calc_router",
    "permissions_router",
    "users_router",
)

from .calc.views import router as calc_router
from .permissions.views import router as permissions_router
from .users.views import router as users_router
