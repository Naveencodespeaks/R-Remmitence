from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, TIMESTAMP, CHAR, VARCHAR, DATETIME, INT, TEXT

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    #user_id = Column(CHAR(38), nullable=False)
    id = Column(INT, primary_key=True, index=True,autoincrement=True)
    client_id = Column(CHAR(38))
    association_id = Column(CHAR(38))
    association_type_term = Column(VARCHAR(39))
    user_name = Column(VARCHAR(61))
    password = Column(TEXT)
    token = Column(TEXT)
    status_term = Column(VARCHAR(39))
    profile_pic = Column(VARCHAR(361))
    display_name = Column(VARCHAR(61))
    created_on = Column(DATETIME)
    created_by = Column(CHAR(39))
    updated_on = Column(DATETIME)
    updated_by = Column(CHAR(39))
    email = Column(CHAR(161))
    mobile_no = Column(CHAR(13))
    is_active = Column(String(1))
    is_delete = Column(String(1))
    update_log = Column(TIMESTAMP, default=datetime.now())    
    user_type_term = Column(VARCHAR(39))
    is_default = Column(String(1))
    is_it_admin = Column(String(1))
    forgot_password_token = Column(TEXT)

    class Config:
        orm_mode = True
