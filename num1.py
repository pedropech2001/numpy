{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled1.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMgAc0AD7E8xZcZ/NqIJOPo",
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
        "<a href=\"https://colab.research.google.com/github/pedropech2001/numpy/blob/master/num1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SVdeGtomeuQ9",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 67
        },
        "outputId": "73f2b841-ea0b-4076-d5b1-e97f1e9179db"
      },
      "source": [
        "import numpy as np\n",
        "yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')\n",
        "print(\"Yesterday: \", yesterday)\n",
        "today = np.datetime64('today', 'D')\n",
        "print(\"Today: \", today)\n",
        "tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')\n",
        "print(\"Tomorrow: \", tomorrow)"
      ],
      "execution_count": 47,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Yesterday:  2020-07-17\n",
            "Today:  2020-07-18\n",
            "Tomorrow:  2020-07-19\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}