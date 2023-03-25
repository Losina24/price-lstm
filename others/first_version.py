{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true,
    "pycharm": {
     "is_executing": true
    }
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "from keras.models import Sequential\n",
    "from keras.layers.core import Dense\n",
    "\n",
    "# Lectura y visualización del dataset\n",
    "data = pd.read_csv('kc_house_data.csv')\n",
    "print(data)\n",
    "\n",
    "# Graficar datos\n",
    "data.plot.scatter(x='sqft_living', y='price')\n",
    "plt.xlabel('Pies cuadrados construidos')\n",
    "plt.ylabel('Precio')\n",
    "plt.show()\n",
    "\n",
    "x = data['sqft_living'].values\n",
    "y = data['price'].values"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
