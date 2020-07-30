# Minimal Python Binding for C++ with SIP

This repository contains a minimal example of how to empower your Python application 
with c++ libraries, using SIP Python bindings. 

Most of the commercial software used in VFX/Animation like Maya, Nuke and Houdini are developed in C++, but they have Python APIs to allow users to quickly develop tools on the software. Though, as a TD or Artist who got deep into development, I started to feel the need to use C++ to improve the performance of my tools or to simply access lower level APIs. 

After studying C++ for a while, I found myself in a strange place where I had some fresh knowledge in my head and I was keen to put it to use, but I couldn’t really apply it in my work. I had this common misconception that from a certain point, my tools would become pure C++ beauties. Though it is a complicated language and it takes much longer than Python to perform certain tasks (Some seasoned developers may disagree, but here we’re talking about newcomers)

That’s when using both languages to develop a tool helps you to meet your deadlines and please the users. For instance, you can develop pretty much everything in your tool  in python except for the parts that you really need C++ for higher performance, lower level APIs or any other of its features. 
For instance, the whole GUI can be developed in python, while the heavy 3D scene processing can be done in C++.

The best of both worlds!

For that kind of architecture, we compile the C++ code in a library and use Python Bindings to expose it to the python application. 

I struggled to find beginners information about how to set those bindings properly, so I decided to record the steps I’ve taken and share with people who are in the same process of expanding the development knowledge from Pyhton towards C++.

In this minimal example, you’ll see how to author the bindings using SIP. Which is a technology developed to create the early versions of PyQt. Today it can be used for any kind of application.


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

