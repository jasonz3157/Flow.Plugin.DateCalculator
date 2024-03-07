# Flow.Launcher.Plugin.DateCalculator
A [FlowLauncher](https://github.com/Flow-Launcher/Flow.Launcher) plugin written in python for calculating date

> [!TIP]
> There is already an awesome [Flow.Launcher.Plugin.DateDiff](https://github.com/LeoDupont/Flow.Launcher.Plugin.DateDiff) plugin, but it requires nodejs to be installed. I don't want to install nodejs on my PC, so I wrote this simple python plugin that uses Flow's embedded python.

### Usage
#### Diff

<img src="https://s2.loli.net/2024/03/07/oxOzmCsUMZ2l1Ja.png" width="400">

```
dc [FROM_DATE] TO_DATE
```
If *FROM_DATE* is not provided, today's date will be used.

Supported date formats:
- `YYYYMMDD`
- `YYYY/MM/DD`
- `YYYY-MM-DD`

e.g.
```
dc 20250101
dc 2025/01/01
dc 2025-01-01
dc 20240101 20250101
dc 2024/01/01 2025/01/01
dc 2024-01-01 2025-01-01
```
#### Calculating

<img src="https://s2.loli.net/2024/03/07/dOLto5xiRj6I9JB.png" width="400">

```
dc [FROM_DATE] DATE_DELTA
```
If *FROM_DATE* is not provided, today's date will be used.

*DATE_DELTA* should be composed of an *OPERATOR* and a *DATE_RANGE*:
- *OPERATOR*: `+` `-`
- *DATE_RANGE*: `ny` `nm` `nw` `nd` (n is an integer).

e.g.
```
dc +4d
dc +3m4d
dc -1y2m3w4d
dc 20240101 +2m4d
dc 2024/01/01 -1y4d
```