import pyhausbus.HausBusUtils
from enum import Enum

class EErrorCode(Enum):
  CONFIGURATION_OUT_OF_MEMORY=0
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EErrorCode.__members__.values():
      if (act.value == checkValue):
        return act

    return EErrorCode.SER_UNKNOWN



