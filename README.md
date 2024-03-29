<h1 align="center">
Quidk - Text Summarization
</h1>

<p align="center">
A summarization website for essays, scientific papers, thesis, web pages, etc. brings convenience in learning for students and teachers.</br>
</br>
<strong>Chromium-based extension available <a href="https://github.com/PL508/Quidk-extension">here</a>.</strong>
</p>

## Functionality

The website is capable of performing 3 kinds of text summarization tasks:

- By raw text:

![image](https://user-images.githubusercontent.com/58034112/177291521-63320156-36fa-4424-b2bb-fa48b544b0fc.png)

- By link embedded:

![image](https://user-images.githubusercontent.com/58034112/177291569-fe0a12cb-bd1f-4a40-9da4-432083fb5af9.png)

- By file:

![image](https://user-images.githubusercontent.com/58034112/177291616-099450b0-36b5-4272-908a-63ff29b5b52f.png)

## Prerequisites
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [TensorFlow](https://www.tensorflow.org/)
- [Beautiful Soup](https://realpython.com/beautiful-soup-web-scraper-python/)
- [Hugging Face Transformers](http://huggingface.co/docs/transformers)
- [Googletrans](https://py-googletrans.readthedocs.io/en/latest/)

## Installation

### Install Environment

You will need [Python 3.7 or later](https://www.python.org/downloads/) and [a C++14 compiler](https://osdn.net/projects/mingw/). Also, we highly recommend installing an [Anaconda](https://www.anaconda.com/distribution/#download-section) environment to get a high-quality BLAS library (MKL).

### Install Dependencies

All the libraries need for Quidk are in [requirements.txt](requirements.txt).</br>

Use `pip install -r .\requirements.txt` to install.

### Setup for discrete GPU (optional)

This program uses CPU by default. </br> We highly recommend using discrete GPU for the better performance.

If you want to run with **NVIDIA GPU** support, install:
- [NVIDIA CUDA](https://developer.nvidia.com/cuda-downloads) 10.2 or above.
- [NVIDIA cuDNN](https://developer.nvidia.com/cudnn) v7 or above.
- If you want to build on Windows, [Visual Studio 2017/2019 with MSVC toolset, and NVTX](https://visualstudio.microsoft.com/vs/older-downloads/) are also needed.
- [Compiler](https://gist.github.com/ax3l/9489132) compatible with CUDA.

or follow some tutorial videos for [Windows](https://youtu.be/hHWkvEcDBO0?t=50) or [Debian-based Linux distros](https://youtu.be/EFPxYotTwDI).

**_Note:_** You could refer to the [cuDNN Support Matrix](https://docs.nvidia.com/deeplearning/cudnn/pdf/cuDNN-Support-Matrix.pdf) for cuDNN versions with the various supported CUDA, CUDA driver and NVIDIA hardwares.

If you want to run with **AMD GPU** support, install:
- [AMD ROCm](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html) 4.0 and above installation.
- ROCm is currently supported only for **Linux systems**.

or follow [this tutorial video](https://youtu.be/efKjfBkjPlM) for **Debian-based Linux distros**.

**_CUDA and ROCm are not supported on macOS._**

**_After that_**, install [TensorFlow](https://www.tensorflow.org/hub/installation#use_with_tensorflow_2) via Conda or pip wheels (you may need [tested build configurations](https://www.tensorflow.org/install/source#gpu) to install correct version).

**_Note:_** If you are building for NVIDIA's Jetson platforms (Jetson Nano, TX1, TX2, AGX Xavier), Instructions to install PyTorch for Jetson Nano are [available here](https://devtalk.nvidia.com/default/topic/1049071/jetson-nano/pytorch-for-jetson-nano/) or you can follow [tutorial video](https://youtu.be/UiZaM-Wbc6A).

## How to run

Use `python .\run.py` to run the website.</br>

Default address: `http://127.0.0.1:5000`

## Acknowledgments
- [AI Blog Post Summarization with Hugging Face Transformers & Beautiful Soup Web Scraping](https://youtu.be/JctmnczWg0U)
- [Google Translate API with Python](https://www.youtube.com/watch?v=VIc_DDBpE7U)

## Credits
[Le Quang Phuc](https://www.facebook.com/phuc.lequang.9081/)</br>
[Huynh Tan Phuc](https://www.facebook.com/HtPuc)

## Feedback and contributions

Please let us know if you encounter a bug by [filing an issue](https://github.com/lqphuc123/Quidk/issues).

We appreciate all contributions. If you are planning to contribute back bug-fixes, please do so without any further discussion.

If you plan to contribute new features, utility functions, or extensions to the core, please first open an issue and discuss the feature with us.

## License

Quidk has a MIT license, as found in the [LICENSE](LICENSE) file.
