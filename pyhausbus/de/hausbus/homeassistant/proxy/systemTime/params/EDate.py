import pyhausbus.HausBusUtils as HausBusUtils
from enum import Enum

class EDate(Enum):
  _1=1
  _2=2
  _3=3
  _4=4
  _5=5
  _6=6
  _7=7
  _8=8
  _9=9
  _10=10
  _11=11
  _12=12
  _13=13
  _14=14
  _15=15
  _16=16
  _17=17
  _18=18
  _19=19
  _20=20
  _21=21
  _22=22
  _23=23
  _24=24
  _25=25
  _26=26
  _27=27
  _28=28
  _29=29
  _30=30
  _31=31
  SER_UNKNOWN=-1

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    checkValue = HausBusUtils.bytesToInt(data, offset)
    for act in EDate.__members__.values():
      if (act.value == checkValue):
        return act

    return EDate.SER_UNKNOWN

  @staticmethod
  def value_of(name: str) -> 'EDate':
    try:
      return EDate[name]
    except KeyError:
      return EDate.SER_UNKNOWN 




