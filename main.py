# -*- coding: utf-8 -*-

import json
import os
import re
import sys
from datetime import datetime
import shlex
import locale
import ctypes

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, "lib"))
sys.path.append(os.path.join(parent_folder_path, "plugin"))

from dateutil.relativedelta import relativedelta  # noqa: E402
from dateutil.parser import parse  # noqa: E402
from flowlauncher import FlowLauncher  # noqa: E402


class DateCalculator(FlowLauncher):
    @property
    def settings(self):
        return json.loads(sys.argv[1])["settings"]

    def query(self, arguments: str):
        if not arguments:
            return
        try:
            args = shlex.split(arguments)
        except ValueError:
            return

        now = datetime.now()

        _locale = locale.windows_locale[
            ctypes.windll.kernel32.GetUserDefaultUILanguage()
        ]
        locale.setlocale(locale.LC_ALL, _locale)

        day_first = True if self.settings["what_first"] == "day" else False
        for arg in args:
            if arg.startswith(("-", "+")):
                # Calculating mode
                time_delta = arg
                try:
                    from_dt = parse(args[0], dayfirst=day_first)
                except Exception:
                    from_dt = now
                delta_groups = re.search(
                    r"(?P<operator>[-+])(?P<years>\d+[yY])?(?P<months>\d+m)?(?P<weeks>\d+[wW])?(?P<days>\d+[dD])?(?P<hours>\d+[Hh])?(?P<minutes>\d+M)?(?P<seconds>\d+[sS])?",
                    time_delta,
                )
                operator = delta_groups.group("operator")
                deltas = {
                    "years": int(
                        operator + re.sub("[yY]", "", delta_groups.group("years"))
                    )
                    if delta_groups.group("years")
                    else 0,
                    "months": int(
                        operator + re.sub("[m]", "", delta_groups.group("months"))
                    )
                    if delta_groups.group("months")
                    else 0,
                    "weeks": int(
                        operator + re.sub("[wW]", "", delta_groups.group("weeks"))
                    )
                    if delta_groups.group("weeks")
                    else 0,
                    "days": int(
                        operator + re.sub("[dD]", "", delta_groups.group("days"))
                    )
                    if delta_groups.group("days")
                    else 0,
                    "hours": int(
                        operator + re.sub("[hH]", "", delta_groups.group("hours"))
                    )
                    if delta_groups.group("hours")
                    else 0,
                    "minutes": int(
                        operator + re.sub("[M]", "", delta_groups.group("minutes"))
                    )
                    if delta_groups.group("minutes")
                    else 0,
                    "seconds": int(
                        operator + re.sub("[sS]", "", delta_groups.group("seconds"))
                    )
                    if delta_groups.group("seconds")
                    else 0,
                }
                target_dt = from_dt + relativedelta(**deltas)
                return [
                    {
                        "Title": f"{target_dt:%x %X}",
                        "SubTitle": f"{from_dt:%x %X} {time_delta}",
                        "IcoPath": "Images/app.png",
                    }
                ]

        for index, arg in enumerate(args):
            if arg.startswith("%"):
                if arg.lstrip("%") in list("sSMhHdDmyY"):
                    time_fmt = arg.lstrip("%")
                else:
                    time_fmt = "d"
                args.pop(index)
                break
        else:
            time_fmt = "d"

        try:
            to_date = parse(args[-1], default=now, dayfirst=day_first)
        except Exception:
            return
        try:
            from_date = parse(args[-2], default=now, dayfirst=day_first)
        except Exception:
            from_date = now

        relativedelta_diff = relativedelta(to_date, from_date)
        remain_months = abs(relativedelta_diff.months)
        remain_days = abs(relativedelta_diff.days)

        delta_diff = to_date - from_date

        if time_fmt in ["d", "D"]:
            diff = f"{delta_diff.days} days"
        elif time_fmt in ["y", "Y"]:
            diff = f"{relativedelta_diff.years} years {remain_months} months {remain_days} days"
        elif time_fmt in ["m"]:
            diff = f"{relativedelta_diff.years * 12 + relativedelta_diff.months} months {remain_days} days"
        elif time_fmt in ["h", "H"]:
            diff = f"{delta_diff.days * 24} hours"
        elif time_fmt in ["M"]:
            diff = f"{delta_diff.days * 24 * 60} minutes"
        elif time_fmt in ["s", "S"]:
            diff = f"{delta_diff.total_seconds} seconds"
        return [
            {
                "Title": diff,
                "SubTitle": f"{from_date:%x %X} → {to_date:%x %X}",
                "IcoPath": "Images/app.png",
            }
        ]


if __name__ == "__main__":
    DateCalculator()
