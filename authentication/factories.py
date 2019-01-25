from faker import Faker
import random
from .models import Profile

fake = Faker('no_NO')

def UserFactory():
    return Profile.create(email=fake.email(),
                          first_name=fake.)