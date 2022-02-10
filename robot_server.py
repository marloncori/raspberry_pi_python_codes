#!/usr/bin/env python3
from flask import Flask
from modes import Modes
import sys

app = Flask(__name__)
mode_manager = Modes()

@app.route("/run/<mode_name>", methods=['POST'])
def run(mode_name):
  mode_manager.run(mode_name)
  return "Python script \'%s\' is running.\n"

@app.route("/stop", methods=['POST'])
def stop():
  mode_manager.stop()
  return "Program has stopped.\n"

if __name__ == '__main__':
  try:
    app.run(host="0.0.0.0", debug=True)
    
  except (KeyboardInterrupt, SystemExit):
    print("\nUser has shut down the server.")
    sys.exit(1)
