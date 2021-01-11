# -*- mode: python; coding: utf-8 -*-

import logging

__version__ = "0.0.3"

_LOGGER = logging.getLogger(__name__)


def parse(device):
    mfd = device.get("ManufacturerData")

    if not mfd:
        _LOGGER.debug("no manufacturer data")
        return

    # 0xdc=220 is P&G
    # https://www.bluetooth.com/specifications/assigned-numbers/company-identifiers
    PG = 0xdc

    if PG not in mfd:
        _LOGGER.debug("wrong manufacturer key")
        return

    mfd = [int(x) for x in mfd[PG]]
    _LOGGER.debug("mfd: %s", mfd)
    # print("mfd:", mfd)

    # https://github.com/rfaelens/domotica/blob/master/mqtt-toothbrush.py
    # 0,1,2 always 4,113,4
    # 3 running: 2:off, 3:on
    # 4 pressure: always 50?
    # 5 time (min)
    # 6 time (sec)
    # 7 mode: 0 off, [1,7,2,4,3,6] cycled from top to bottom, mode (icon):
      # 1 Tägliche Reinigung
      # 7 Pro-Clean (Zahn mit Plus)
      # 2 Sensitiv (Feder)
      # 4 Aufhellen (Diamant)
      # 3 Zahnfleisch-Schutz (Wellen)
      # 6 Zungenreinigung (Zunge)
    # 8 quadrant: just counting up every 30s?
    # 9 angle? 0, 90, 45, 10, 65
    return dict(
        # battery?
        running=mfd[3],
        pressure=mfd[4],
        time=mfd[5] * 60 + mfd[6],
        mode=mfd[7],
        quadrant=mfd[8],
        maybe_angle=mfd[9],
        always6=mfd[10],
    )
