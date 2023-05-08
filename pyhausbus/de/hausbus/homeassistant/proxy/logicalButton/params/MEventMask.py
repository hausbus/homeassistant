import pyhausbus.HausBusUtils as HausBusUtils
class MEventMask:

  def setNotifyOnCovered(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 0, self.value)
    return self;

  def isNotifyOnCovered(self):
    return HausBusUtils.isBitSet(0, self.value)
  def setNotifyOnClicked(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 1, self.value)
    return self;

  def isNotifyOnClicked(self):
    return HausBusUtils.isBitSet(1, self.value)
  def setNotifyOnStartHold(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 2, self.value)
    return self;

  def isNotifyOnStartHold(self):
    return HausBusUtils.isBitSet(2, self.value)
  def setNotifyOnEndHold(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 3, self.value)
    return self;

  def isNotifyOnEndHold(self):
    return HausBusUtils.isBitSet(3, self.value)
  def setNotifyOnDoubleClicked(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 4, self.value)
    return self;

  def isNotifyOnDoubleClicked(self):
    return HausBusUtils.isBitSet(4, self.value)
  def setNotifyOnFree(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 5, self.value)
    return self;

  def isNotifyOnFree(self):
    return HausBusUtils.isBitSet(5, self.value)
  def setReserved(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 6, self.value)
    return self;

  def isReserved(self):
    return HausBusUtils.isBitSet(6, self.value)
  def setEnableFeedBack(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 7, self.value)
    return self;

  def isEnableFeedBack(self):
    return HausBusUtils.isBitSet(7, self.value)
  def __init__(self, value:int):
    self.value = value

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    return MEventMask(HausBusUtils.bytesToInt(data, offset))



  def getValue(self):
    return self.value
  def getEntryNames(self):
    result = []
    result.append("NotifyOnCovered")
    result.append("NotifyOnClicked")
    result.append("NotifyOnStartHold")
    result.append("NotifyOnEndHold")
    result.append("NotifyOnDoubleClicked")
    result.append("NotifyOnFree")
    result.append("Reserved")
    result.append("EnableFeedBack")
    return result
  def setEntry(self,name:str, setValue:bool):
    if (name == "NotifyOnCovered"):
      self.setNotifyOnCovered(setValue)
    if (name == "NotifyOnClicked"):
      self.setNotifyOnClicked(setValue)
    if (name == "NotifyOnStartHold"):
      self.setNotifyOnStartHold(setValue)
    if (name == "NotifyOnEndHold"):
      self.setNotifyOnEndHold(setValue)
    if (name == "NotifyOnDoubleClicked"):
      self.setNotifyOnDoubleClicked(setValue)
    if (name == "NotifyOnFree"):
      self.setNotifyOnFree(setValue)
    if (name == "Reserved"):
      self.setReserved(setValue)
    if (name == "EnableFeedBack"):
      self.setEnableFeedBack(setValue)

  def __str__(self):
    return f"MEventMask(NotifyOnCovered = "+self.isNotifyOnCovered()+", NotifyOnClicked = "+self.isNotifyOnClicked()+", NotifyOnStartHold = "+self.isNotifyOnStartHold()+", NotifyOnEndHold = "+self.isNotifyOnEndHold()+", NotifyOnDoubleClicked = "+self.isNotifyOnDoubleClicked()+", NotifyOnFree = "+self.isNotifyOnFree()+", Reserved = "+self.isReserved()+", EnableFeedBack = "+self.isEnableFeedBack()+")"



