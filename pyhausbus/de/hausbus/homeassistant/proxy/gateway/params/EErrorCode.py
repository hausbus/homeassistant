import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EErrorCode(Enum):
  NO_ERROR=0
  WRITE_FAILED=1
  READ_FAILED=2
  QUEUE_OVERRUN=3
  BUSY_BUS=4
  RESET_BUS=5
  BUFFER_OVERRUN=6
  NO_CONFIGURATION=7
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EErrorCode.__members__.values():
      if (act.value == checkValue):
        return act

    return EErrorCode.SER_UNKNOWN



