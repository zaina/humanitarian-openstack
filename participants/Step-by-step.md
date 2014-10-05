Install on Linux:

Install python 2.7:
sudo apt-get install build-essentialsudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
wget http://python.org/ftp/python/2.7.5/Python-2.7.5.tgz
tar -xvf Python-2.7.5.tgz
cd Python-2.7.5
./configuremakemake install
apt-get install git
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install virtualenv
virtualenv venv
source venv/bin/activategit clone https://github.com/rackerlabs/humanitarian-openstack/cd humanitarian-openstack/participants/code/
pip install -r requirements.txt
cp libcloud.conf.template libcloud.conf
vi libcloud.confvi case-1.py
python case-1.py
