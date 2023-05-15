from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.GetMute()
volume.GetMasterVolumeLevel()
volume.GetVolumeRange()
volume_input = (input ("Input volume: "))
c = int (volume_input) /5
print (type(c))
log = c*2*4999.95
flog = float (log)
print (type(log))
print (type (flog))
dB = math.log10 (float (log))
print (dB)
print (type (dB))
volume.SetMasterVolumeLevel(dB, None)