import json
import unittest
from types import SimpleNamespace
from unittest.mock import patch

import main


class SecondsOutputTests(unittest.TestCase):
    def test_seconds_title_contains_numeric_duration(self):
        """验证真实查询返回数值秒数, 覆盖大小写单位和不同时间差."""
        cases = [
            ("2026-08-24T00:00:00", "2026-08-24T00:00:01", "1.0 seconds"),
            ("2026-08-24T00:00:00", "2026-08-25T00:00:01", "86401.0 seconds"),
            ("2026-08-24T00:00:00", "2026-08-24T00:00:00", "0.0 seconds"),
            ("2026-08-25T00:00:01", "2026-08-24T00:00:00", "-86401.0 seconds"),
            ("2026-08-24T00:00:00", "2026-08-25T00:00:01.5", "86401.5 seconds"),
            ("2026-08-25T00:00:01.5", "2026-08-24T00:00:00", "-86401.5 seconds"),
        ]
        argv = ["main.py", json.dumps({"settings": {"what_first": "day"}})]
        windll = SimpleNamespace(
            kernel32=SimpleNamespace(GetUserDefaultUILanguage=lambda: 0x0409)
        )

        # 跳过 FlowLauncher 的 JSON-RPC 初始化, 直接测试实际查询路径.
        calculator = main.DateCalculator.__new__(main.DateCalculator)
        with (
            patch.object(main.sys, "argv", argv),
            patch.object(main.ctypes, "windll", windll, create=True),
            patch.object(main.locale, "setlocale"),
        ):
            for unit in ("s", "S"):
                for from_date, to_date, expected in cases:
                    with self.subTest(unit=unit, from_date=from_date, to_date=to_date):
                        results = calculator.query(f"{from_date} {to_date} %{unit}")
                        self.assertEqual(len(results), 1)
                        title = results[0]["Title"]
                        self.assertEqual(title, expected)
                        self.assertRegex(title, r"^-?\d+(?:\.\d+)? seconds$")


if __name__ == "__main__":
    unittest.main()
