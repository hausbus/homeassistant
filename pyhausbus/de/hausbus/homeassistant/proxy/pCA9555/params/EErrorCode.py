import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EErrorCode(Enum):
  CONNECTION_OK=0
  CONNECTION_LOST=1
  CONFIG_CHECK_FAILED=2
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




