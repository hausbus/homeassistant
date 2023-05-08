import pyhausbus.HausBusUtils
from enum import Enum

class EIndex(Enum):
  RUNNING=0
  INSTALLED=1
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EIndex.__members__.values():
      if (act.value == checkValue):
        return act

    return EIndex.SER_UNKNOWN



