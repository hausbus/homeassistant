import pyhausbus.HausBusUtils
from enum import Enum

class EErrorCode(Enum):
  OK=0
  START_FAIL=1
  FAILTURE=2
  OUT_OF_MEMORY=4
  RESULT_NOT_AVAILABLE=12
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EErrorCode.__members__.values():
      if (act.value == checkValue):
        return act

    return EErrorCode.SER_UNKNOWN



