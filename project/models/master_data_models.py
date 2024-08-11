from sqlalchemy import Column, Integer,INT, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
#Base = declarative_base()
from  .base_model import BaseModel
class MdUserRole(BaseModel):
    __tablename__ = "md_user_roles"
    id = Column(Integer, primary_key=True, autoincrement=True)  # Ensure this is the primary key
    name = Column(Text, index=True)
    user = relationship('UserModel', back_populates='role_details')
    
    class Config:
        orm_mode = True

class MdUserStatus(BaseModel):
    __tablename__ = "md_user_status"
    id = Column(Integer, primary_key=True, autoincrement=True)  # Ensure this is the primary key
    name = Column(Text )
    user_status = relationship('UserModel', back_populates='status_details')
    
    
