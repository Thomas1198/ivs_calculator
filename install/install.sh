#!/bin/sh
sudo apt install git
sudo apt install doxygen
sudo apt install python3
sudo add-apt-repository ppa:kivy-team/kivy
sudo apt-get install python3-kivy

git clone https://github.com/Thomas1198/ivs_calculator.git
cd ivs_calculator/src
make run