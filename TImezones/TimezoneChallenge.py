"""
Create a program that allows a user to select one of at most 9 timezones
from a menu. You can choose any of the timezones in the all_timezones list.

The program will then display the current time in that timezone,
as well as in local time and utc time.

Entering 0 as the choice will exit the program.

Display the time in formats suitable for the user of the program to understand,
and include the timezone name when showing the results.
"""

import datetime
import pytz
from pytz import reference

# grab utc time, create it in local timezone as well
utc_zone = pytz.timezone("UTC")
current_time = datetime.datetime.now().astimezone(utc_zone)

local_zone = reference.LocalTimezone()
local_time = current_time.astimezone(local_zone)

# provide the list of available timezones to choose from, including the first as the option to exit
available_timezones = ["Exit",
                       "America/Anchorage",
                       "America/Chicago",
                       "America/Denver",
                       "America/Los_Angeles",
                       "America/New_York",
                       "Pacific/Honolulu",
                       "Pacific/Midway",
                       "Pacific/Wake",
                       "Pacific/Guam"
                       ]

# create the keys for each menu option
menu_numbers = [i for i in range(len(available_timezones)+1)]

# create the dictionary as the zip of the two lists
menu = dict(zip(menu_numbers, available_timezones))

# provide the user the menu and request their input
print(menu)
choice = input("Please select one of the options above to display the current time in: ")


if int(choice) == 0:
    exit()
else:
    zone = pytz.timezone(menu.get(int(choice)))
    tz_time = current_time.astimezone(zone)

    print(f"The current time in the chosen timezone {zone} is {tz_time.strftime('%A %x %X %z')}.")
    print(f"The current time in the local timezone is {local_time.strftime('%A %x %X %z')}.")
    print(f"The current time in the UTC timezone is {current_time.strftime('%A %x %X %z')}.")
    exit()

