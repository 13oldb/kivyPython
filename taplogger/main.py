
from kivy.app import App
from kivy.uix.widget import Widget
import logging
from kivy.logger import Logger
logging.root = Logger
import sys

def redirect_to_file(text):
	original = sys.stdout
	sys.stdout = open('/home/inity/kivy/log.txt','a')
	print(text)
	sys.stdout = original

class TapWidget(Widget):
	def on_touch_down(self, touch):
		print(touch)
		redirect_to_file(touch)
class Tapper(App):
    def build(self):
        return TapWidget()

if __name__ == '__main__':
	Tapper().run()
