
from scriptHandler import script
import globalPluginHandler
import ctypes

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	@script(description="Switch input language", gesture="kb:windows+space")
	def script_langSwitch(self, gesture):
		user32 = ctypes.windll.user32

		hnd=user32.GetForegroundWindow()
		user32.PostMessageA(hnd, 0x0050, 2, 0)
