#!/usr/bin/python
from pytz import timezone
from datetime import datetime
import requests

api_key = "GOOGLE_API_KEY"
local_format = "%Y-%m-%d %H:%M:%S"

class time_zone_converter:
    def _build_url(self, lat, lon):
        return "https://maps.googleapis.com/maps/api/timezone/json?location={},{}&timestamp=1331161200&key={}".format(lat, lon, api_key)

    def _get_timezone(self, lat, lon):
        r = requests.get(self._build_url(lat, lon))
        return timezone(r.json().get('timeZoneId'))

    def normalize_time(self, lat, lon, timestamp):
        the_timezone = self._get_timezone(lat, lon)
        return datetime.fromtimestamp(timestamp, the_timezone).strftime(local_format)

if __name__ == "__main__":
    print(time_zone_converter().normalize_time(40.72, -74, 1456790400.0))