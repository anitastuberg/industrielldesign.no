import django
django.setup()

from models import Profile

users = Profile.objects.all()

for user in users:
    print(user.first_name)