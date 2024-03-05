# Flow.Launcher.Plugin.DateDiffPy
A FlowLauncher plugin written in python for calculating date diff

> [!TIP]
> There is already an awesome datediff plugin [Flow.Launcher.Plugin.DateDiff](https://github.com/LeoDupont/Flow.Launcher.Plugin.DateDiff), but it requires nodejs to be installed. I don't want to install nodejs on my PC, so I wrote this simple python plugin that uses Flow's embedded python.

### Usage
```
dd [FROM_DATE] TO_DATE
```
If *FROM_DATE* is not provided, today's date will be used.

Supported date formats:
- `YYYYmmdd`
- `YYYY/mm/dd`
- `YYYY-mm-dd`

e.g.
```
dd 20240101
dd 2024/01/01
dd 2024-01-01
dd 20240101 20250101
dd 2024/01/01 2025/01/01
dd 2024-01-01 2025-01-01
```