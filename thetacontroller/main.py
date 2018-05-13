from flask import *
# from thetapylib import *
from ptpcam import *

# Create flask app and global pi 'thing' object.
app = Flask(__name__)

# Define app routes.
# Index route renders the main HTML page.
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/v1/<path:service>", methods=['GET'])
def view(service):
    if service == 'state/battery':
        BatteryState = getBatteryState()
        return (BatteryState, 200)
    elif service == 'driver/mobile':
        return render_template('driver-mobile.html', switch=switch)
    elif service == 'cardboard':
        return render_template('cardboard.html')
    else:
        return ('Unknow request', 400)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8089, debug=True, threaded=True)
    # app.run(host='0.0.0.0', port=8089, debug=False, threaded=True)
