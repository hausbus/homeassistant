import logging
from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.schalter.params.EState import EState
from pyhausbus.de.hausbus.homeassistant.proxy.schalter.params.EErrorCode import EErrorCode
from pyhausbus.de.hausbus.homeassistant.proxy.schalter.params.MOptions import MOptions

class Schalter(ABusFeature):
  CLASS_ID:int = 19

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return Schalter(HausBusUtils.getObjectId(deviceId, 19, instanceId))

  """
  @param offTime Ausschaltdauer: \r\nWert * Zeitbasis [ms].
  @param onTime Einschaltdauer: \r\nWert * Zeitbasis [ms].
  @param quantity Anzahl der Zustandswechsel.
  """
  def toggle(self, offTime:int, onTime:int, quantity:int):
    logging.info("toggle"+" offTime = "+str(offTime)+" onTime = "+str(onTime)+" quantity = "+str(quantity))
    hbCommand = HausBusCommand(self.objectId, 4, "toggle")
    hbCommand.addByte(offTime)
    hbCommand.addByte(onTime)
    hbCommand.addByte(quantity)
    hbCommand.send()
    logging.info("returns")

  """
  @param duration Einschaltdauer: \r\nWert * Zeitbasis [ms]\r\n0=nicht mehr ausschalten.
  @param onDelay Einschaltverzoegerung: Wert * Zeitbasis [ms]\r\n0=Keine.
  """
  def on(self, duration:int, onDelay:int):
    logging.info("on"+" duration = "+str(duration)+" onDelay = "+str(onDelay))
    hbCommand = HausBusCommand(self.objectId, 3, "on")
    hbCommand.addWord(duration)
    hbCommand.addWord(onDelay)
    hbCommand.send()
    logging.info("returns")

  """
  @param offDelay Ausschaltverzoegerung: Wert * Zeitbasis [ms]\r\n0=Keine.
  """
  def off(self, offDelay:int):
    logging.info("off"+" offDelay = "+str(offDelay))
    hbCommand = HausBusCommand(self.objectId, 2, "off")
    hbCommand.addWord(offDelay)
    hbCommand.send()
    logging.info("returns")

  """
  @param duration Dauer.
  """
  def evOn(self, duration:int):
    logging.info("evOn"+" duration = "+str(duration))
    hbCommand = HausBusCommand(self.objectId, 201, "evOn")
    hbCommand.addWord(duration)
    hbCommand.send()
    logging.info("returns")

  """
  """
  def evOff(self):
    logging.info("evOff")
    hbCommand = HausBusCommand(self.objectId, 200, "evOff")
    hbCommand.send()
    logging.info("returns")

  """
  """
  def getStatus(self):
    logging.info("getStatus")
    hbCommand = HausBusCommand(self.objectId, 5, "getStatus")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param state .
  @param duration Einschaltdauer: Wert * Zeitbasis [ms]\r\n0=Endlos.
  """
  def Status(self, state:EState, duration:int):
    logging.info("Status"+" state = "+str(state)+" duration = "+str(duration))
    hbCommand = HausBusCommand(self.objectId, 129, "Status")
    hbCommand.addByte(state.value)
    hbCommand.addWord(duration)
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

  """
  """
  def evToggle(self):
    logging.info("evToggle")
    hbCommand = HausBusCommand(self.objectId, 202, "evToggle")
    hbCommand.send()
    logging.info("returns")

  """
  @param maxOnTime Maximale Zeit.
  @param offDelayTime Verzoegerungszeit nach einem Off-Kommando.
  @param timeBase Zeitbasis [ms] fuer die Zeitabhaengigen Befehle.
  @param options Reservierte Bits muessen immer deaktiviert sein. Das Aktivieren eines reservierten Bits fuehrt nach dem Neustart des Controllers zu den Standart-Einstellungen..
  @param disableBitIndex Bit Index0-31 Systemvariable.
  """
  def Configuration(self, maxOnTime:int, offDelayTime:int, timeBase:int, options:MOptions, disableBitIndex:int):
    logging.info("Configuration"+" maxOnTime = "+str(maxOnTime)+" offDelayTime = "+str(offDelayTime)+" timeBase = "+str(timeBase)+" options = "+str(options)+" disableBitIndex = "+str(disableBitIndex))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addByte(maxOnTime)
    hbCommand.addByte(offDelayTime)
    hbCommand.addWord(timeBase)
    hbCommand.addByte(options.getValue())
    hbCommand.addByte(disableBitIndex)
    hbCommand.send()
    logging.info("returns")

  """
  """
  def getConfiguration(self):
    logging.info("getConfiguration")
    hbCommand = HausBusCommand(self.objectId, 0, "getConfiguration")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param maxOnTime Maximale Zeit.
  @param offDelayTime Verzoegerungszeit nach einem Off-Kommando.
  @param timeBase Zeitbasis [ms] fuer die Zeitabhaengigen Befehle.
  @param options Reservierte Bits muessen immer deaktiviert sein. Das Aktivieren eines reservierten Bits fuehrt nach dem Neustart des Controllers zu den Standart-Einstellungen..
  @param disableBitIndex Bit Index0-31 Systemvariable.
  """
  def setConfiguration(self, maxOnTime:int, offDelayTime:int, timeBase:int, options:MOptions, disableBitIndex:int):
    logging.info("setConfiguration"+" maxOnTime = "+str(maxOnTime)+" offDelayTime = "+str(offDelayTime)+" timeBase = "+str(timeBase)+" options = "+str(options)+" disableBitIndex = "+str(disableBitIndex))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addByte(maxOnTime)
    hbCommand.addByte(offDelayTime)
    hbCommand.addWord(timeBase)
    hbCommand.addByte(options.getValue())
    hbCommand.addByte(disableBitIndex)
    hbCommand.send()
    logging.info("returns")

  """
  @param cmdDelay Dauer Wert * Zeitbasis [ms].
  """
  def evCmdDelay(self, cmdDelay:int):
    logging.info("evCmdDelay"+" cmdDelay = "+str(cmdDelay))
    hbCommand = HausBusCommand(self.objectId, 203, "evCmdDelay")
    hbCommand.addWord(cmdDelay)
    hbCommand.send()
    logging.info("returns")

  """
  """
  def evDisabled(self):
    logging.info("evDisabled")
    hbCommand = HausBusCommand(self.objectId, 204, "evDisabled")
    hbCommand.send()
    logging.info("returns")


