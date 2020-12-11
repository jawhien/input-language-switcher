
import globalPluginHandler
import ctypes
import api
from scriptHandler import script

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	@script(description="Switch input language", gesture="kb:windows+space")
	def script_switchLanguage(self, gesture):
		user32 = ctypes.windll.user32
		hnd=api.getFocusObject().windowHandle
		user32.PostMessageA(hnd, 0x0050, 2, 0)
