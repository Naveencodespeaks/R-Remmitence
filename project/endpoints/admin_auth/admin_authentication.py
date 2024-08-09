from project.models.user import User
from . import APIRouter, Utility, SUCCESS, FAIL, EXCEPTION, Depends, Session, get_database_session, AuthHandler
from ...schemas.login import Login

# APIRouter creates path operations for product module
router = APIRouter(
    prefix="/Admin",
    tags=["Admin Authentication"],
    responses={404: {"description": "Not found"}},
)


@router.post("/login", response_description="Client authenticated")
def client_login(request: Login, db: Session = Depends(get_database_session)):
    try:
        email = request.email
        password = request.password
        user = db.query(User).filter(User.email == email, User.is_delete == '0', User.is_active == '1',
                                        User.user_type_term == 'Client')
        if user.count() != 1:
            return Utility.json_response(status=FAIL, message="Invalid credential's", error=[], data={})
        verify_password = AuthHandler().verify_password(str(password), user.one().password)
        if not verify_password:
            return Utility.json_response(status=FAIL, message="Invalid credential's", error=[], data={})
        login_token = AuthHandler().encode_token(user.one().client_id)
        if not login_token:
            return Utility.json_response(status=FAIL, message="Token not assigned", error=[], data={})
        user.update({User.token: login_token}, synchronize_session=False)
        db.flush()
        db.commit()
        return Utility.dict_response(status=SUCCESS, message="Logged in successfully", error=[], data=user.one())
    except Exception as E:
        print(E)
        db.rollback()
        return Utility.json_response(status=EXCEPTION, message="Something went wrong", error=[], data={})
