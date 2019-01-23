import os
import sublime
import sublime_plugin

class Beep():
	binary = None
	modified = False

	if sublime.platform() != 'osx':
		print('Beep: Platform is not supported')
	else:
		binary = os.path.dirname(os.path.realpath(__file__)) + '/binary/beep'

	def command(self, cmd):
		if Beep.binary:
			Beep.modified = False
			self.window.run_command(cmd)

			if not Beep.modified:
				os.popen('"%s"' % Beep.binary)

class BeepListener(sublime_plugin.EventListener):
	def on_modified(self, view):
		Beep.modified = True

class UndoBeepCommand(sublime_plugin.WindowCommand):
	def run(self):
		Beep.command(self, 'undo')

class RedoBeepCommand(sublime_plugin.WindowCommand):
	def run(self):
		Beep.command(self, 'redo')