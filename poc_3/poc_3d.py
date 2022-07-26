import pydantic
import pydantic.fields
import phonenumbers

"""Custom data type"""


class PhoneNumber(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate_phone_number

    @classmethod
    def validate_phone_number(cls, phone_number: str) -> str:
        try:
            parsed_phone = phonenumbers.parse(phone_number)
        except phonenumbers.NumberParseException:
            raise ValueError(
                f"Invalid phone number: {phone_number}. Validate by custom field."
            )

        if phonenumbers.is_valid_number(parsed_phone):
            return phone_number
        raise ValueError(
            f"Invalid phone number: {phone_number}. Validate by custom field."
        )


class User(pydantic.BaseModel):
    first_name: str = "Jone"
    last_name: str = "Smith"
    phone_number: PhoneNumber


class Company(pydantic.BaseModel):
    name: str = "My Company"
    phone_number: PhoneNumber


print(User(phone_number="+447823456901"))
# first_name='Jone' last_name='Smith' phone_number='+447823456901'

try:
    User(phone_number="+123456789")
except pydantic.ValidationError as e:
    print(e)
# 1 validation error for User
# phone_number
#   Invalid phone number: +123456789. Validate by custom field. (type=value_error)
