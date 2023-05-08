import logging
from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.de.hausbus.homeassistant.proxy.taupunkt.params.EErrorCode import EErrorCode
from pyhausbus.de.hausbus.homeassistant.proxy.taupunkt.params.ELastEvent import ELastEvent

class Taupunkt(ABusFeature):
  CLASS_ID:int = 42

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  """
  """
  def evLow(self):
    logging.info("evLow")
    hbCommand = HausBusCommand(self.objectId, 200, "evLow")
    hbCommand.send()
    logging.info("returns")

  """
  """
  def evInRange(self):
    logging.info("evInRange")
    hbCommand = HausBusCommand(self.objectId, 201, "evInRange")
    hbCommand.send()
    logging.info("returns")

  """
  """
  def evAbove(self):
    logging.info("evAbove")
    hbCommand = HausBusCommand(self.objectId, 202, "evAbove")
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
  def getConfiguration(self):
    logging.info("getConfiguration")
    hbCommand = HausBusCommand(self.objectId, 0, "getConfiguration")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param lowerThreshold untere Taupunktschwelle.
  @param lowerThresholdFraction Nachkommastellen der unteren Taupunktschwelle[00-99].
  @param upperThreshold obere Taupunktschwelle.
  @param upperThresholdFraction Nachkommastellen der oberen Taupunktschwelle[00-99].
  @param reportTimeBase Zeitbasis fuer die Einstellungen von minReportTime und maxReportTime.
  @param minReportTime Mindestzeit.
  @param maxReportTime Maximalzeit.
  @param hysteresis Hysterese [Wert * 0.
  @param calibration Dieser Wert wird verwendet um die vom Sensor gelieferten Messwerte zu justieren. [1/10 Prozent].
  @param deltaSensorID Die InstanceID des Sensors auf diesem Controller.
  """
  def setConfiguration(self, lowerThreshold:int, lowerThresholdFraction:int, upperThreshold:int, upperThresholdFraction:int, reportTimeBase:int, minReportTime:int, maxReportTime:int, hysteresis:int, calibration:int, deltaSensorID:int):
    logging.info("setConfiguration"+" lowerThreshold = "+str(lowerThreshold)+" lowerThresholdFraction = "+str(lowerThresholdFraction)+" upperThreshold = "+str(upperThreshold)+" upperThresholdFraction = "+str(upperThresholdFraction)+" reportTimeBase = "+str(reportTimeBase)+" minReportTime = "+str(minReportTime)+" maxReportTime = "+str(maxReportTime)+" hysteresis = "+str(hysteresis)+" calibration = "+str(calibration)+" deltaSensorID = "+str(deltaSensorID))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addSByte(lowerThreshold)
    hbCommand.addSByte(lowerThresholdFraction)
    hbCommand.addSByte(upperThreshold)
    hbCommand.addSByte(upperThresholdFraction)
    hbCommand.addByte(reportTimeBase)
    hbCommand.addByte(minReportTime)
    hbCommand.addByte(maxReportTime)
    hbCommand.addByte(hysteresis)
    hbCommand.addSByte(calibration)
    hbCommand.addByte(deltaSensorID)
    hbCommand.send()
    logging.info("returns")

  """
  """
  def getStatus(self):
    logging.info("getStatus")
    hbCommand = HausBusCommand(self.objectId, 2, "getStatus")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param lowerThreshold untere Taupunktschwelle.
  @param lowerThresholdFraction Nachkommastellen der unteren Taupunktschwelle[00-99].
  @param upperThreshold obere Taupunktschwelle.
  @param upperThresholdFraction Nachkommastellen der oberen Taupunktschwelle[00-99].
  @param reportTimeBase Zeitbasis fuer die Einstellungen von minReportTime und maxReportTime.
  @param minReportTime Mindestzeit.
  @param maxReportTime Maximalzeit.
  @param hysteresis Hysterese [Wert * 0.
  @param calibration Dieser Wert wird verwendet um die vom Sensor gelieferten Messwerte zu justieren. [1/10 Prozent].
  @param deltaSensorID Die InstanceID des Sensors auf diesem Controller.
  """
  def Configuration(self, lowerThreshold:int, lowerThresholdFraction:int, upperThreshold:int, upperThresholdFraction:int, reportTimeBase:int, minReportTime:int, maxReportTime:int, hysteresis:int, calibration:int, deltaSensorID:int):
    logging.info("Configuration"+" lowerThreshold = "+str(lowerThreshold)+" lowerThresholdFraction = "+str(lowerThresholdFraction)+" upperThreshold = "+str(upperThreshold)+" upperThresholdFraction = "+str(upperThresholdFraction)+" reportTimeBase = "+str(reportTimeBase)+" minReportTime = "+str(minReportTime)+" maxReportTime = "+str(maxReportTime)+" hysteresis = "+str(hysteresis)+" calibration = "+str(calibration)+" deltaSensorID = "+str(deltaSensorID))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addSByte(lowerThreshold)
    hbCommand.addSByte(lowerThresholdFraction)
    hbCommand.addSByte(upperThreshold)
    hbCommand.addSByte(upperThresholdFraction)
    hbCommand.addByte(reportTimeBase)
    hbCommand.addByte(minReportTime)
    hbCommand.addByte(maxReportTime)
    hbCommand.addByte(hysteresis)
    hbCommand.addSByte(calibration)
    hbCommand.addByte(deltaSensorID)
    hbCommand.send()
    logging.info("returns")

  """
  @param celsius Grad Celsius.
  @param centiCelsius hundertstel Grad Celsius.
  @param lastEvent .
  """
  def evStatus(self, celsius:int, centiCelsius:int, lastEvent:ELastEvent):
    logging.info("evStatus"+" celsius = "+str(celsius)+" centiCelsius = "+str(centiCelsius)+" lastEvent = "+str(lastEvent))
    hbCommand = HausBusCommand(self.objectId, 203, "evStatus")
    hbCommand.addSByte(celsius)
    hbCommand.addSByte(centiCelsius)
    hbCommand.addByte(lastEvent.value)
    hbCommand.send()
    logging.info("returns")

  """
  @param celsius Grad Celsius.
  @param centiCelsius hundertstel Grad Celsius.
  @param lastEvent .
  """
  def Status(self, celsius:int, centiCelsius:int, lastEvent:ELastEvent):
    logging.info("Status"+" celsius = "+str(celsius)+" centiCelsius = "+str(centiCelsius)+" lastEvent = "+str(lastEvent))
    hbCommand = HausBusCommand(self.objectId, 129, "Status")
    hbCommand.addSByte(celsius)
    hbCommand.addSByte(centiCelsius)
    hbCommand.addByte(lastEvent.value)
    hbCommand.send()
    logging.info("returns")


