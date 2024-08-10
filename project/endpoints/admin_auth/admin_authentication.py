from datetime import datetime, timezone
from sqlalchemy import and_

from project.models.admin_user import MdUserRole,MdUserStatus, AdminUser
from . import APIRouter, Utility, SUCCESS, FAIL, EXCEPTION, Depends, Session, get_database_session, AuthHandler
from ...schemas.register import AdminRegister
import re
from ...schemas.login import Login


# APIRouter creates path operations for product module
router = APIRouter(
    prefix="/Admin",
    tags=["Admin Authentication"],
    responses={404: {"description": "Not found"}},
)

@router.post("/admin-register", response_description="Admin User Registration")
async def register(request: AdminRegister, db: Session = Depends(get_database_session)):
    try:
        user_name = request.user_name
        contact = request.mobile_no
        email = request.email
        password = request.password
        if user_name == '' or contact == '' or email == '' or password == '':
            return Utility.json_response(status=FAIL, message="Provide valid detail's", error=[], data={})
        if user_name is None or contact is None or email is None or password is None:
            return Utility.json_response(status=FAIL, message="Provide valid detail's", error=[], data={})
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(email_regex, email):
            return Utility.json_response(status=FAIL, message="Provide valid email", error=[], data={})
        # contact_digits = math.floor(math.log10(contact)) + 1
        if len(str(contact)) < 7 or len(str(contact)) > 13:
            return Utility.json_response(status=FAIL, message="Mobile number not valid. Length must be 7-13.",
                                         error=[], data={})
        user_with_email = db.query(AdminUser).filter(AdminUser.email == email).all()
        if len(user_with_email) != 0:
            return Utility.json_response(status=FAIL, message="Email already exists", error=[], data={})

        user_data = AdminUser( email=email,user_name=user_name, mobile_no=contact,password=AuthHandler().get_password_hash(str(password)))
        db.add(user_data)
        db.flush()
        db.commit()
        if user_data.id:
            return Utility.json_response(status=SUCCESS, message="User Registered Successfully", error=[],
                                         data={"user_id": user_data.id})
        else:
            return Utility.json_response(status=FAIL, message="Something went wrong11111", error=[], data={})
    except Exception as E:
        print(E)
        db.rollback()
        return Utility.json_response(status=FAIL, message="Something went wrong-----", error=[], data={})


@router.post("/login", response_description="Admin authenticated")
def admin_login(request: Login, db: Session = Depends(get_database_session)):
    try:
        email = request.email
        password = request.password
        user = db.query(AdminUser).filter(AdminUser.email == email, AdminUser.role_id == 1)
        if user.count() != 1:
            return Utility.json_response(status=FAIL, message="Invalid credential's", error=[], data={})
        if user.status_id !=2:
            msg = "Admin Profile is Inactive" if user.status_id == 3 else "Admin Profile is Deleted" if user.status_id == 4 else "Admin Profile is Inactive"
            return Utility.json_response(status=FAIL, message=msg, error=[], data={})
        verify_password = AuthHandler().verify_password(str(password), user.one().password)
        if not verify_password:
            return Utility.json_response(status=FAIL, message="Invalid credential's", error=[], data={})
        login_token = AuthHandler().encode_token(user.one().id)
        if not login_token:
            return Utility.json_response(status=FAIL, message="Token not assigned", error=[], data={})
        user.update({AdminUser.token: login_token}, synchronize_session=False)
        db.flush()
        db.commit()
        return Utility.dict_response(status=SUCCESS, message="Logged in successfully", error=[], data=user.one())
    except Exception as E:
        print(E)
        db.rollback()
        return Utility.json_response(status=EXCEPTION, message="Something went wrong", error=[], data={})
