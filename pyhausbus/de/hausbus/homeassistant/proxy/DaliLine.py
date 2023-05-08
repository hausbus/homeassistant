import logging
from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.de.hausbus.homeassistant.proxy.daliLine.params.EErrorCode import EErrorCode

class DaliLine(ABusFeature):
  CLASS_ID:int = 160

  def __init__ (self,objectId:int):
    super().__init__(objectId)

  """
  @param address0 .
  @param address1 .
  @param address2 .
  @param address3 .
  """
  def getConfiguration(self, address0:int, address1:int, address2:int, address3:int):
    logging.info("getConfiguration"+" address0 = "+str(address0)+" address1 = "+str(address1)+" address2 = "+str(address2)+" address3 = "+str(address3))
    hbCommand = HausBusCommand(self.objectId, 0, "getConfiguration")
    hbCommand.addByte(address0)
    hbCommand.addByte(address1)
    hbCommand.addByte(address2)
    hbCommand.addByte(address3)
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param address0 .
  @param address1 .
  @param address2 .
  @param address3 .
  """
  def setConfiguration(self, address0:int, address1:int, address2:int, address3:int):
    logging.info("setConfiguration"+" address0 = "+str(address0)+" address1 = "+str(address1)+" address2 = "+str(address2)+" address3 = "+str(address3))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addByte(address0)
    hbCommand.addByte(address1)
    hbCommand.addByte(address2)
    hbCommand.addByte(address3)
    hbCommand.send()
    logging.info("returns")

  """
  """
  def allOff(self):
    logging.info("allOff")
    hbCommand = HausBusCommand(self.objectId, 2, "allOff")
    hbCommand.send()
    logging.info("returns")

  """
  """
  def allOn(self):
    logging.info("allOn")
    hbCommand = HausBusCommand(self.objectId, 3, "allOn")
    hbCommand.send()
    logging.info("returns")

  """
  @param command Dali Kommando s.Spezifikation.
  @param address Kurz- oder Gruppenadresse YAAA AAAS\r\n64 Kurzadressen           0AAA AAAS\r\n16 Gruppenadressen        100A AAAS\r\nSammelaufruf              1111 111S\r\n\r\nY: Adressenart: Y=?  ? ? ??  ?? ??? ??  ?0?  ? ? ??  ?? ??? ??  ? ? Kurzadresse.
  """
  def sendCommand(self, command:int, address:int):
    logging.info("sendCommand"+" command = "+str(command)+" address = "+str(address))
    hbCommand = HausBusCommand(self.objectId, 4, "sendCommand")
    hbCommand.addByte(command)
    hbCommand.addByte(address)
    hbCommand.send()
    logging.info("returns")

  """
  @param address0 .
  @param address1 .
  @param address2 .
  @param address3 .
  """
  def Configuration(self, address0:int, address1:int, address2:int, address3:int):
    logging.info("Configuration"+" address0 = "+str(address0)+" address1 = "+str(address1)+" address2 = "+str(address2)+" address3 = "+str(address3))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addByte(address0)
    hbCommand.addByte(address1)
    hbCommand.addByte(address2)
    hbCommand.addByte(address3)
    hbCommand.send()
    logging.info("returns")

  """
  @param status .
  """
  def Status(self, status:int):
    logging.info("Status"+" status = "+str(status))
    hbCommand = HausBusCommand(self.objectId, 129, "Status")
    hbCommand.addByte(status)
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


