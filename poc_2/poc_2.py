"""
https://betterprogramming.pub/the-beginners-guide-to-pydantic-ba33b26cde89
"""

from datetime import datetime
from typing import List, Optional
from pydantic import (
    BaseModel,
    StrictBool,
    ValidationError,
    validator,
    NegativeInt,
    PositiveInt,
    conint,
    conlist,
    constr,
)


class User(BaseModel):
    id: int
    username: str
    password: str
    confirm_password: str
    alias = "anonymous"
    timestamp: Optional[datetime] = None
    friends: List[int] = []

    """Custom Validators"""

    @validator("id")
    def id_must_be_4_digits(cls, v):
        if len(str(v)) != 4:
            raise ValueError("must be 4 digits")
        return v

    @validator("confirm_password")
    def passwords_match(cls, v, values, **kwargs):
        if "password" in values and v != values["password"]:
            raise ValueError("passwords do not match")
        return v


data = {
    "id": "1234",
    "username": "wai foong",
    "password": "Password123",
    "confirm_password": "Password133",
    "timestamp": "2020-08-03 10:30",
    "friends": [1, "2", b"3"],
}

"""ValidationError"""

try:
    user = User(**data)
except ValidationError as e:
    print(e.json())

print(user)

"""Constrained Types"""


class Model(BaseModel):
    # minimum length of 2 and maximum length of 10
    short_str: constr(min_length=2, max_length=10)
    # regex
    regex_str: constr(regex=r"^apple (pie|tart|sandwich)$")
    # remove whitespace from string
    strip_str: constr(strip_whitespace=True)
    # value must be greater than 1000 and less than 1024
    big_int: conint(gt=1000, lt=1024)
    # value is multiple of 5
    mod_int: conint(multiple_of=5)
    # must be a positive integer
    pos_int: PositiveInt
    # must be a negative integer
    neg_int: NegativeInt
    # list of integers that contains 1 to 4 items
    short_list: conlist(int, min_items=1, max_items=4)


"""Strict Types"""


class StrictBoolModel(BaseModel):
    strict_bool: StrictBool
