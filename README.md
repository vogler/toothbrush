*DEPRECATED:* See [smart-home/toothbrush2mqtt.py](https://github.com/vogler/smart-home/blob/fa3a1979bf4fadb0cdee61dc04b08d0ee88f08c5/toothbrush2mqtt.py) which is just one file, only needs `bluepy`, and reports every second. This fork is too complicated, has too many dependencies, and `blus` only reports every 10s.

# Toothbrush

Receive BLE packets from your Oral-B electrical toothbrush

## how to use

```
> toothbrush --help
Receive BLE packets from your Oral-B electrical toothbrush

Usage:
  toothbrush (-h | --help)
  toothbrush --version
  toothbrush [-v|-vv] [options] scan
  toothbrush [-v|-vv] [options] monitor <mac>

Options:
  -i <interface>        Bluetooth adapter interface
  -h --help             Show this message
  -v,-vv                Increase verbosity
  --version             Show version

> toothbrush scan
Oral-B Toothbrush 11:22:33:44:55:66
^C

> toothbrush monitor 11:22:33:44:55:66
{"running": 2, "pressure": 32, "time": 0, "mode": 7, "quadrant": 1}
{"running": 2, "pressure": 32, "time": 0, "mode": 7, "quadrant": 1}
{"running": 2, "pressure": 32, "time": 0, "mode": 7, "quadrant": 1}
{"running": 2, "pressure": 32, "time": 0, "mode": 7, "quadrant": 1}
{"running": 2, "pressure": 32, "time": 0, "mode": 7, "quadrant": 1}
{"running": 2, "pressure": 32, "time": 0, "mode": 7, "quadrant": 1}
^C

> toothbrush monitor 11:22:33:44:55:66 | mosquitto_pub -l -t /toothbrush

```

## credits
Inspired by https://github.com/rfaelens/domotica/blob/master/mqtt-toothbrush.py
