"""
https://towardsdev.com/pydantic-validators-v-s-custom-data-type-2c65c6402829
"""
import pydantic
import phonenumbers

"""Reuse validators"""


def validate_phone_number(phone_number: str) -> str:
    try:
        parsed_phone = phonenumbers.parse(phone_number)
    except phonenumbers.NumberParseException:
        raise ValueError(
            f"Invalid phone number: {phone_number}. Validate by reused validator."
        )
    if phonenumbers.is_valid_number(parsed_phone):
        return phone_number
    raise ValueError(
        f"Invalid phone number: {phone_number}. Validate by reused validator."
    )


class User(pydantic.BaseModel):
    first_name: str = "Jone"
    last_name: str = "Smith"
    phone_number: str

    _phone_validator = pydantic.validator("phone_number", allow_reuse=True)(
        validate_phone_number
    )


class Company(pydantic.BaseModel):
    name: str = "My Company"
    phone_number: str

    _phone_validator = pydantic.validator("phone_number", allow_reuse=True)(
        validate_phone_number
    )


print(User(phone_number="+447823456901"))
# first_name='Jone' last_name='Smith' phone_number='+447823456901'

try:
    User(phone_number="+123456789")
except pydantic.ValidationError as e:
    print(e)
# 1 validation error for User
# phone_number
#   Invalid phone number: +123456789. Validate by reused validator. (type=value_error)

try:
    Company(phone_number="+123456789")
except pydantic.ValidationError as e:
    print(e)
# 1 validation error for Company
# phone_number
#   Invalid phone number: +123456789. Validate by reused validator. (type=value_error)
