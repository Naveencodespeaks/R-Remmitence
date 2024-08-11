from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
#from project.database.database import Base

#Base = declarative_base()
from .base_model import BaseModel

class AdminUser(BaseModel):
    __tablename__ = "admin"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(61))
    password = Column(Text)
    login_token = Column(Text)
    token = Column(Text)
    email = Column(String(161))
    mobile_no = Column(String(13))
    role_id = Column(Integer, ForeignKey('md_user_roles.id'), nullable=False)  # Ensure this matches UserRole.id
    role = relationship('MdUserRole', back_populates='admin_user')

    status_id = Column(Integer, ForeignKey('md_user_status.id'),  nullable=False)
    status_details = relationship('MdUserStatus', back_populates='admin_status')


    class Config:
        orm_mode = True
