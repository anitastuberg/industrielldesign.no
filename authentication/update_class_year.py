from models import Profile
import django
django.setup()


users = Profile.objects.all()

for user in users:
    print(user.first_name)
