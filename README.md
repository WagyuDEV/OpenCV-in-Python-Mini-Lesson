# OpenCV in Python

In this workshop you will learn the basics of OpenCV and Python. This will be tought by example with detailed explanations as to how each step works.

# Installing OpenCV

We need to install our dependencies for this workshop; since we do not want the depencies for this workshop to clash with depencies for any of our other projects we will create a virtual environment (venv).

### Setting up venv

```bash
python3 -m venv .venv
# if on POSIX (mac, linux, bsd)
source .venv/bin/activate
# if on windows
.venv\Scripts\activate.bat
```

### Installing OpenCV

Now that we are in our virtual environment

```bash
pip install opencv-python
```

# Running the examples

While in our virtual environment

```bash
# depending on your system the command may be `python3` or `python`
python3 <filename> # ex python3 bitwise.py
```