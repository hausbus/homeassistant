import pyhausbus.HausBusUtils
from enum import Enum

class EFirmwareId(Enum):
  AR8=1
  MS6=2
  SD6=3
  SD485=4
  SONOFF=5
  S0_Reader=6
  ESP=7
  HBC=8
  HBX192C3=9
  ESP32=10
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EFirmwareId.__members__.values():
      if (act.value == checkValue):
        return act

    return EFirmwareId.SER_UNKNOWN
  def getTemplateId(self) -> str:
    if (self.name.startsWith("HB")):
        return "HBC"
    return self.name



