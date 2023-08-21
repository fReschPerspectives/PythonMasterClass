import pytz
import datetime

country = 'Europe/Moscow'

tz_to_display = pytz.timezone(country)
moscow_local_time = datetime.datetime.now(tz=tz_to_display)

print(f"The time in {country} is {moscow_local_time}.")
print(f"The time in UTC is {datetime.datetime.utcnow()}.")


for z in sorted(pytz.country_names):
    print(f"{z}: {pytz.country_names[z]}", end=": \n")
    if z in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[z]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print(f"\t\t{zone}: {local_time}")
    else:
        print("No timezone defined")
