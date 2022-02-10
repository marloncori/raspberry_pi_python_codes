from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def index():
  return "\n\033[1;35m======================\033[0m\n \033[1;34mHello, Flask!\n This is a simple server.\n\tEnjoy it :D\n\033[0m"

@app.route('/robot')
def robot():
  return "\t The robot is moving forward!\n"

if __name__ == '__main__':
  try:
    app.run(debug=True, host='0.0.0.0')
    
  except (KeyboardInterrupt, SystemExit):
    print(" [Server has been shut down.]")
    sys.exit(1)
