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

    To reference Static files(e.g., css, js) in Template files(e.g., html)

    ```sh
    <link rel="stylesheet" href="{{ url_for('static', filename='$FILE_NAME.css') }}
    # <link rel="stylesheet" href="$FILE_NAME.css">
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