from flask import *
from thetapylib import *
from ptpcam import *

getBattery()
#
# # Create flask app and global pi 'thing' object.
# app = Flask(__name__)
#
# # Define app routes.
# # Index route renders the main HTML page.
# @app.route("/")
# def index():
#     return render_template('index.html')
#
# @app.route("/state/<path:service>", methods=['GET'])
# def view(service):
#     # print service
#     if service == 'driver/full':
#         return render_template('driver-full.html', servo_y_min=SERVO_Y_MIN, servo_y_max=SERVO_Y_MAX, servo_y_start=SERVO_Y_START, servo_x_min=SERVO_X_MIN, servo_x_max=SERVO_X_MAX, servo_x_start=SERVO_X_START)
#     elif service == 'driver/mobile':
#         return render_template('driver-mobile.html', switch=switch)
#     elif service == 'cardboard':
#         return render_template('cardboard.html')
#     else:
#         return ('Unknow request', 400)
#
# # Start the flask debug server listening on the pi port 5000 by default.
# if __name__ == "__main__":
# #
#     app.run(host='0.0.0.0', port=8089, debug=True, threaded=True)
#     # app.run(host='0.0.0.0', port=8089, debug=False, threaded=True)
