import os

# configuring the settings for the project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

from AppTwo.models import User
from faker import Faker

fake = Faker()


def populate_user_model(N=10):
    for data in range(N):
        fake_first_name = fake.first_name()
        fake_last_name = fake.last_name()
        fake_email = fake.email()

        user = User.objects.get_or_create(first_name=fake_first_name,
                                          last_name=fake_last_name,
                                          email=fake_email)[0]

if __name__ == '__main__':
    print('populating db ...')
    populate_user_model()
    print('populating complete')
