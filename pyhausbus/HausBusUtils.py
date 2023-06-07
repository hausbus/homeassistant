import time
import traceback

HOMESERVER_DEVICE_ID:int = 9998
HOMESERVER_OBJECT_ID:int = (HOMESERVER_DEVICE_ID << 16) + (0 << 8) + 1

UDP_PORT = 5855
UDP_PORT = 9

def getObjectId(deviceId:int, classId:int, instanceId:int) -> int:
  return (deviceId << 16) + (classId << 8) + instanceId

def bytesToDWord(data:bytearray, offset) -> int:
  try:
    result = 0
    result += (data[offset[0]] & 0xff)
    offset[0] += 1

    result += (data[offset[0]] & 0xff) * 256
    offset[0] += 1

    result += (data[offset[0]] & 0xff) * 65536
    offset[0] += 1

    result += (data[offset[0]] & 0xff) * 16777216
    offset[0] += 1

    return result
  except (Exception) as err:
    print("error:", err)
    traceback.print_exc()
    return 0


def bytesToWord(data:bytearray, offset) -> int:
  try:
    result = 0
    result += (data[offset[0]] & 0xff)
    offset[0] += 1

    result += (data[offset[0]] & 0xff) * 256
    offset[0] += 1

    return result
  except (Exception) as err:
    print("error:", err)
    #traceback.print_exc()
    return 0


def bytesToInt(data:bytearray, offset) -> int:
  try:
    if (len(data)<=offset[0]):
      return 0
    result = data[offset[0]] & 0xff;
    offset[0] += 1
    return result
  except (Exception) as err:
    print("error:", err)
    traceback.print_exc()
    return 0


def bytesToString(data:bytearray, offset) -> str:
  try:
    result = ""
    for i in range(offset[0], len(data)):
      offset[0] += 1
      if (data[i] == 0):
        break

      result += chr(data[i])
    return result
  except (Exception) as err:
    print("error:", err)
    traceback.print_exc()
    return ""


def bytesToDebugString(message:bytearray) -> str:
  result = ""
  for byte in message:
    if (result != ""):
      result = result + ", "
    result = result + hex(byte)
  return result


def getInstanceId(objectId) -> int:
  return (objectId) & 0xff


def getDeviceId(objectId) -> int:
  return ((objectId >> 24) & 0xff) * 256 + ((objectId >> 16) & 0xff)


def getClassId(objectId) -> int:
  return (objectId >> 8) & 0xff


def formatObjectId(objectId) -> str:
  result = "[DeviceId: " + str(getDeviceId(objectId))
  result += ", ClassId: " + str(getClassId(objectId))
  result += ", Instance: " + str(getInstanceId(objectId)) + "]"
  return result


def getClockIndependMillis():
  return time.perf_counter() * 1000


def setBit(is_set: bool, bit: int, value: int) -> int:
    if is_set:
        value |= (1 << bit)
    else:
        value &= ~(1 << bit)
    return value


def isBitSet(bit:int, value:int) -> bool:
  return ((value >> bit) & 1) > 0


def bytesToBlob(data:bytearray, offset) -> bytearray:
  try:
    result = bytearray(len(data) - offset[0])
    result[:] = data[offset[0]:]
    offset[0]=offset[0]+len(data);
    return result
  except (Exception) as err:
    print("error:", err)
    traceback.print_exc()
    return 0

def dWordToBytes(value: int) -> bytearray:
  result = bytearray(4)
  result[0] = value & 0xff
  result[1] = (value >> 8) & 0xff
  result[2] = (value >> 16) & 0xff
  result[3] = (value >> 24) & 0xff
  return result


def addWord(value: int, inOutList):
  inOutList.append(value & 0xff)
  inOutList.append((value >> 8) & 0xff)
  
def addDword(value: int, inOutList):
  inOutList.append(value & 0xff)
  inOutList.append((value >> 8) & 0xff)
  inOutList.append((value >> 16) & 0xff)
  inOutList.append((value >> 24) & 0xff)
  
def wordToBytes(value: int) -> bytearray:
  result = bytearray(2)
  result[0] = value & 0xff
  result[1] = (value >> 8) & 0xff
  return result

def bytesToSInt(data:bytearray, offset) -> int:
  result = data[offset[0]] & 0xff
  offset[0]+=1;
  if (result > 127):
    result -= 256
  return result

def formatBytes(data:bytearray, offset:int=0, length:int=-1, asHex:bool=True) -> str:
  if (length==-1):
    length=len(data)
      
    if (data == None):
      return "NULL"

    result=""
    
    for i in range (offset,length):
      if (asHex):
        result+="0x"+hex(data[i])
      else:
        result+=data[i] & 0xff
    return result

def bytesToList(data:bytearray, offset):
  try:
    result = bytearray()
    offsetStart = offset[0]
    for i in range (offsetStart,len(data),2):
      key = data[i] & 0xff
      value = data[i + 1] & 0xff
      result.append(key)
      result.append(value)
      offset[0]+=2
    return result
  except (Exception) as err:
    print("error:", err)
    traceback.print_exc()
    return bytearray()