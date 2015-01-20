# pyplotter
Tool to send cnc files to Makeblock Plotters

# Installation
1. Install python
2. Install pyserial
<pre><code>pip install pyserial</pre></code>

# Usage
Send CNC commands directly from command line:

    ./pyplotter.py /dev/cu.wchusbserial1410 # Linux, OSX
    python pyplotter.py COM1 # Windows

Send a CNC file to the plotter:

    ./pyplotter.py -f fish_simple.cnc /dev/cu.wchusbserial1410 # Linux, OSX
    python pyplotter.py -f fish_simple.cnc COM1 # Windows

Full usage:

<pre><code>usage: pyplotter.py [-h] [-f FILE] [-b BAUD] device

positional arguments:
  device                Serial device to connect

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File to send
  -b BAUD, --baud BAUD  Baud rate
</code></pre>
