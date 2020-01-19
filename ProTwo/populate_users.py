import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'ProTwo.settings')

import django
django.setup()

from AppTwo.models import User
from faker import Faker

Fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name = Fakegen.name().split()
        fake_first_name=fake_name[0]
        fake_last_name=fake_name[1]
        fake_email=Fakegen.email()

        #new entry
        user = User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name, email=fake_email)[0]

if __name__ == '__main__':
    print('POPULATING DATABASES')
    populate(20)
    print('complete')
