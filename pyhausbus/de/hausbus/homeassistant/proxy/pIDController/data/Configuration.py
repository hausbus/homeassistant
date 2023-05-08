import pyhausbus.HausBusUtils as HausBusUtils

class Configuration:
  CLASS_ID = 44
  FUNCTION_ID = 128

  def __init__(self,P:int, I:int, D:int, targetValue:int, sensorObjectId:int, actorObjectId:int, timeout:int, hysteresis:int):
    self.P=P
    self.I=I
    self.D=D
    self.targetValue=targetValue
    self.sensorObjectId=sensorObjectId
    self.actorObjectId=actorObjectId
    self.timeout=timeout
    self.hysteresis=hysteresis


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Configuration(HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToDWord(dataIn, offset), HausBusUtils.bytesToDWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"Configuration(P={self.P}, I={self.I}, D={self.D}, targetValue={self.targetValue}, sensorObjectId={self.sensorObjectId}, actorObjectId={self.actorObjectId}, timeout={self.timeout}, hysteresis={self.hysteresis})"

  '''
  @param P P-Anteil des Reglers.
  '''
  def getP(self):
    return self.P

  '''
  @param I I-Anteil des Reglers.
  '''
  def getI(self):
    return self.I

  '''
  @param D D-Anteil des Reglers.
  '''
  def getD(self):
    return self.D

  '''
  @param targetValue Regelungszielwert z.B. targetValue*0.
  '''
  def getTargetValue(self):
    return self.targetValue

  '''
  @param sensorObjectId Komplette Objekt-ID des Feedback-Sensors.
  '''
  def getSensorObjectId(self):
    return self.sensorObjectId

  '''
  @param actorObjectId Komplette Objekt-ID des Stellers.
  '''
  def getActorObjectId(self):
    return self.actorObjectId

  '''
  @param timeout Zeit.
  '''
  def getTimeout(self):
    return self.timeout

  '''
  @param hysteresis Erweitert den Regelzielwert in einen Bereich\r\n0: Regelzielwert wird versucht exakt zu erreichen\r\n>0: Regelzielwert +/- hysteresis wird versucht zu erreichen.
  '''
  def getHysteresis(self):
    return self.hysteresis



