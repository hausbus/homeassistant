import logging
from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.de.hausbus.homeassistant.proxy.systemTime.params.EWeekDay import EWeekDay
from pyhausbus.de.hausbus.homeassistant.proxy.systemTime.params.EDate import EDate
from pyhausbus.de.hausbus.homeassistant.proxy.systemTime.params.EMonth import EMonth
from pyhausbus.de.hausbus.homeassistant.proxy.systemTime.params.EErrorCode import EErrorCode

class SystemTime(ABusFeature):
  CLASS_ID:int = 3

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  """
  """
  def getTime(self):
    logging.info("getTime")
    hbCommand = HausBusCommand(self.objectId, 0, "getTime")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param weekDay .
  @param date .
  @param month .
  @param year .
  @param hours .
  @param minutes .
  @param seconds .
  """
  def setTime(self, weekDay:EWeekDay, date:EDate, month:EMonth, year:int, hours:int, minutes:int, seconds:int):
    logging.info("setTime"+" weekDay = "+str(weekDay)+" date = "+str(date)+" month = "+str(month)+" year = "+str(year)+" hours = "+str(hours)+" minutes = "+str(minutes)+" seconds = "+str(seconds))
    hbCommand = HausBusCommand(self.objectId, 1, "setTime")
    hbCommand.addByte(weekDay.value)
    hbCommand.addByte(date.value)
    hbCommand.addByte(month.value)
    hbCommand.addWord(year)
    hbCommand.addByte(hours)
    hbCommand.addByte(minutes)
    hbCommand.addByte(seconds)
    hbCommand.send()
    logging.info("returns")

  """
  @param weekday .
  @param date .
  @param month .
  @param year .
  @param hours .
  @param minutes .
  @param seconds .
  """
  def Time(self, weekday:int, date:int, month:int, year:int, hours:int, minutes:int, seconds:int):
    logging.info("Time"+" weekday = "+str(weekday)+" date = "+str(date)+" month = "+str(month)+" year = "+str(year)+" hours = "+str(hours)+" minutes = "+str(minutes)+" seconds = "+str(seconds))
    hbCommand = HausBusCommand(self.objectId, 128, "Time")
    hbCommand.addByte(weekday)
    hbCommand.addByte(date)
    hbCommand.addByte(month)
    hbCommand.addWord(year)
    hbCommand.addByte(hours)
    hbCommand.addByte(minutes)
    hbCommand.addByte(seconds)
    hbCommand.send()
    logging.info("returns")

  """
  @param errorCode .
  """
  def evError(self, errorCode:EErrorCode):
    logging.info("evError"+" errorCode = "+str(errorCode))
    hbCommand = HausBusCommand(self.objectId, 255, "evError")
    hbCommand.addByte(errorCode.value)
    hbCommand.send()
    logging.info("returns")


