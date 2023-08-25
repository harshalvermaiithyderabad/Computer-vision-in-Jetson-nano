PIL

Quick and easy
Python2: sudo apt-get install python-scipy python-h5py python-pil
Python3: sudo apt-get install python3-scipy python3-h5py python3-pil
but depending on your use-case that may leave you with outdated versions.

For something fancier, e.g. with a Python-Environment you can:
pip install scipy h5py PIL


Pycuda installations 
# Remember to give proper cuda path 10.2.0
https://forums.developer.nvidia.com/t/pycuda-installation-failure-on-jetson-nano/77152/4


# Install libraries
sudo apt-get update
sudo apt-get install -y liblapack-dev libblas-dev gfortran libfreetype6-dev libopenblas-base libopenmpi-dev libjpeg-dev zlib1g-dev
sudo apt-get install -y python3-pip

# Update Pip
python3 -m pip install --upgrade pip

# Install below necessary packages
# For numpy, first uninstall the version already installed, and then install numpy==1.19.0
numpy==1.19.0
pandas==0.22.0
Pillow==8.4.0
PyYAML==3.12
scipy==1.5.4
psutil
tqdm==4.64.1
imutils

# Install Pycuda
export PATH=/usr/local/cuda-10.2/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-10.2/lib64:$LD_LIBRARY_PATH
python3 -m pip install pycuda --user


Pycuda installations 
# Remember to give proper cuda path 10.2.0
https://forums.developer.nvidia.com/t/pycuda-installation-failure-on-jetson-nano/77152/4



# Install Seaborn
sudo apt install python3-seaborn

# Install torch & torchvision
wget https://nvidia.box.com/shared/static/fjtbno0vpo676a25cgvuqc1wty0fkkg6.whl -O torch-1.10.0-cp36-cp36m-linux_aarch64.whl
pip3 install torch-1.10.0-cp36-cp36m-linux_aarch64.whl
git clone --branch v0.11.1 https://github.com/pytorch/vision torchvision
cd torchvision
sudo python3 setup.py install 

# Not required but good library
jetson-stats==3.1.4
