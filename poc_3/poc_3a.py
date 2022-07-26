"""
https://towardsdev.com/pydantic-validators-v-s-custom-data-type-2c65c6402829
"""

import pydantic

"""Simple regex pattern validation"""


class User(pydantic.BaseModel):
    first_name: str = "John"
    last_name: str = "Smith"
    phone_number: str = pydantic.Field(regex="^[+][0-9]{9,11}$")


print(User(phone_number="+123456789"))
# first_name='Jone' last_name='Smith' phone_number='+123456789'

try:
    User(phone_number="+12345678")
except pydantic.ValidationError as e:
    print(e)
# 1 validation error for User
# phone_number
# string does not match regex "^[+][0-9]{9,11}$" (type=value_error.str.regex; pattern=^[+][0-9]{9,11}$)
