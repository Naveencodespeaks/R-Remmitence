from fastapi import APIRouter
from project.endpoints.user_auth import user_authentication
from project.endpoints.admin_auth import admin_authentication

router = APIRouter()

# --------------------Admin Routing---------------------
router.include_router(user_authentication.router)

# --------------------Admin Routing--------------------
router.include_router(admin_authentication.router)
