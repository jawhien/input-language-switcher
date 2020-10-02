
from scriptHandler import script
import globalPluginHandler
import ctypes
import api

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	@script(description="Switch input language", gesture="kb:windows+space")
	def script_langSwitch(self, gesture):
		user32 = ctypes.windll.user32

		hnd=api.getFocusObject().windowHandle
		user32.PostMessageA(hnd, 0x0050, 2, 0)
