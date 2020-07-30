# Minimal C++ Python Binding with SIP

This repository contains a minimal example of how to empower your Python application 
with c++ libraries, using SIP Python bindings. 


As an Artist / TD in animation, Python it the king. All commercial tools are either developed
in python or offer powerful Python APIs for tool developments.  Though there may be some times
you want to harness the lower level high performance of C++. 
With SIP bindings you can develop some c++ libraries and incorporate them inside your python application.
This concept is extremely powerful since it allows you to develop non-processor demanding parts of your application (like UIs) with Python and all of its conveniences, then call c++ libraries for heavier tasks, such as processing large 3D scenes or exr images. 


# Instructions

## Requirements

To follow these instructions you'll need to be in Linux with the following packages installed
 - pip
 - gcc
 - python 3+ (it works with python 2.7+, but may require legacy packages)
 - virtualenv

Clone this repository and open a terminal on that location.

## 1. Set your virtual environment

This step is optional, but it's better to install your "hello world" library in a virtual
environment and keep your local python clean. 

In your bash terminal, type:

```
virtualenv --python python3 venv
source venv/bin/activate

```
*note*: replace `python3` by the alias of your local instalation of Python 3, e.g.: `python3.6`


## Build the library:


To build the c++ library.

```
cd src/build
g++ -c -Wall -Werror -fpic ../helloSip.cpp
g++ -shared -o libhelloSip.so helloSip.o
```
This shared library is built in an unconventional folder, so you need to add the lobrart location to the LD_LIBRARY_PATH, please, change the path bellow and run the command:

```
export LD_LIBRARY_PATH=/path/to/github/cloned/repo/src/build:$LD_LIBRARY_PATH
```

You can test if the library is working by using the provided main.cpp file. 
It just includes the library and run its function.

```
cd ../
g++ -Lbuild -Wall -o test main.cpp -lhelloSip
./test

>> Hello From C++!

```

 
## Create the Binding library:

Be sure you have sip installed in the current python environment.

```
pip install sip
```

Then, you can install the bindings in your environment by running the commands bellow:

```
cd .. 
pip install .
```

If something goes wrong, you can try running sip directly, as the log lines returned in the terminal are more helpful for debugging. 

```
sip-install
```

## Testing your bindings

You can try:

```
python
import helloSip
helloSip.helloFromCpp()
>>  Hello From C++!
```

# Need More info?

For more information, please access River Bank Computing's SIP reference documentation:
https://www.riverbankcomputing.com/static/Docs/sip/index.html

