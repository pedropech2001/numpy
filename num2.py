{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled1.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyP+78UxlFB4Iuu4EVYFftOw",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/pedropech2001/numpy/blob/master/num2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DMF-nT84dZlE",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import numpy as np\n",
        "#using no.full\n",
        "x = np.full((5, 8), 8, dtype=np.uint)\n",
        "print(x)\n",
        "#using no.ones\n",
        "y = np.ones([5, 6], dtype=np.uint) *9\n",
        "print(y)"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}