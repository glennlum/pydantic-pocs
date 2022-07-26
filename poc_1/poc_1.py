"""
https://pydantic-docs.helpmanual.io/
"""

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError

"""Pydantic data structure"""


class User(BaseModel):
    id: int
    name = "John Doe"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2019-06-01 12:22",
    "friends": [1, 2, "3"],
}
user = User(**external_data)
print(user.id)
# > 123
print(repr(user.signup_ts))
# > datetime.datetime(2019, 6, 1, 12, 22)
print(user.friends)
# > [1, 2, 3]
print(user.dict())
"""
{
    'id': 123,
    'signup_ts': datetime.datetime(2019, 6, 1, 12, 22),
    'friends': [1, 2, 3],
    'name': 'John Doe',
    'hello': 'hi',
}
"""

try:
    User(signup_ts="broken", friends=[1, 2, "not number"])
except ValidationError as e:
    print(e.json())

"""
[
  {
    "loc": [
      "id"
    ],
    "msg": "field required",
    "type": "value_error.missing"
  },
  {
    "loc": [
      "signup_ts"
    ],
    "msg": "invalid datetime format",
    "type": "value_error.datetime"
  },
  {
    "loc": [
      "friends",
      2
    ],
    "msg": "value is not a valid integer",
    "type": "type_error.integer"
  }
]
"""
