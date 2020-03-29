from datetime import datetime

import pytz

ZONES = {
    '0_0': 'Etc/UTC',
    '0_60': 'Europe/London',
    '60_60': 'Africa/Lagos',
    '60_120': 'Europe/Paris',
    '120_120': 'Africa/Johannesburg',
    '120_180': 'Europe/Helsinki',
    '180_180': 'Africa/Nairobi',
    '210_270': 'Asia/Tehran',
    '240_240': 'Asia/Dubai',
    '270_270': 'Asia/Kabul',
    '300_300': 'Asia/Karachi',
    '330_330': 'Asia/Kolkata',
    '345_345': 'Asia/Kathmandu',
    '360_360': 'Asia/Urumqi',
    '390_390': 'Asia/Yangon',
    '420_420': 'Asia/Ho_Chi_Minh',
    '480_480': 'Asia/Shanghai',
    '525_525': 'Australia/Eucla',
    '540_540': 'Asia/Seoul',
    '570_570': 'Australia/Darwin',
    '570_630': 'Australia/Adelaide',
    '600_600': 'Australia/Brisbane',
    '600_660': 'Australia/Sydney',
    '630_660': 'Australia/Lord_Howe',
    '660_660': 'Pacific/Norfolk',
    '720_720': 'Pacific/Wake',
    '720_780': 'Pacific/Auckland',
    '765_825': 'Pacific/Chatham',
    '780_780': 'Pacific/Enderbury',
    '780_840': 'Pacific/Tongatapu',
    '840_840': 'Pacific/Kiritimati',
    '-60_0': 'Atlantic/Azores',
    '-60_-60': 'Atlantic/Cape_Verde',
    '-120_-120': 'America/Noronha',
    '-180_-180': 'America/Sao_Paulo',
    '-180_-120': 'America/Miquelon',
    '-210_-150': 'America/St_Johns',
    '-240_-240': 'America/Port_of_Spain',
    '-240_-180': 'America/Santiago',
    '-300_-300': 'America/Bogota',
    '-300_-240': 'America/New_York',
    '-360_-360': 'America/Costa_Rica',
    '-360_-300': 'America/Chicago',
    '-420_-420': 'America/Phoenix',
    '-420_-360': 'America/Denver',
    '-480_-480': 'Pacific/Pitcairn',
    '-480_-420': 'America/Los_Angeles',
    '-540_-540': 'Pacific/Gambier',
    '-540_-480': 'America/Anchorage',
    '-570_-570': 'Pacific/Marquesas',
    '-600_-600': 'Pacific/Honolulu',
    '-600_-540': 'America/Adak',
    '-660_-660': 'Pacific/Pago_Pago',
    '-720_-720': 'Etc/GMT+12',
}

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
