# -*- coding: utf-8 -*-

import os
import re
import sys
from datetime import datetime

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, "lib"))
sys.path.append(os.path.join(parent_folder_path, "plugin"))

from dateutil.relativedelta import *
from flowlauncher import FlowLauncher


class DateDiff(FlowLauncher):
    def query(self, arguments: str):
        if not arguments:
            return
        args = [str(_).lower() for _ in arguments.strip().split(" ")]

        for fmt in ["%Y%m%d", "%Y-%m-%d", "%Y/%m/%d"]:
            to_given = args[0] if len(args) == 1 else args[1]
            from_given = (
                datetime.strftime(datetime.now(), fmt) if len(args) == 1 else args[0]
            )

            # dd [date] {+|-}1y2m3w4d
            if to_given.startswith("+") or to_given.startswith("-"):
                from_dt = datetime.strptime(from_given, fmt)
                delta_groups = re.search(
                    r"(?P<operator>[-+])(?P<year>\d+y)?(?P<month>\d+m)?(?P<week>\d+w)?(?P<day>\d+d)?",
                    to_given,
                    flags=re.IGNORECASE,
                )
                operator = delta_groups.group("operator")
                target_dt = from_dt + relativedelta(
                    years=(
                        int(operator + delta_groups.group("year").rstrip("y"))
                        if delta_groups.group("year")
                        else 0
                    ),
                    months=(
                        int(operator + delta_groups.group("month").rstrip("m"))
                        if delta_groups.group("month")
                        else 0
                    ),
                    weeks=(
                        int(operator + delta_groups.group("week").rstrip("w"))
                        if delta_groups.group("week")
                        else 0
                    ),
                    days=(
                        int(operator + delta_groups.group("day").rstrip("d"))
                        if delta_groups.group("day")
                        else 0
                    ),
                )
                return [
                    {
                        "Title": f"{target_dt:%Y-%m-%d}",
                        "SubTitle": f"{from_dt:%Y-%m-%d} {to_given}",
                        "IcoPath": "Images/app.png",
                    }
                ]
            # dd [from] to
            else:
                try:
                    from_dt = datetime.strptime(from_given, fmt)
                    to_dt = datetime.strptime(to_given, fmt)
                except ValueError:
                    continue
                else:
                    diff = (to_dt - from_dt).days
                    return [
                        {
                            "Title": str(diff),
                            "SubTitle": f"{from_dt:%Y-%m-%d} → {to_dt:%Y-%m-%d}",
                            "IcoPath": "Images/app.png",
                        }
                    ]
        return


if __name__ == "__main__":
    DateDiff()
