import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EEnable(Enum):
  FALSE=0
  TRUE=1
  INVERT=2
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EEnable.__members__.values():
      if (act.value == checkValue):
        return act

    return EEnable.SER_UNKNOWN

  @staticmethod
  def value_of(name: str) -> 'EEnable':
    try:
      return EEnable[name]
    except KeyError:
      return EEnable.SER_UNKNOWN 




