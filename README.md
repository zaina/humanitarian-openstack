humanitarian-openstack
======================
* volunteers/
  * volunteer_packet.txt- Instructions for volunteers

* usercases.txt - Example usecases to implement for building fault tolerant, scalable architectures

  
* participants/
  * code/ 
  
  deployment/ - Contains scripts to deploy webservers, databases, haproxy
  
  libcloud.conf - Template file to include cloud provider details for libcloud
  
  case-1.py - Implements code for usecase - 2 webservers with a load balancer and a database node
    
  To run the code:

    1. Set credentials in libcloud.conf

    2. Create a venv - http://docs.python-guide.org/en/latest/starting/install/linux/#virtualenv (optional)
    
    3. pip install -r participants/code/requirements.txt
    
    4. Run python case-1.py

    Build your own use cases and try them!
