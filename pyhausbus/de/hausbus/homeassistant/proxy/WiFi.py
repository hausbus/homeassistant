import logging
from pyhausbus.HausBusCommand import HausBusCommand
from pyhausbus.ABusFeature import *
from pyhausbus.de.hausbus.homeassistant.proxy.wiFi.params.EErrorCode import EErrorCode

class WiFi(ABusFeature):
  CLASS_ID:int = 164

  def __init__ (self,objectId:int):
    super().__init__(objectId)

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
  @param mac1 .
  @param mac2 .
  @param mac3 .
  @param mac4 .
  @param mac5 .
  @param mac6 .
  """
  def wakeUpDevice(self, mac1:int, mac2:int, mac3:int, mac4:int, mac5:int, mac6:int):
    logging.info("wakeUpDevice"+" mac1 = "+str(mac1)+" mac2 = "+str(mac2)+" mac3 = "+str(mac3)+" mac4 = "+str(mac4)+" mac5 = "+str(mac5)+" mac6 = "+str(mac6))
    hbCommand = HausBusCommand(self.objectId, 2, "wakeUpDevice")
    hbCommand.addByte(mac1)
    hbCommand.addByte(mac2)
    hbCommand.addByte(mac3)
    hbCommand.addByte(mac4)
    hbCommand.addByte(mac5)
    hbCommand.addByte(mac6)
    hbCommand.send()
    logging.info("returns")

  """
  @param SSID .
  @param Password .
  @param Server_Port Zusaetzlicher Port fuer die Homeserverfunktionen z.B 15557 f?r Loxone oder 5855 f?r IOBroker.
  @param Server_IP0 Server IP-Adresse im Format IP0.IP1.IP2.IP3 0.0.0.0 deaktiviert das Gateway 13 und 14.
  @param Server_IP1 Server IP-Adresse im Format IP0.IP1.IP2.IP3 0.0.0.0 deaktiviert das Gateway 13 und 14.
  @param Server_IP2 Server IP-Adresse im Format IP0.IP1.IP2.IP3 0.0.0.0 deaktiviert das Gateway 13 und 14.
  @param Server_IP3 Server IP-Adresse im Format IP0.IP1.IP2.IP3 0.0.0.0 deaktiviert das Gateway 13 und 14.
  """
  def setConfiguration(self, SSID:str, Password:str, Server_Port:int, Server_IP0:int, Server_IP1:int, Server_IP2:int, Server_IP3:int):
    logging.info("setConfiguration"+" SSID = "+str(SSID)+" Password = "+str(Password)+" Server_Port = "+str(Server_Port)+" Server_IP0 = "+str(Server_IP0)+" Server_IP1 = "+str(Server_IP1)+" Server_IP2 = "+str(Server_IP2)+" Server_IP3 = "+str(Server_IP3))
    hbCommand = HausBusCommand(self.objectId, 1, "setConfiguration")
    hbCommand.addString(SSID)
    hbCommand.addString(Password)
    hbCommand.addWord(Server_Port)
    hbCommand.addByte(Server_IP0)
    hbCommand.addByte(Server_IP1)
    hbCommand.addByte(Server_IP2)
    hbCommand.addByte(Server_IP3)
    hbCommand.send()
    logging.info("returns")

  """
  @param SSID .
  @param Password .
  @param Server_Port Zusaetzlicher Port fuer die Homeserverfunktionen z.B 15557 f?r Loxone oder 5855 f?r IOBroker.
  @param Server_IP0 Server IP-Adresse im Format IP0.IP1.IP2.IP3 0.0.0.0 deaktiviert das Gateway 13 und 14.
  @param Server_IP1 Server IP-Adresse im Format IP0.IP1.IP2.IP3 0.0.0.0 deaktiviert das Gateway 13 und 14.
  @param Server_IP2 Server IP-Adresse im Format IP0.IP1.IP2.IP3 0.0.0.0 deaktiviert das Gateway 13 und 14.
  @param Server_IP3 Server IP-Adresse im Format IP0.IP1.IP2.IP3 0.0.0.0 deaktiviert das Gateway 13 und 14.
  """
  def Configuration(self, SSID:str, Password:str, Server_Port:int, Server_IP0:int, Server_IP1:int, Server_IP2:int, Server_IP3:int):
    logging.info("Configuration"+" SSID = "+str(SSID)+" Password = "+str(Password)+" Server_Port = "+str(Server_Port)+" Server_IP0 = "+str(Server_IP0)+" Server_IP1 = "+str(Server_IP1)+" Server_IP2 = "+str(Server_IP2)+" Server_IP3 = "+str(Server_IP3))
    hbCommand = HausBusCommand(self.objectId, 128, "Configuration")
    hbCommand.addString(SSID)
    hbCommand.addString(Password)
    hbCommand.addWord(Server_Port)
    hbCommand.addByte(Server_IP0)
    hbCommand.addByte(Server_IP1)
    hbCommand.addByte(Server_IP2)
    hbCommand.addByte(Server_IP3)
    hbCommand.send()
    logging.info("returns")

  """
  """
  def getCurrentIp(self):
    logging.info("getCurrentIp")
    hbCommand = HausBusCommand(self.objectId, 3, "getCurrentIp")
    hbCommand.send()
    resultObject=None
    logging.info("returns"+str(resultObject))
    return resultObject

  """
  @param IP0 .
  @param IP1 .
  @param IP2 .
  @param IP3 .
  """
  def CurrentIp(self, IP0:int, IP1:int, IP2:int, IP3:int):
    logging.info("CurrentIp"+" IP0 = "+str(IP0)+" IP1 = "+str(IP1)+" IP2 = "+str(IP2)+" IP3 = "+str(IP3))
    hbCommand = HausBusCommand(self.objectId, 129, "CurrentIp")
    hbCommand.addByte(IP0)
    hbCommand.addByte(IP1)
    hbCommand.addByte(IP2)
    hbCommand.addByte(IP3)
    hbCommand.send()
    logging.info("returns")


