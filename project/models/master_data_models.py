from sqlalchemy import Column, Integer,INT, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class MdUserRole(Base):
    __tablename__ = "md_user_roles"
    role_id = Column(Integer, primary_key=True, autoincrement=True)  # Ensure this is the primary key
    name = Column(String(161), index=True)
    #role_users = relationship('User', back_populates='role_details')
    status= Column(Text )

    class Config:
        orm_mode = True


class MdUserStatus(Base):
    __tablename__ = "md_user_status"    
    status_id = Column(Integer, primary_key=True, autoincrement=True)  # Ensure this is the primary key
    name = Column(Text )
    #users = relationship('User', back_populates='status_details')
    status= Column(Text )
