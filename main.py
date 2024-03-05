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
        args = [str(_) for _ in arguments.strip().split(" ")]

        if len(args) == 1:
            to_given = args[0]
            from_given = datetime.strftime(datetime.now(), "%Y%m%d")
        else:
            to_given = args[1]
            from_given = args[0]

        for fmt in ["%Y%m%d", "%Y-%m-%d", "%Y/%m/%d"]:
            try:
                from_dt = datetime.strptime(from_given, fmt)
                to_dt = datetime.strptime(to_given, fmt)
            except ValueError:
                continue
            else:
                diff = (to_dt - from_dt).days
                return [
                    {
                        "Title": diff,
                        "SubTitle": f"{from_dt:%Y-%m-%d} → {to_dt:%Y-%m-%d}",
                        "IcoPath": "Images/app.png",
                    }
                ]
        return


if __name__ == "__main__":
    DateDiff()
