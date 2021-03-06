#!/usr/bin/env python
#
# Module for launching the Touchscreen module and specific modules required for each pi
#
# by Peter Juett
# References:
#
# Copyright 2018
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import socket
from threading import Thread

import time
import logging
import datetime
from logging.handlers import RotatingFileHandler
#import paho.mqtt.client as mqtt
#import DB

import TouchScreen
import GoogleCalendar
import SensorBoard
import SensorBoard2
import GY30
import BMP180
import DHT12
import WAQI
import AlphaVantage
import HUE
import HS100
import Sounds
import Automation

import YahooWeather
import HKWeather
import Transport
import RPIIO

class Launcher(object):

        def __init__(self):

		self.hostname = socket.gethostname().lower()

                self.log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')

                self.logFile = 'logs/launcher.log'

                self.my_handler = RotatingFileHandler(self.logFile, mode='a', maxBytes=5*1024*1024, backupCount=1, encoding=None, delay=0)
                self.my_handler.setFormatter(self.log_formatter)
                self.my_handler.setLevel(logging.INFO)

                self.app_log = logging.getLogger('root')
                self.app_log.setLevel(logging.INFO)

                self.app_log.addHandler(self.my_handler)

		self.start_threads()

                self.process_loop()


	def touch_screen(self):
		TouchScreen.run_program(self.app_log)

	def google_calendar(self):
		GoogleCalendar.run_program(self.app_log)

	def sensor_board(self):
		SensorBoard.run_program(self.app_log)

	def sensor_board_2(self):
		SensorBoard2.run_program(self.app_log)

	def gy30(self):
		GY30.run_program(self.app_log)

	def bmp180(self):
		BMP180.run_program(self.app_log)

	def dht12(self):
		DHT12.run_program(self.app_log)

	def waqi(self):
		WAQI.run_program(self.app_log)

	def alpha_vantage(self):
		AlphaVantage.run_program(self.app_log)

	def hue(self):
		HUE.run_program(self.app_log)

	def hs100(self):
		HS100.run_program(self.app_log)

	def yahoo_weather(self):
		YahooWeather.run_program(self.app_log)

	def hk_weather(self):
		HKWeather.run_program(self.app_log)

	def sounds(self):
		Sounds.run_program(self.app_log)

	def transport(self):
		Transport.run_program(self.app_log)

	def rpiio(self):
		RPIIO.run_program(self.app_log)

	def automation(self):
		Automation.run_program(self.app_log)

	def process_loop(self):
                try:
			while(True):	
				time.sleep(1)
		except Exception as e:
	                self.app_log.exception('Exception: %s', e)

	def start_threads(self):
                try:
			if (self.hostname == "bedroomtouch"):
       				self.touch_screen_thread = Thread(target=self.touch_screen,args=())
				self.touch_screen_thread.start()
				
       				self.automation_thread = Thread(target=self.automation,args=())
				self.automation_thread.start()
				
        			self.google_calendar_thread = Thread(target=self.google_calendar,args=())
				self.google_calendar_thread.start()

        			self.waqi_thread = Thread(target=self.waqi,args=())
				self.waqi_thread.start()

        			self.alpha_vantage_thread = Thread(target=self.alpha_vantage,args=())
				self.alpha_vantage_thread.start()

        			self.hue_thread = Thread(target=self.hue,args=())
				self.hue_thread.start()

        			self.hs100_thread = Thread(target=self.hs100,args=())
				self.hs100_thread.start()

        			self.yahoo_weather_thread = Thread(target=self.yahoo_weather,args=())
				self.yahoo_weather_thread.start()

        			self.hk_weather_thread = Thread(target=self.hk_weather,args=())
				self.hk_weather_thread.start()

        			self.rpiio_thread = Thread(target=self.rpiio,args=())
				self.rpiio_thread.start()

        			self.transport_thread = Thread(target=self.transport,args=())
				self.transport_thread.start()

			elif (self.hostname == "bedroomtouch2"):

       				self.touch_screen_thread = Thread(target=self.touch_screen,args=())
				self.touch_screen_thread.start()

       				self.automation_thread = Thread(target=self.automation,args=())
				self.automation_thread.start()

      				self.sensor_board_2_thread = Thread(target=self.sensor_board_2,args=())
				self.sensor_board_2_thread.start()

	       			self.gy30_thread = Thread(target=self.gy30,args=())
				self.gy30_thread.start()

       				self.bmp180_thread = Thread(target=self.bmp180,args=())
				self.bmp180_thread.start()

	       			self.dht12_thread = Thread(target=self.dht12,args=())
				self.dht12_thread.start()

	       			self.sounds_thread = Thread(target=self.sounds,args=())
				self.sounds_thread.start()

			elif (self.hostname == "livingroom"):

       				self.touch_screen_thread = Thread(target=self.touch_screen,args=())
				self.touch_screen_thread.start()

       				self.automation_thread = Thread(target=self.automation,args=())
				self.automation_thread.start()

      				self.sensor_board_thread = Thread(target=self.sensor_board,args=())
				self.sensor_board_thread.start()

	       			self.gy30_thread = Thread(target=self.gy30,args=())
				self.gy30_thread.start()

       				self.bmp180_thread = Thread(target=self.bmp180,args=())
				self.bmp180_thread.start()

	       			self.dht12_thread = Thread(target=self.dht12,args=())
				self.dht12_thread.start()
			else:
				print "No processes included for Hostname " + self.hostname



		except Exception as e:
	                self.app_log.exception('Exception: %s', e)



if __name__ == '__main__':
	launcher = Launcher()


