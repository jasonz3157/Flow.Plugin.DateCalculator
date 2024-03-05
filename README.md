# Flow.Launcher.Plugin.DateDiffPy
A FlowLauncher plugin written in python for calculating date diff

> There is already an awesome datediff plugin [Flow.Launcher.Plugin.DateDiff](https://github.com/LeoDupont/Flow.Launcher.Plugin.DateDiff), but it requires nodejs to be installed.<br>I don't want to install nodejs on my PC, so I wrote this simple python plugin that uses the flow's embedded python without any other dependencies.

### Usage
```
dd FROM_DATE [TO_DATE]
```
e.g.
```
dd 20240101
dd 2024/01/01
dd 2024-01-01
dd 20240101 20250101
dd 2024/01/01 2025/01/01
dd 2024-01-01 2025-01-01
```