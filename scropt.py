# -*- coding: utf-8 -*-

import os,sys

path = os.path.normpath(os.path.join(os.getcwd(), '..'))
sys.path.append(path)
from django.core.management import setup_environ
import main.settings

setup_environ(main.settings)

from addressprogram.models import AdvertisingSpace
from addressprogram.utils import take_advertising_space_prints

take_advertising_space_prints(AdvertisingSpace.objects.all())
