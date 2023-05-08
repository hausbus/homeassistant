import pyhausbus.HausBusUtils
from enum import Enum

class ELastEvent(Enum):
  BELOW=200
  IN_RANGE=201
  ABOVE=202
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in ELastEvent.__members__.values():
      if (act.value == checkValue):
        return act

    return ELastEvent.SER_UNKNOWN



