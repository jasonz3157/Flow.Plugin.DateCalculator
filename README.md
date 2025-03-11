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

```
dc [FROM_DATE] {+|-}{TIME_DELTA}
```
e.g.
```
dc +181d
dc -1y2m3d
dc 2025/03/11 +366H
dc "Oct. 11, 2025"
dc "Mar. 11, 2025" -1y
```
![calculate01](https://raw.githubusercontent.com/jasonz3157/Flow.Plugin.DateCalculator/blob/master/Images/calculate01.png?raw=true | width=100)

- If *FROM_DATE* is not provided, today's date will be used.
- If *TIME_DELTA* contains space, please wrap it with quotes.