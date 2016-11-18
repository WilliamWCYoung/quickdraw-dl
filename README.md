# Quickdraw-dl
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/WilliamWCYoung/quickdraw-dl/master/LICENSE.txt)

## Introduction

This script downloads submitted doodles to a new game by Google. The objective of the game is to draw well enough to be recognized by their neural network, very fun! 

The game itself can be found at https://quickdraw.withgoogle.com/. 

Quickdraw-dl will download the top doodles for a given keyword. These doodles are SVG paths, so the script will translate them into a valid format and save them within a subdirectory.

N.B. This script is a clone of their own API calls, and although it responds, should be respected.

## Installation

This script has been tested in python 3.5.2, and requires the ```requests``` library.
