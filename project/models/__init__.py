
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
#from project.database.database import Base 
#from .admin_user import MdUserRole,MdUserStatus
from .master_data_models import UserRole, UserStatus 
from .user import User
from .admin_user import AdminUser

