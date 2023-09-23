{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/iTsRH98/ErrorAlpha/blob/main/deepfake.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "D3L8Lkyj-5gl"
      },
      "source": [
        "#Clone roop repo and install dependencies"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "0aHr4Fo-7IRy"
      },
      "outputs": [],
      "source": [
        "!git clone https://github.com/s0md3v/roop.git\n",
        "%cd roop\n",
        "!pip install -r requirements.txt"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "jl9zIFZYGWTQ"
      },
      "source": [
        "#download model"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Z6SA7jbZTN8i"
      },
      "outputs": [],
      "source": [
        "!wget https://huggingface.co/ezioruan/inswapper_128.onnx/resolve/main/inswapper_128.onnx -O inswapper_128.onnx\n",
        "!mkdir models\n",
        "!mv inswapper_128.onnx ./models"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "McO5R_O8JlrE"
      },
      "source": [
        "#GPU support"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "gKrwR2oEFkuC"
      },
      "outputs": [],
      "source": [
        "!pip uninstall onnxruntime onnxruntime-gpu -y\n",
        "!pip install torch torchvision torchaudio --force-reinstall --index-url https://download.pytorch.org/whl/cu118\n",
        "!pip install onnxruntime-gpu"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nCKli1C-_EaO"
      },
      "source": [
        "#Deepfake"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0PhkDU98hfEr"
      },
      "source": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "lDYdfL3L71i1"
      },
      "outputs": [],
      "source": [
        "!python run.py --target /content/bryan.mp4  --source /content/tom.jpg -o /content/swapped.mp4 --execution-provider cuda --frame-processor face_swapper face_enhancer"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "dB-yigWx8zht"
      },
      "outputs": [],
      "source": []
    }
  ],
  "metadata": {
    "accelerator": "GPU",
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}