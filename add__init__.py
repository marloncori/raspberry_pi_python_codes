(...)

@intent_handler(IntentBuilder("")
                .require("Robot")
                .require("stop"))
def handle_stop(self, message):
  try:
    requests.post(self.base_url + "/stop")
    self.speak_dialog('Robot')
    self.speak_dialog('stopping')
 except:
     self.speak_dialog('UnableToReach'
     LOG.exception('Unable to reach the robot')
