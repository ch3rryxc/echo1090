from flask import *
import api, config

app = Flask(__name__, static_url_path = '/static')

@app.route('/')
def index():
    return render_template(
        'index.html', 
        lat = config.START_COORDS[0],
        lon = config.START_COORDS[1]
    )

@app.route('/live')
def live():
    return api.prepareResponse()

if __name__ == '__main__':
    app.run(
        host = config.HOST, 
        port = config.PORT,
        debug = True
    )