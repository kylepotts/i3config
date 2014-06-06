# -*- coding: utf-8 -*-

import subprocess

from i3pystatus import Status
from i3pystatus.mail import imap

status = Status(standalone=True)

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock",
        format="%d %B %Y %I:%M:%S",)

# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)

status.register("cpu_usage", format="CPU {usage:02}%")

# Shows your CPU temperature, if you have a Intel CPU
status.register("temp",
    format="{temp:.0f}°C",)



#Show Memory Usage
status.register("mem",
        format="Ram {avail_mem:.0f} Mb {percent_used_mem}%"
        )

#Network Information
status.register("network",
        format_up="Network {name}:{v4}",
        interface="enp0s15",
        )

# The battery monitor has many formatting options, see README for details

# This would look like this, when discharging (or charging)
# ↓14.22W 56.15% [77.81%] 2h:41m
# And like this if full:
# =14.22W 100.0% [91.21%]
#
# This would also display a desktop notification (via dbus) if the percentage
# goes below 5 percent while discharging. The block will also color RED.

# Has all the options of the normal network and adds some wireless specific things
# like quality and network names.
#
# Note: requires both netifaces and basiciw
# Shows disk usage of /
# Format:
# 42/128G [86G]
status.register("disk",
    path="/home",
    format="HDD {used}/{total}G [{avail}G]",)

# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI
status.register("pulseaudio",
    format="♪{volume}",)

status.register("weather",
        location_code="46322:4:US",
        units="imperial",
        format="Weather {current_temp:} {humidity}%",
    )

status.register("mail",
    backends=[
        imap.IMAP(
             # port and ssl are the defaults
             host="imap.gmail.com", port=993, ssl=True,
             username="punkkid219@gmail.com", password="@@ky12le"
            )
    ])

status.run()
