off: {quadrant: 15, running: 2, mode: 0}
on: {quadrant: 1-6, running: 3, mode: 1-?}

issues:
- refreshes only every 10s
- pressure always 50?
- quadrant is just increasing with every 30s flash instead of reporting the actual quadrant

❯ sudo ./toothbrush monitor 04:EE:03:BB:77:88
{"quadrant": 15, "running": 2, "time": 0, "pressure": 50, "mode": 0}
{"quadrant": 15, "running": 3, "time": 0, "pressure": 58, "mode": 0}
{"quadrant": 1, "running": 3, "time": 14, "pressure": 50, "mode": 1}
{"quadrant": 2, "running": 3, "time": 25, "pressure": 50, "mode": 1}
{"quadrant": 2, "running": 3, "time": 36, "pressure": 50, "mode": 1}
{"quadrant": 3, "running": 3, "time": 47, "pressure": 50, "mode": 1}
{"quadrant": 3, "running": 3, "time": 58, "pressure": 50, "mode": 1}
{"quadrant": 4, "running": 3, "time": 69, "pressure": 50, "mode": 1}
{"quadrant": 5, "running": 3, "time": 91, "pressure": 50, "mode": 1}
{"quadrant": 6, "running": 3, "time": 102, "pressure": 50, "mode": 1}
{"quadrant": 15, "running": 3, "time": 124, "pressure": 50, "mode": 1}
{"quadrant": 15, "running": 2, "time": 131, "pressure": 50, "mode": 0}
{"quadrant": 15, "running": 2, "time": 131, "pressure": 50, "mode": 0}
