# Copyright 2015 Konstantinos Pachnis

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import getpass
import socket

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db.utils import IntegrityError


class Command(BaseCommand):

    help = 'Create a developer account'

    def handle(self, *args, **options):
        try:
            user = User.objects.create_user(
                getpass.getuser(),
                "{0}@{1}".format(getpass.getuser(), socket.getfqdn()),
                'dev'
            )
            user.is_superuser = True
            user.is_staff = True
            user.save()
        except IntegrityError:
            pass
