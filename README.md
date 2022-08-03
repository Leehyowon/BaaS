# Serverless BaaS Scenario Tester

With this service, you can:

-   Text1

-   Text2


The application is written for [BaaS][KTC Serverless Service]. 


## Prerequisite for Flask

1. Directory Architecture

    ```sh
    ㄴ app.py
    ㄴ templates
        ㄴ $FILE_NAME.html
    ㄴ static
        ㄴ $FILE_NAME.css 
            ...
    ㄴ requirements.txt
    ㄴ Dockerfile
    ㄴ test_error.log
    ```

1.  Flask Template Setting

    To reference static files(e.g., css, js) in template files(e.g., html), add the url in the template files according to the form below.

    ```sh
    <link rel="stylesheet" href="{{ url_for('static', filename='$FILE_NAME.css') }}">
    # <link rel="stylesheet" href="$FILE_NAME.css">
    ```
1.  app.py

    Run the Flask server with app.py file.

    Recommend to set the file name 'app.py' to skip setting the environment vaiables.

    Add dictConfig in the app.py file to generate test_error.log file to debug easier.

    Set host '0.0.0.0' to allow external access.

    ```sh
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
    def $FUNCTION():
        return render_template('$FILE_NAME.html')
        

    if __name__=="__main__":
        app.run(host='0.0.0.0', port='$PORT', debug=True)
    ```


## Quick start

Text

1.  texts


## Production setup

This section details a full production setup using [BaaS][KTC Serverless Service].

1.  Install or update ~.

1.  Authenticate to the SDK:

    ```sh
    ~
    ```


[BaaS]: https://serverlessdev-web.ktcloud.com:12581/auth/login