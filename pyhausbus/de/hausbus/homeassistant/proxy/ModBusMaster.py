import logging
from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.de.hausbus.homeassistant.proxy.modBusMaster.params.ESensorType import ESensorType

class ModBusMaster(ABusFeature):
  CLASS_ID:int = 45

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  """
  @param idx index of the configuration slot.
  """
  def getConfiguration(self, idx:int):
    logging.info("getConfiguration"+" idx = "+str(idx))
    hbCommand = HausBusCommand(self.objectId, 0, "getConfiguration")
    hbCommand.addByte(idx)
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param idx index of the configuration slot.
  @param node Geraeteadresse im ModBus.
  @param sensorType Supported Power-Meter SDM630 / SDM72D / SDM72V2 / ORWE517.
  """
  def setConfiguration(self, idx:int, node:int, sensorType:ESensorType):
    logging.info("setConfiguration"+" idx = "+str(idx)+" node = "+str(node)+" sensorType = "+str(sensorType))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addByte(idx)
    hbCommand.addByte(node)
    hbCommand.addByte(sensorType.value)
    hbCommand.send()
    logging.info("returns")

  """
  @param idx index of the configuration slot.
  @param node device node on ModBus.
  @param sensorType Supported Power-Meter SDM630 / SDM72D / SDM72V2 / ORWE517.
  """
  def Configuration(self, idx:int, node:int, sensorType:ESensorType):
    logging.info("Configuration"+" idx = "+str(idx)+" node = "+str(node)+" sensorType = "+str(sensorType))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addByte(idx)
    hbCommand.addByte(node)
    hbCommand.addByte(sensorType.value)
    hbCommand.send()
    logging.info("returns")


