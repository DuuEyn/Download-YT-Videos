
<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/DuuEyn/Download-YT-Videos">
    <img src="https://lh3.googleusercontent.com/3_OFn2skqHXk-UQ-9RUdNrDl_HQJrMCxks5teQcUrF_bOSeDG1hD8j83FeD31W8hASZCvubzsGfumuJq8kvvSAq03wY87RZ7Otx_DF4" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Download-YT-Videos</h3>

  <p align="center">
    Downloads a YouTube video using <a href="https://pytube.io/en/latest/index.html">pytube</a>.
    <br />
    <a href="https://github.com/DuuEyn/Download-YT-Videos
"><strong>Explore the repo »</strong></a>
    <br />
    <br />
    <a href="https://github.com/DuuEyn/Download-YT-Videos/blob/main/yt_download.py
">View the code</a>
    ·
    <a href="https://github.com/DuuEyn/Download-YT-Videos
/issues">Report Bug</a>
    ·
    <a href="https://github.com/DuuEyn/Download-YT-Videos
/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
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
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a simple script that downloads a YouTube video, whose link and resolution is provided by the user, using the <a href="https://pytube.io/en/latest/index.html">pytube</a> library.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python.org]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
* Install pytube
  ```sh
  pip install pytube
  ```


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/DuuEyn/Download-YT-Videos
   ```
2. Move `yt_download.py` to your working directory.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

This script prompts the user for the YouTube link of the video to download. The user is then prompted to choose from the available resolution. The script then downloads the video to the folder `YT_Downloads` under the working directory.
<br />
<br />
<strong>NOTE: </strong> This script is only intended to execute a progressive download. In its current configuration, it does not support adaptive download, which requires the video and audio tracks to be downloaded separately in exchange for the highest quality streams. As a result, resolution of videos that can be downloaded by this script is limited to 720p and below.


<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/recommendedFeature`)
3. Commit your Changes (`git commit -m 'Add some recommendedFeature'`)
4. Push to the Branch (`git push origin feature/recommendedFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

DuuEyn - iddiche@gmail.com

Project Link: [https://github.com/DuuEyn/Download-YT-Videos](https://github.com/DuuEyn/Download-YT-Videos)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/DuuEyn/Download-YT-Videos.svg?style=for-the-badge
[contributors-url]: https://github.com/DuuEyn/Download-YT-Videos/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/DuuEyn/Download-YT-Videos.svg?style=for-the-badge
[forks-url]: https://github.com/DuuEyn/Download-YT-Videos/network/members
[stars-shield]: https://img.shields.io/github/stars/DuuEyn/Download-YT-Videos.svg?style=for-the-badge
[stars-url]: https://github.com/DuuEyn/Download-YT-Videos/stargazers
[issues-shield]: https://img.shields.io/github/issues/DuuEyn/Download-YT-Videos.svg?style=for-the-badge
[issues-url]: https://github.com/DuuEyn/Download-YT-Videos/issues
[license-shield]: https://img.shields.io/github/license/DuuEyn/Download-YT-Videos.svg?style=for-the-badge
[license-url]: https://github.com/DuuEyn/Download-YT-Videos/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/ian-dewaine-diche-69406a2bb
[Python.org]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
