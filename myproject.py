from __future__ import print_function

import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.properties import *
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, FadeTransition
from kivy.lang import Builder
from kivy.base import runTouchApp
import time
import random
import subprocess
from kivy.uix.popup import Popup
from kivy.core.window import Window
import kivy
from kivy.config import Config
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.animation import Animation
from kivy.clock import Clock, mainthread
from kivy.uix.gridlayout import GridLayout
import threading
import time
import json
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from time import sleep, time
from subprocess import Popen

from smartcard.CardMonitoring import CardMonitor, CardObserver
from smartcard.util import toHexString
import subprocess
import Tkinter as tk
from Tkinter import *
# from Tkinter.Scrolle import ScrolledText
from smartcard.CardType import CardType, AnyCardType, ATRCardType
from smartcard.CardRequest import CardRequest
from smartcard.util import toHexString, toBytes
from subprocess import Popen, PIPE


# Before the window is created:

# Config.set('graphics' 'width' '200')
# Config.set('graphics' 'height' '200')
# Dynamically after the Window was created:
# Window.size = (400 400)

class DCCardType(CardType):
    def matches(self, atr, reader=None):
        return atr[0] == 0x3B


class PrintObserver(CardObserver):
    """A simple card observer that is notified
    when cards are inserted/removed from the system and
    prints the list of cards
    """

    def update(self, observable, actions):
        (addedcards, removedcards) = actions
        for card in addedcards:
            output = toHexString(card.atr)
            print('+Inserted:  ' + output)
            if output == "3B 9A 94 00 92 02 75 93 11 00 01 02 02 21":
                p = Popen("MOES1.bat",
                          cwd=r"C:\Users\D_prince Abdulhamid\Desktop\WRITING\WRITING-20171019T094713Z-001\WRITING",
                          stdout=PIPE,
                          stderr=subprocess.STDOUT)
                d = Popen("MOES2.bat",
                          cwd=r"C:\Users\D_prince Abdulhamid\Desktop\WRITING\WRITING-20171019T094713Z-001\WRITING",
                          stdout=PIPE,
                          stderr=subprocess.STDOUT)
                while True:
                    out = p.stdout.readline()
                    if out == '' and p.poll() is not None:
                        print(out)
                        break
                    out2 = d.stdout.readline()
                    if out2 == '' and d.poll() is not None:
                        print(out2)
                        break
                    print(out2)
                    print(out)

                print('MOES ID MATCHED....')
                print("\n")
                print('CONNECTED TO NETWORK')
            else:
                print("\n")
                print('MOES ID NOT DETECTED (CONNECTION UNSUCCESSFUL)')
        for card in removedcards:
            print("\n")
            print("-Removed: " + toHexString(card.atr))
            p = Popen("disconnect.bat", cwd=r"C:\Users\Emmanuel\Desktop\MOES\moes_sim_files",
                      stdout=PIPE, stderr=subprocess.STDOUT)
            print("\n")
            print('MOES CARD REMOVED (WIFI DISCONNECTED)')


class timer():
    def work1(self):
        print("Hello World")
        MyScreenManager.current = 'first'


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class ThirdScreen(Screen):
    pass


class ScrollableLabel(ScrollView):
    text = StringProperty('')


class MyScreenManager(ScreenManager):

    def connectCard(self):
        cardtype = AnyCardType()
        cardrequest = CardRequest(timeout=4, cardType=cardtype)
        cardservice = cardrequest.waitforcard()
        cardservice.connection.connect()
        a = toHexString(cardservice.connection.getATR())
        self.txxt.text = a

    def on_press(self):
        self.root.ids.sm.current = 'first'

        # def new_color_screen(self):
        # name = time.time()
        # s = ColourScreen(name = name
        # colour =[random.random() for _ in range(3) + [1]])

    def vtr(self):
        cardtype = ATRCardType(toBytes("3B 16 94 20 02 01 00 00 0D"))
        cardrequest = CardRequest(timeout=1, cardType=cardtype)
        cardservice = cardrequest.waitforcard()
        cardservice.connection.connect()
        toHexString(cardservice.connection.getATR())
        output = toHexString(cardservice.connection.getATR())
        self.txxt.text = output
        self.txxt.text = err

    def uname(self):
        l = []
        m = []
        p = subprocess.Popen('netsh wlan add profile filename = "MOES1.xml"', stdout=subprocess.PIPE)
        out = p.stdout.readline()
        retcode = p.wait()
        self.ted.text = out
        q = subprocess.Popen('netsh wlan set profileparameter name=MOES1 SSID name=MOES1 keymaterial=codel201711',
                             stdout=subprocess.PIPE)
        out = q.stdout.readline()
        retcode = q.wait()
        self.ted.text = out
        r = subprocess.Popen('netsh wlan connect name=MOES1 ssid=MOES1', stdout=subprocess.PIPE)
        out = r.stdout.readline()
        retcode = r.wait()
        self.ted.text = out
        t = subprocess.Popen('netsh wlan add profile filename = "MOES2.xml', stdout=subprocess.PIPE)
        out2 = t.stdout.readline()
        retcode = t.wait()
        self.ted.text = out2
        u = subprocess.Popen('netsh wlan set profileparameter name=MOES2 SSID name=MOES2 keymaterial=qwerty123',
                             stdout=subprocess.PIPE)
        out2 = u.stdout.readline()
        retcode = u.wait()
        self.ted.text = out2
        v = subprocess.Popen('netsh wlan connect name=MOES2 ssid=MOES2', stdout=PIPE, stderr=subprocess.STDOUT)

        out2 = v.stdout.readline()
        retcode = v.wait()
        self.ted.text = out2

    # v=subprocess.Popen('netsh wlan connect name = "AUser"',stdout=subprocess.PIPE)
    # text = v.stdout.read()
    # retcode = v.wait()
    # self.sds.text = text
    # self.ted.text = text
    # print (text)
    def rssi(self):
        p = subprocess.Popen('netsh wlan show network mode = "Bssid"', stdout=subprocess.PIPE)
        text = p.stdout.read()
        retcode = p.wait()
        self.fret.text = text
        print(text)

    def animd(self):
        anim = Animation(opacity=0.3, width=100, duration=0.6)
        anim += Animation(opacity=1, width=400, duration=0.8)
        anim.repeat = True
        anim.start(self.anim_box)


class ColorScreen(Screen):
    pass


class ScreenButton(Button):
    screenmanager = ObjectProperty()

    def on_press(self, *args):
        super(ScreenButton, self).on_press(*args)
        self.screenmanager.current = 'first'


root_widget = Builder.load_string('''
#: import FadeTransition kivy.uix.screenmanager.FadeTransition
MyScreenManager:
	anim_box :anim_box
	txxt:txxt
	id : sm
	ted:ted
	fret:fret
	sds:sds
	transition: FadeTransition()
	FirstScreen:
		name:"first"
		GridLayout:
			cols:1
			row_force_default:True
			row_default_height:40
			spacing: 10
			padding: 10
			Label :
				height: 10
				width: 10
				text: "N-PROFILE NETWORK SYSTEM"
				font_size: 20
			Button:
				height: 10
				width: 10
				text:"CHECK ATR"
				font_size: 20
				on_press:app.root.connectCard()
			Label:
				id:sds
			TextInput:
				id:txxt
				height: 10
				width: 10
				name:"getatr"
				multiline:True
				text:
			Button:
				height: 10
				width: 10
				text:"Go to Network page"
				font_size: 20
				on_press:app.root.current = 'second'
	SecondScreen:
		name:"second"
		GridLayout:
			rows:5
			spacing: 10
			padding: 10
			cols:1
			Label:
				height: 10
				width: 10
				size_hint_y : 0.1
				text: "INFORMATION"
				outline_color: 1,1,1
				size: self.texture_size
			
			Button:
				height: 10
				width: 10
				size_hint_y : 0.1
				text:"CHECK NETWORK DETAILS"
				font_size: 20
				on_press: app.root.rssi()
			Button:
				height: 10
				width: 10
				size_hint_y : 0.1
				text:"SIGN IN"
				font_size: 20
				on_press:app.root.current = 'third'
				
			Button:
				height: 10
				width: 10
				size_hint_y : 0.1
				text:"BACK TO HOME"
				font_size: 20
				on_press: app.root.current = 'first'
			ScrollableLabel:
				Label:
					id : fret
					size_hint_y: None
					height: self.texture_size[1]
					text_size: self.width, None
					text_size: self.width, None
	ThirdScreen:
		name:"third"
		GridLayout:
			rows:5
			spacing: 10
			padding: 10
			cols:1
			Label:
				height: 10
				width: 10
				size_hint_y : 0.1
				text: "INFORMATION"
				outline_color: 1,1,1
				size: self.texture_size
			Button:
				height: 10
				width: 10
				size_hint_y : 0.1
				text:"BACK TO HOME"
				font_size: 20
				on_press: app.root.current = 'first'

			Button:
				height: 10
				width: 10
				size_hint_y : 0.1
				text:"CONNECT TO NETWORK"
				font_size: 20
				on_press: app.root.animd
			Label:
				id:anim_box
				height: 10
				width: 10
				size_hint_y : 0.1
				text: "INFORMATION"
				outline_color: 1,1,1
				size: self.texture_size

			ScrollableLabel:
				Label:
					id : ted
					size_hint_y: None
					height: self.texture_size[1]
					text_size: self.width,None
''')


class MyprojectApp(App):
    def build(self):
        return root_widget


MyprojectApp().run()
