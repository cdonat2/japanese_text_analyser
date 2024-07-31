[![MIT License][license-shield]][license-url]

<!-- TABLE OF CONTENTS -->
<details>
  <summary id="readme-top">Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

A Japanese Text Analyser.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

[![Python][python.org]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started
To get a local copy up and running follow these steps.

### Requirements
* Python 3.10 [Python](https://www.python.org/downloads/release/python-3100/)
* Docker Desktop [Docker Desktop](https://www.docker.com/products/docker-desktop/)

### Installation
1. Clone the Project
  ```sh
  git clone https://github.com/cdonat2/japanese_text_analyser
  ```
2. Setup Manually
  ```sh
  pip install -r requirements.txt
  sudo apt install build-essential
  sudo apt-get install libboost-all-dev
  python3 manage.py makemigrations
  python3 manage.py migrate
  python3 manage.py collectstatic
  ```
3. Alternatively, use Docker

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

1. Run project
* Using `.env` File
  ```sh
  python manage.py runserver
  ```
* Using `.env-prod` File
  ```sh
  ENV_PATH=.env-prod python3 manage.py runserver
  ```
* Using Docker
  ```sh
  docker compose up --build
  docker compose down
  docker system prune -fa
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Christian Donat - c.donat.de@gmail.com

Project Link: [https://github.com/cdonat2/japanese-text-analyzer](https://github.com/cdonat2/japanese-text-analyzer)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Best Readme Template](https://github.com/othneildrew/Best-README-Template/tree/master)
* [Django App Template](https://github.com/rmiyazaki6499/django-app.git)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[Python.org]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://www.python.org/
