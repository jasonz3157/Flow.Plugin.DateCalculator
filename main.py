# -*- coding: utf-8 -*-

import os
import sys
from datetime import datetime

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, "lib"))
sys.path.append(os.path.join(parent_folder_path, "plugin"))

from flowlauncher import FlowLauncher


class DateDiff(FlowLauncher):
    def query(self, arguments: str):
        if not arguments:
            return
        args = arguments.strip().split(" ")
        if len(args) == 1:
            to_given = args[0]
            from_dt = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        else:
            to_given = args[1]
            from_given = args[0]
            from_dt = datetime.strptime(f"{from_given:08}", "%Y%m%d")
        to_dt = datetime.strptime(f"{to_given:08}", "%Y%m%d")

        diff = (to_dt - from_dt).days
        return [
            {
                "Title": f"{diff} Days",
                "SubTitle": f"From {from_dt:%Y%m%d} to {to_dt:%Y%m%d}",
                "IcoPath": "Images/app.png",
            }
        ]


if __name__ == "__main__":
    DateDiff()
