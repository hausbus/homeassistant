import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EDirection(Enum):
  TOGGLE=0
  TO_DARK=255
  TO_LIGHT=1
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EDirection.__members__.values():
      if (act.value == checkValue):
        return act

    return EDirection.SER_UNKNOWN



