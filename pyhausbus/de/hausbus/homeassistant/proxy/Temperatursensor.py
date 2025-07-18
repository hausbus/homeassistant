from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.ResultWorker import ResultWorker
import pyhausbus.HausBusUtils as HausBusUtils
from pyhausbus.de.hausbus.homeassistant.proxy.temperatursensor.data.Configuration import Configuration
from pyhausbus.de.hausbus.homeassistant.proxy.temperatursensor.data.Status import Status
from pyhausbus.de.hausbus.homeassistant.proxy.temperatursensor.params.ELastEvent import ELastEvent
from pyhausbus.de.hausbus.homeassistant.proxy.temperatursensor.params.EErrorCode import EErrorCode

class Temperatursensor(ABusFeature):
  CLASS_ID:int = 32

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  @staticmethod
  def create(deviceId:int, instanceId:int):
    return Temperatursensor(HausBusUtils.getObjectId(deviceId, 32, instanceId))

  """
  """
  def evCold(self):
    LOGGER.debug("evCold")
    hbCommand = HausBusCommand(self.objectId, 200, "evCold")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def evWarm(self):
    LOGGER.debug("evWarm")
    hbCommand = HausBusCommand(self.objectId, 201, "evWarm")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def evHot(self):
    LOGGER.debug("evHot")
    hbCommand = HausBusCommand(self.objectId, 202, "evHot")
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def getConfiguration(self):
    LOGGER.debug("getConfiguration")
    hbCommand = HausBusCommand(self.objectId, 0, "getConfiguration")
    ResultWorker()._setResultInfo(Configuration,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param lowerThreshold untere Temperaturschwelle.
  @param lowerThresholdFraction lowerThresholdFraction.
  @param upperThreshold obere Temperaturschwelle.
  @param upperThresholdFraction Nachkommastellen der oberen Temperaturschwelle [00-99].
  @param reportTimeBase Zeitbasis f?r die Einstellungen von minReportTime und maxReportTime.
  @param minReportTime Mindestzeit.
  @param maxReportTime Maximalzeit.
  @param hysteresis Hysterese [Wert * 0.
  @param calibration Dieser Wert wird verwendet um die vom Sensor gelieferten Messwerte zu justieren. [1/10 Grad].
  @param deltaSensorID Die InstanceID des Sensors auf diesem Controller.
  """
  def Configuration(self, lowerThreshold:int, lowerThresholdFraction:int, upperThreshold:int, upperThresholdFraction:int, reportTimeBase:int, minReportTime:int, maxReportTime:int, hysteresis:int, calibration:int, deltaSensorID:int):
    LOGGER.debug("Configuration"+" lowerThreshold = "+str(lowerThreshold)+" lowerThresholdFraction = "+str(lowerThresholdFraction)+" upperThreshold = "+str(upperThreshold)+" upperThresholdFraction = "+str(upperThresholdFraction)+" reportTimeBase = "+str(reportTimeBase)+" minReportTime = "+str(minReportTime)+" maxReportTime = "+str(maxReportTime)+" hysteresis = "+str(hysteresis)+" calibration = "+str(calibration)+" deltaSensorID = "+str(deltaSensorID))
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
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param lowerThreshold untere Temperaturschwelle.
  @param lowerThresholdFraction Nachkommastellen der unteren Temperaturschwelle [00-99].
  @param upperThreshold obere Temperaturschwelle.
  @param upperThresholdFraction Nachkommastellen der oberen Temperaturschwelle [00-99].
  @param reportTimeBase Zeitbasis fuer die Einstellungen von minReportTime und maxReportTime [s].
  @param minReportTime Mindestzeit.
  @param maxReportTime Maximalzeit.
  @param hysteresis Hysterese [Wert * 0.
  @param calibration Dieser Wert wird verwendet um die vom Sensor gelieferten Messwerte zu justieren. [1/10 Grad].
  @param deltaSensorID Die InstanceID des Sensors auf diesem Controller.
  """
  def setConfiguration(self, lowerThreshold:int, lowerThresholdFraction:int, upperThreshold:int, upperThresholdFraction:int, reportTimeBase:int, minReportTime:int, maxReportTime:int, hysteresis:int, calibration:int, deltaSensorID:int):
    LOGGER.debug("setConfiguration"+" lowerThreshold = "+str(lowerThreshold)+" lowerThresholdFraction = "+str(lowerThresholdFraction)+" upperThreshold = "+str(upperThreshold)+" upperThresholdFraction = "+str(upperThresholdFraction)+" reportTimeBase = "+str(reportTimeBase)+" minReportTime = "+str(minReportTime)+" maxReportTime = "+str(maxReportTime)+" hysteresis = "+str(hysteresis)+" calibration = "+str(calibration)+" deltaSensorID = "+str(deltaSensorID))
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
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  """
  def getStatus(self):
    LOGGER.debug("getStatus")
    hbCommand = HausBusCommand(self.objectId, 2, "getStatus")
    ResultWorker()._setResultInfo(Status,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param celsius Grad Celsius.
  @param centiCelsius hundertstel Grad Celsius.
  @param lastEvent .
  """
  def evStatus(self, celsius:int, centiCelsius:int, lastEvent:ELastEvent):
    LOGGER.debug("evStatus"+" celsius = "+str(celsius)+" centiCelsius = "+str(centiCelsius)+" lastEvent = "+str(lastEvent))
    hbCommand = HausBusCommand(self.objectId, 203, "evStatus")
    hbCommand.addSByte(celsius)
    hbCommand.addSByte(centiCelsius)
    hbCommand.addByte(lastEvent.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param errorCode .
  """
  def evError(self, errorCode:EErrorCode):
    LOGGER.debug("evError"+" errorCode = "+str(errorCode))
    hbCommand = HausBusCommand(self.objectId, 255, "evError")
    hbCommand.addByte(errorCode.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")

  """
  @param celsius Grad Celsius.
  @param centiCelsius hundertstel Grad Celsius.
  @param lastEvent .
  """
  def Status(self, celsius:int, centiCelsius:int, lastEvent:ELastEvent):
    LOGGER.debug("Status"+" celsius = "+str(celsius)+" centiCelsius = "+str(centiCelsius)+" lastEvent = "+str(lastEvent))
    hbCommand = HausBusCommand(self.objectId, 129, "Status")
    hbCommand.addSByte(celsius)
    hbCommand.addSByte(centiCelsius)
    hbCommand.addByte(lastEvent.value)
    ResultWorker()._setResultInfo(None,self.getObjectId())
    hbCommand.send()
    LOGGER.debug("returns")


