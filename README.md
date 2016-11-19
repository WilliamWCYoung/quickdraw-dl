# Quickdraw-dl
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/WilliamWCYoung/quickdraw-dl/master/LICENSE.txt)

## Introduction

This script downloads doodles submitted to "Quick, Draw!", a new game by Google. The objective of the game is to draw well enough to be recognized by their neural network.

The game itself can be found at https://quickdraw.withgoogle.com/. 

Quickdraw-dl will download the top doodles for a given keyword. These doodles are provided in Google's IME format. Handily, it's not far off SVG paths, so the script will translate them into a valid format and save the resulting image within a subdirectory.

N.B. This script is a clone of the API calls made by quickdraw, and although it responds, usage should moderated.

## Installation

This script has been tested in python 3.5.2, and requires the ```requests``` library.

## Examples

Return images of a dog:
```
python quickdraw.py dog
```

Return images of the Mona Lisa:
```
python quickdraw.py "The Mona Lisa"
```

Return images of a random entity:
```
python quickdraw.py
```
