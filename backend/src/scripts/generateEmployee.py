from django.contrib.auth import get_user_model

from account.models import Profile

import random
import unidecode, shortuuid
from pprint import pprint

User = get_user_model()

GIRLS = {
    "FIRST_NAMES": ["Ngô Thị", "Nguyễn Thị", "Trần Thị", "Lê Thị"],
    "LAST_NAMES": ["Mận", "Mai", "Linh", "Đan"],
    "MIDDLE_NAMES": ["Phương", "An", "Khánh", "Lê", "Tiểu"],
}

BOYS = {
    "FIRST_NAMES": ["Ngô", "Nguyễn", "Trần", "Huỳnh"],
    "LAST_NAMES": ["Bảo", "Trọng", "Thuận", "Hào", "Vinh"],
    "MIDDLE_NAMES": ["Quốc", "An", "Anh", "Minh", "Hoàng", "Hoàng Văn", "Hồng Quốc"],
}


def nameGenerator():
    gender = random.choice([GIRLS, BOYS])

    firstName = random.choice(gender.get("FIRST_NAMES"))
    midName = random.choice(gender.get("MIDDLE_NAMES"))
    lastName = random.choice(gender.get("LAST_NAMES"))

    return " ".join([firstName, midName, lastName])


def emailGenerator(fullName):
    """Generate an email from a fullname"""
    fullName = unidecode.unidecode(fullName)  # Remove accent from text
    words = fullName.split(" ")

    name = "".join([word[0].lower() for word in words[:-1]])
    name += words[-1].lower()
    userId = shortuuid.ShortUUID(alphabet="01345678").random(length=3)

    email = f"{name}K{userId}@kaz.company.com"

    return email


def phoneGenerator():
    openings = ["093", "077", "094"]
    rest = shortuuid.ShortUUID(alphabet="01345678").random(length=7)

    return random.choice(openings) + rest


def createManager(length=3):
    for i in range(length):
        name = nameGenerator()
        email = emailGenerator(name)
        password = "kaz123"
        phone = phoneGenerator()

        # manager = User.objects.create_superuser(email=email, password=password)

        pprint(
            {
                "name": name,
                "email": email,
                "password": password,
                "phone": phone,
            }
        )


def run():
    createManager()
