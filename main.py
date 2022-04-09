import subprocess

class Plugin:
	# The name of the plugin. This string will be displayed in the Plugin menu
	name = "DeckPlayerCTL"
	# The name of the plugin author
	author = "ScorchLight"

	# If the plugin should be reloaded from a call to /plugins/reload or a file change
	hot_reload = True

	# The HTML that will be loaded when selecting the plugin in the list
	main_view_html = "main_view.html"

	# The HTML that will be used to display a widget in the plugin main page
	tile_view_html = "tile_view.html"

	# A normal method. It can be called from JavaScript using call_plugin_function("method_1", argument1, argument2)

	async def ctlnext(self):
		subprocess.Popen("playerctl next", stdout=subprocess.PIPE, shell=True).communicate()

	async def ctlplay(self):
		subprocess.Popen("playerctl play-pause", stdout=subprocess.PIPE, shell=True).communicate()

	async def ctlprev(self):
		subprocess.Popen("playerctl previous", stdout=subprocess.PIPE, shell=True).communicate()

	async def ctlartist(self):
		return subprocess.Popen("playerctl metadata --format '{{ artist }}'", stdout=subprocess.PIPE, shell=True).communicate()[0][0:-1] 
		#return "avril"
	async def ctltrack(self):
		return subprocess.Popen("playerctl metadata --format '{{ title }}'", stdout=subprocess.PIPE, shell=True).communicate()[0][0:-1]
		#return "avril"
	async def ctlstate(self):
		return subprocess.Popen("playerctl status", stdout=subprocess.PIPE, shell=True).communicate()[0] == b'Playing\n'

