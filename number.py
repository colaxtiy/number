import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from colorama import Fore
import os
f = Fore
fb = f.BLUE
fr = f.RED
frs = f.RESET
fg = f.GREEN
os.system("clear")
print(fr+"""
 _   _                 _                   
| \ | |_   _ _ __ ___ | |__   ___ _ __  
|  \| | | | | '_ ` _ \| '_ \ / _ \ '__/
| |\  | |_| | | | | | | |_) |  __/ |
|_| \_|\__,_|_| |_| |_|_.__/ \___|_|

Coded By Securist0x01

""")
numbers = input(fb+"Enter Mobile Number with Country code ==> ")
numbers = phonenumbers.parse(numbers)
print(timezone.time_zones_for_number(numbers))
print(carrier.name_for_number(numbers, "en"))
print(geocoder.description_for_number(numbers, "en"))
print(fg+"Valid Mobile Number ==> ",phonenumbers.is_valid_number(numbers))
print(fg+"Checking possibility of Number ==> ", phonenumbers.is_possible_number(numbers))
