import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EErrorCode(Enum):
  NO_ZERO_CROSS_DETECTED=1
  INVALID_PERIOD=2
  INVALID_MODE=3
  DEFECT=4
  CONFIGURATION_OUT_OF_MEMORY=128
  ANY_ERROR=255
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EErrorCode.__members__.values():
      if (act.value == checkValue):
        return act

    return EErrorCode.SER_UNKNOWN

  @staticmethod
  def value_of(name: str) -> 'EErrorCode':
    try:
      return EErrorCode[name]
    except KeyError:
      return EErrorCode.SER_UNKNOWN 




