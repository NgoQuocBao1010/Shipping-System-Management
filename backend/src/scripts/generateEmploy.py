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
    """Generate a Vietnamese name"""
    gender = random.choice([GIRLS, BOYS])

    firstName = random.choice(gender.get("FIRST_NAMES"))
    midName = random.choice(gender.get("MIDDLE_NAMES"))
    lastName = random.choice(gender.get("LAST_NAMES"))

    return " ".join([firstName, midName, lastName])


def emailGenerator(fullName, mode="user"):
    """Generate an email from a fullname"""
    fullName = unidecode.unidecode(fullName)  # Remove accent from text
    words = fullName.split(" ")

    name = "".join([word[0].lower() for word in words[:-1]])
    name += words[-1].lower()

    idLength = 4 if mode == "user" else 3
    userId = shortuuid.ShortUUID(alphabet="01345678").random(length=idLength)

    email = (
        f"{name}{userId}@gmail.com"
        if mode == "user"
        else f"{name}K{userId}@kaz.company.com"
    )

    return email


def phoneGenerator():
    openings = ["093", "077", "094"]
    rest = shortuuid.ShortUUID(alphabet="01345678").random(length=7)

    return random.choice(openings) + rest


def addressGenerator():
    streetNames = ["Nguyễn Văn Cừ", "Mạc Thiên Tích", "Quang Trung"]
    district_n_wards = [
        (919, 31189),
        (917, 31153),
        (916, 31117),
        (918, 31171),
        (916, 31149),
    ]

    homeId = random.randint(1, 200)

    address = f"Số {homeId} đường {random.choice(streetNames)}"
    return (address, *random.choice(district_n_wards))


def createUser(length=5):
    for _ in range(length):
        name = nameGenerator()
        email = emailGenerator(name)
        password = "kaz123"
        phone = phoneGenerator()

        user = User.objects.create_user(email=email, password=password)

        address, districtId, wardId = addressGenerator()
        profile = Profile.objects.get(user=user)
        profile.fullName = name
        profile.phone = phone
        profile.address = address
        profile.districtId = districtId
        profile.wardId = wardId

        profile.save()


def updateDriverLicense():
    drivers = Profile.objects.filter(user__admin=False, user__staff=True)

    for driver in drivers:
        license = shortuuid.ShortUUID(alphabet="01345678").random(length=8)
        driver.driverLicense = license
        driver.save()


def run():
    createUser(length=10)
    # print("NO")
