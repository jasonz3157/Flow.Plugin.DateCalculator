# Flow.Plugin.DateCalculator
A [FlowLauncher](https://github.com/Flow-Launcher/Flow.Launcher) plugin written in python for calculating date

> [!TIP]
> There is already an awesome [Flow.Launcher.Plugin.DateDiff](https://github.com/LeoDupont/Flow.Launcher.Plugin.DateDiff) plugin, but it requires nodejs to be installed. I don't want to install nodejs on my PC, so I wrote this simple python plugin that uses Flow's embedded python.

### Usage

> [!TIP]
> This plugin use python-dateutil to parse date string.
> It supports many formats, see [dateutil's documentation](https://dateutil.readthedocs.io/en/stable/examples.html#parse-examples) for details.

#### Diff
```
dc [FROM_DATE] TO_DATE [%UNIT]
```
- If *FROM_DATE* is not provided, today's date will be used.
- If *FROM_DATE* contains space, please wrap it with quotes.
- *%UNIT* is optional. *UNIT* can be one of the following:
    - `s`/`S`: seconds.
    - `M`: minutes.
    - `h`/`H`: hours.
    - `d`/`D`: days, default.
    - `m`: months.
    - `y`/`Y`: years.

e.g.
```
dc 20250101
dc 2025/01/01 %m
dc 2025/01/01
dc "Oct. 11, 2025"
dc "Oct. 10, 2025" %H
dc 20240101 2025-01-01
dc 2024/01/01 "Oct 11 2024"
```

<img src="https://github.com/jasonz3157/Flow.Plugin.DateCalculator/blob/master/Images/diff01.png?raw=true" width="400">

<img src="https://github.com/jasonz3157/Flow.Plugin.DateCalculator/blob/master/Images/diff02.png?raw=true" width="400">

<img src="https://github.com/jasonz3157/Flow.Plugin.DateCalculator/blob/master/Images/diff03.png?raw=true" width="400">

<img src="https://github.com/jasonz3157/Flow.Plugin.DateCalculator/blob/master/Images/calculate04.png?raw=true" width="400">

<img src="https://github.com/jasonz3157/Flow.Plugin.DateCalculator/blob/master/Images/diff04.png?raw=true" width="400">

<img src="https://github.com/jasonz3157/Flow.Plugin.DateCalculator/blob/master/Images/diff05.png?raw=true" width="400">

<img src="https://github.com/jasonz3157/Flow.Plugin.DateCalculator/blob/master/Images/diff06.png?raw=true" width="400">

#### Calculating

```
dc [FROM_DATE] {+|-}{TIME_DELTA}
```
- If *FROM_DATE* is not provided, today's date will be used.
- If *FROM_DATE* contains space, please wrap it with quotes.

e.g.
```
dc +181d
dc -1y2m3d
dc 2025/03/11 +366H
dc "Mar. 11, 2025" -1y
```
<img src="https://github.com/jasonz3157/Flow.Plugin.DateCalculator/blob/master/Images/calculate01.png?raw=true" width="400">

<img src="https://github.com/jasonz3157/Flow.Plugin.DateCalculator/blob/master/Images/calculate02.png?raw=true" width="400">

<img src="https://github.com/jasonz3157/Flow.Plugin.DateCalculator/blob/master/Images/calculate03.png?raw=true" width="400">

<img src="https://github.com/jasonz3157/Flow.Plugin.DateCalculator/blob/master/Images/calculate05.png?raw=true" width="400">