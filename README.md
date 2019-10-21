Chat app - simple one-room app for instant messaging
========
<!-- PROJECT SHIELDS -->
![MIT License][license-shield]
![Python 3.6+][python-shield]
![Node.js 10+][node-shield]
![Django 2.2][django-shield]
![React ^16][react-shield]

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/badge/license-MIT-green
[python-shield]: https://img.shields.io/badge/python-3.6+-brightgreen
[node-shield]: https://img.shields.io/badge/node-10+-brightgreen
[django-shield]: https://img.shields.io/badge/django-2.2-blue
[react-shield]: https://img.shields.io/badge/react-^16-blue

## Table of Contents

- [Installation](#installation)
- [Demo](#demo-with-docker)
- [License](#license)


## Installation

Chat app requires Python 3.6+, Node.js 10.0+ (see ```requirements.txt``` and ```package.json``` for details).

1. install libs

    ```bash
    sudo apt install python3-pip python3-dev
    ```

2. create env

    ```bash
    sudo dnf install python3-virtualenv
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
3. configure project
    1. Copy ```config/example.env``` to ```config/.env```
    2. You can change values in ```.env``` file, but for demonstration purposes such settings are ok. In production you need change DEBUG to ```False``` and make ALLOWED_HOSTS mode specific.
    3. Apply migrations to database:
    ```python manage.py migrate```
    4. (Optional) Apply fixtures (some users and messages, see [demo](#demo-with-docker) for credentials):
    ```python manage.py loaddata fixtures/users.json && python manage.py loaddata fixtures/messages.json```
    5. Create your superuser:
    ```python manage.py createsuperuser```
    6. (Optional) Collect static files (needed if you'll run with ```DEBUG=False```): 
    ```python manage.py collectstatic```
    
Finally run server:
```bash
python manage.py runserver
```

## Demo with Docker

Want to see Chat app in action? Just run ```docker compose up``` and go to ```localhost:8000```

Login credentials #1: `Feynman`/`MrFeynman`

Login credentials #2: `MrsSmith`/`MrsSmith`

## License

Everything you see here is open and free to use as long as you comply with the [MIT license](https://github.com/djet-me/chat/blob/master/LICENSE).