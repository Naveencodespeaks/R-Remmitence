from pydantic import BaseModel, EmailStr, constr, field_validator
import phonenumbers
from phonenumbers import NumberParseException, is_valid_number


class Register(BaseModel):
    email: str
    password: str
    mobile_no: str
    contact: int

class AdminRegister(BaseModel):
    email: EmailStr
    mobile_no: str| int
    user_name: str| int #constr(min_length=3, max_length=50)
    password: str| int #constr(min_length=8)

    '''
    @field_validator('passworddd')
    def password_must_contain_digit(cls, value):
        """Ensure the password contains at least one digit."""
        if not any(char.isdigit() for char in value):
            raise ValueError('Password must contain at least one digit')
        return value
    
    @field_validator('mobile_no---')
    def validate_mobile_no(cls, value):
        """Validate phone number for all countries."""
        try:
            # Parse the phone number
            phone_number = phonenumbers.parse(value, None)  # None uses the default region
            
            if not is_valid_number(phone_number):
                raise ValueError("Invalid phone number")
            
            return value
        except NumberParseException:
            raise ValueError("Invalid phone number format")
    '''

