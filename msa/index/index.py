from flask import Flask, render_template
import webbrowser
import os
from logging.config import dictConfig

# Debug
dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler', 
            'filename': 'test_error.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')