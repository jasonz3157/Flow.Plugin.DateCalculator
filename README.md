# Flow.Launcher.Plugin.DateDiffPy
A FlowLauncher plugin written in python for calculating date diff

> [!TIP]
> There is already an awesome datediff plugin [Flow.Launcher.Plugin.DateDiff](https://github.com/LeoDupont/Flow.Launcher.Plugin.DateDiff), but it requires nodejs to be installed. I don't want to install nodejs on my PC, so I wrote this simple python plugin that uses Flow's embedded python.

### Usage
#### Date Diff
```
dd [FROM_DATE] TO_DATE
```
If *FROM_DATE* is not provided, today's date will be used.

Supported date formats:
- `YYYYMMDD`
- `YYYY/MM/DD`
- `YYYY-MM-DD`

e.g.
```
dd 20250101
dd 2025/01/01
dd 2025-01-01
dd 20240101 20250101
dd 2024/01/01 2025/01/01
dd 2024-01-01 2025-01-01
```
#### Date Calculating
```
dd [FROM_DATE] DATE_DELTA
```
If *FROM_DATE* is not provided, today's date will be used.

DATE_DELTA should be composed of an *OPERATOR* and a *DATE_RANGE*.
- *OPERATOR*: `+` `-`
- *DATE_RANGE*: `ny` `nm` `nw` `nd` (n is an integer). If only an integer is given, it will be treated as `d`.

e.g.
```
dd -12
dd +12d
dd +3m4d
dd -1y2m3w4d
dd 20240101 +1y
```