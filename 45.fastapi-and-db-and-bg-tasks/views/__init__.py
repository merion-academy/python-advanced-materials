__all__ = (
    "calc_router",
    "users_router",
)

from .calc.views import router as calc_router
from .users.views import router as users_router
