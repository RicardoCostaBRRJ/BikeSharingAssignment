# Bike-Sharing-Neural-Network-Udacity-Assignment

In this project, you'll build your first neural network and use it to predict daily bike rental ridership.

This is the environment I used:

#Linux

Distributor ID:	Ubuntu
Description:	Ubuntu 16.10
Release:	16.10
Codename:	yakkety

#Packages

* anaconda Command line client (version 1.6.3)
* conda 4.3.21
* Python 3.6.1 :: Anaconda custom (64-bit)

# Setup

#Step 1: Anaconda

You can download and install Anaconda from https://www.continuum.io/downloads. There will be easy instructions to follow. After the install, run 
```
conda upgrade conda
conda update --all
```
to make sure it's up to date.

#Step 2: Clone this github repo
```
git clone https://github.com/udacity/BikeSharingAssignment.git
```
Then 
```
cd BikeSharingAssignment/
```

#Step 3: Setup conda environment
```
conda -create name dlnd python=3.6
```

#Step 4: Activate conda environment
```
source activate dlnd
```

#Step 5: Install packages
```
conda install numpy matplotlib pandas jupyter notebook
```
Make sure everything is up to date
```
conda upgrade conda
conda update --all
```

# Note

Always update your conda environment before and after any installs, to make sure everything is up to date:
```
conda update --all
```

#This is the 'conda list' output from my environment

bleach                    1.5.0                    py36_0  
cycler                    0.10.0                   py36_0  
dbus                      1.10.10                       0  
decorator                 4.0.11                   py36_0  
entrypoints               0.2.2                    py36_1  
expat                     2.1.0                         0  
fontconfig                2.12.1                        3  
freetype                  2.5.5                         2  
glib                      2.50.2                        1  
gst-plugins-base          1.8.0                         0  
gstreamer                 1.8.0                         0  
html5lib                  0.999                    py36_0  
icu                       54.1                          0  
ipykernel                 4.6.1                    py36_0  
ipython                   6.1.0                    py36_0  
ipython_genutils          0.2.0                    py36_0  
ipywidgets                6.0.0                    py36_0  
jedi                      0.10.2                   py36_2  
jinja2                    2.9.6                    py36_0  
jpeg                      9b                            0  
jsonschema                2.6.0                    py36_0  
jupyter                   1.0.0                    py36_3  
jupyter_client            5.0.1                    py36_0  
jupyter_console           5.1.0                    py36_0  
jupyter_core              4.3.0                    py36_0  
libffi                    3.2.1                         1  
libgcc                    5.2.0                         0  
libiconv                  1.14                          0  
libpng                    1.6.27                        0  
libsodium                 1.0.10                        0  
libxcb                    1.12                          1  
libxml2                   2.9.4                         0  
markupsafe                0.23                     py36_2  
matplotlib                2.0.2               np113py36_0  
mistune                   0.7.4                    py36_0  
mkl                       2017.0.1                      0  
nbconvert                 5.2.1                    py36_0  
nbformat                  4.3.0                    py36_0  
notebook                  5.0.0                    py36_0  
numpy                     1.13.0                   py36_0  
openssl                   1.0.2l                        0  
pandas                    0.20.2              np113py36_0  
pandocfilters             1.4.1                    py36_0  
path.py                   10.3.1                   py36_0  
pcre                      8.39                          1  
pexpect                   4.2.1                    py36_0  
pickleshare               0.7.4                    py36_0  
pip                       9.0.1                    py36_1  
prompt_toolkit            1.0.14                   py36_0  
ptyprocess                0.5.1                    py36_0  
pygments                  2.2.0                    py36_0  
pyparsing                 2.1.4                    py36_0  
pyqt                      5.6.0                    py36_2  
python                    3.6.1                         2  
python-dateutil           2.6.0                    py36_0  
pytz                      2017.2                   py36_0  
pyzmq                     16.0.2                   py36_0  
qt                        5.6.2                         4  
qtconsole                 4.3.0                    py36_0  
readline                  6.2                           2  
setuptools                27.2.0                   py36_0  
simplegeneric             0.8.1                    py36_1  
sip                       4.18                     py36_0  
six                       1.10.0                   py36_0  
sqlite                    3.13.0                        0  
terminado                 0.6                      py36_0  
testpath                  0.3.1                    py36_0  
tk                        8.5.18                        0  
tornado                   4.5.1                    py36_0  
traitlets                 4.3.2                    py36_0  
wcwidth                   0.1.7                    py36_0  
wheel                     0.29.0                   py36_0  
widgetsnbextension        2.0.0                    py36_0  
xz                        5.2.2                         1  
zeromq                    4.1.5                         0  
zlib                      1.2.8                         3

