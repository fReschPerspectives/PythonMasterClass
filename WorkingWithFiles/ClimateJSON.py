import json
import urllib.request

climate_data_web_source = "https://www.ncdc.noaa.gov/cag/global/time-series/globe/land_ocean/1/4/1880-2022/data.json"
climate_data_source = "data/temperature_data.json"

with open(climate_data_source, encoding="utf-8", mode="r") as data:
    anomalous_data = json.load(data)

print(anomalous_data.keys())

print(anomalous_data["data"].keys())



"""
The json can actually be accessed directly from the stream of web data.
"""

with urllib.request.urlopen(climate_data_web_source) as json_stream:
    data = json_stream.read().decode("utf-8")
    anomalous_stream_data = json.loads(data)

for key, value in anomalous_stream_data["data"].items():
    print(f"Year: {key}, Anomaly: {value}")
