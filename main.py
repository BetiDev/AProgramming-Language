import testing
from sys import *
import time
import json
import replit
variables = []
class output:
  def log(output):
    try:
      print(output)
    except NameError:
      print("Error: Output is not defined")
    
  def clear():
    try:
      system("clear")
    except:
      system("cls")
  def sleep(seconds):
    time.sleep(seconds)
  def require(module):
    while True:
      print("Downloading " + module + "")
      time.sleep(0.5)
      replit.clear()
      print("Downloading " + module + ".")
      time.sleep(0.5)
      replit.clear()
      print("Downloading " + module + "..")
      replit.clear()
      time.sleep(0.5)
      print("Downloading " + module + "...")
      replit.clear()
      time.sleep(0.5)
  class filesystem:
    def append(filename,context):
      fileobject = open(filename,"a")
      fileobject.write(context)
      fileobject.close()
      return ""
    def write(filename,context):
      fileobject = open(filename,"w")
      fileobject.write(context)
      fileobject.close()
      return ""
    def read(filename):
      fileobject = open(filename,"r")
      return fileobject.read()
  def read():
    return input()