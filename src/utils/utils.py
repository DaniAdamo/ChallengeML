from enum import IntEnum


class Roles(IntEnum):
    ADMIN = 1
    READER = 2
    GUEST = 3

    def __str__(self):
        return ROLES_TRANSLATOR[self]


ROLES_TRANSLATOR = {
    Roles.ADMIN: "Administrator",
    Roles.READER: "Reader",
    Roles.GUEST: "Guest"
}

