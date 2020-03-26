from datetime import datetime

import pytz

MOST_PREFERRED_ZONES = [
    'US/Arizona',
    'US/Pacific',
    'US/Mountain',
    'US/Central',
    'US/Eastern',
    'America/Los_Angeles',
    'America/Denver',
    'America/Chicago',
    'America/New_York',
    'Europe/London',
    'GMT',
    'UTC',
    'Europe/Paris',
    'Europe/Berlin',
    'Europe/Moscow',
    'Asia/Hong_Kong',
    'Asia/Shanghai',
    'Asia/Seoul',
    'Asia/Kolkata',
    'Australia/Sydney',
    'Pacific/Auckland',
]

PREFERRED_ZONES = [
    'Pacific/Midway',
    'Pacific/Honolulu',
    'US/Hawaii',
    'Pacific/Marquesas',
    'America/Anchorage',
    'US/Alaska',
    'America/Phoenix',
    'America/Vancouver',
    'Canada/Pacific',
    'America/Mexico_City',
    'Canada/Mountain',
    'America/Bogota',
    'America/Lima',
    'America/Panama',
    'Canada/Central',
    'America/Detroit',
    'America/Toronto',
    'America/Argentina/Buenos_Aires',
    'America/Argentina/San_Juan',
    'America/Santiago',
    'America/Sao_Paulo',
    'Canada/Newfoundland',
    'Atlantic/South_Georgia',
    'Atlantic/Cape_Verde',
    'Europe/Amsterdam',
    'Europe/Madrid',
    'Africa/Johannesburg',
    'Europe/Helsinki',
    'Europe/Bucharest',
    'Asia/Riyadh',
    'Europe/Istanbul',
    'Asia/Dubai',
    'Asia/Kabul',
    'Asia/Tehran',
    'Asia/Karachi',
    'Asia/Kathmandu',
    'Asia/Dhaka',
    'Asia/Yangon',
    'Asia/Bangkok',
    'Asia/Ho_Chi_Minh',
    'Asia/Jakarta',
    'Asia/Taipei',
    'Australia/Eucla',
    'Asia/Tokyo',
    'Australia/Darwin',
    'Pacific/Guam',
    'Australia/Adelaide',
    'Australia/Melbourne',
    'Pacific/Fiji',
    'Pacific/Wake',
    'Pacific/Chatham',
    'Pacific/Kiritimati',
]


def offset_to_timezone(offset):
    """ Convert output from JavaScript's getTimezoneOffset() to a timezone name.
    """
    offset = -offset / 60.0
    zones = []
    for tz in pytz.common_timezones:
        if (pytz.timezone(tz).utcoffset(datetime.now()).total_seconds() / 3600.0) == offset:
            zones.append(tz)
    
    zone = None
    for tz in zones:
        if tz in MOST_PREFERRED_ZONES:
            zone = tz
        if tz in PREFERRED_ZONES and not zone:
            zone = tz
    if zone:
        return zone
    elif isinstance(tz, list):
        return tz[0]
    else:
        return 'UTC'
