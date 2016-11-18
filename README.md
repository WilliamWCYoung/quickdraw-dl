# Quickdraw-dl
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/WilliamWCYoung/quickdraw-dl/master/LICENSE.txt)

## Introduction

This script downloads doodles submitted to "Quick, Draw!", a new game by Google. The objective of the game is to draw well enough to be recognized by their neural network.

The game itself can be found at https://quickdraw.withgoogle.com/. 

Quickdraw-dl will download the top doodles for a given keyword. These doodles are provided in Google's IME format. Handily, it's not far off SVG paths, so the script will translate them into a valid format and save the resulting image within a subdirectory.

N.B. This script is a clone of the API calls made by quickdraw, and although it responds, usage should moderated.

## Installation

This script has been tested in python 3.5.2, and requires the ```requests``` library.

To run, simply call the python file with a keyword as the sole argument:
```
python quickdraw.py [word]
```

If it's multiple words, wrap in quote marks. For example:
```
python quickdraw.py 'The Mona Lisa'
```
