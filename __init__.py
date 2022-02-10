from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from mycroft.util.log import LOG

import requests

class MyRobot(MycroftSkill):
  def __init__(self):
    super().__init__()
    self.base_url = self.settings.get("base_url")
  
  def handle_control(self, end_point, dialog_verb):
    try:
      resquests.post(self.base_url + end_point)
      self.speak_dialog('Robot')
      self.speak_dialog(dialog_verb)
    except:
      self.speak_dialog('UnableToReach')
      LOG.exception('Unable to reach the robot!')
      
  @intent_handler(IntentBuilder("")
                 .require("Robot")
                 .require("test"))
  def handle_test(self, message):
      self.handle_control('/run/test', 'test')
  
  @intent_handler(IntentBuilder("")
                 .require("Robot")
                 .require("test2"))
  def handle_test2(self, message):
      self.handle_control('/run/test2', 'test2')
      
  @intent_handler(IntentBuilder("")
                 .require("Robot")
                 .require("test3"))
  def handle_test3(self, message):
      self.handle_control('/run/test3', 'test3')
      
  @intent_handler(IntentBuilder("")
                 .require("Robot")
                 .require("test4"))
  def handle_test4(self, message):
     self.handle_control('/run/test4', 'test4')
  
  @intent_handler(IntentBuilder("")
                .require("Robot")
                .require("stop"))
  def handle_stop(self, message):
     self.handle_control('/stop', 'stopping')
 
def create_skill():
  return MyRobot()
