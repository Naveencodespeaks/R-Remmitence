from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
#from project.database.database import Base

Base = declarative_base()

class AdminUser(Base):
    __tablename__ = "admin"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(61))
    password = Column(Text)
    token = Column(Text)
    email = Column(String(161))
    mobile_no = Column(String(13))
    role_id = Column(Integer,default=1)
    #role_id = Column(Integer, ForeignKey('md_user_roles.role_id'), nullable=False)  # Ensure this matches UserRole.id
    #role_details = relationship('MdUserRole')
    #status_id = Column(Integer, ForeignKey('md_user_status.status_id'), nullable=False)
    #status_details = relationship('MdUserStatus', back_populates='users')


    class Config:
        orm_mode = True
