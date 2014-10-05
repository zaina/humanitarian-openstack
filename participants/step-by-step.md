1. Install python 2.7 on Ubuntu (if you are using Mac, Windows, or other flavor of Linux, skip this step):
```
sudo apt-get install build-essentialsudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev
libgdbm-dev libc6-dev libbz2-dev
wget http://python.org/ftp/python/2.7.5/Python-2.7.5.tgz
tar -xvf Python-2.7.5.tgz
cd Python-2.7.5
./configuremakemake install
apt-get install git
```
2. Install pip:
```
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
```
3. Install and run virtual environment:
```
pip install virtualenv
virtualenv venv
source venv/bin/activategit 
```
4. Get code for the application from GitHub:
```
clone https://github.com/rackerlabs/humanitarian-openstack/cd humanitarian-openstack/participants/code/
```
5. Make sure you are in the humanitarian-openstack/participants/code directory:
```
cd humanitarian-openstack/participants/code
```
6. Install requirements:
```
pip install -r requirements.txt
```
7. Create 'libcloud.conf' file by coyping configuration template, pay attention to the name:
```
cp libcloud.conf.template libcloud.conf
```
8. User your favorite editor to edit the configuration file. Set the "identity" and "credential" values.
```
vi libcloud.conf
```
9. Edit case-1.py file. Rename "server-1", "server-2", "db", "haproxy" with your name, for example, "Susan-server1".
```
vi case-1.py
```
- Finally, Execute the code:
```
python case-1.py
```
