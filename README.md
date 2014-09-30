humanitarian-openstack
======================
volunteer_packet.txt
  Instructions for volunteers

usercases.txt
  Example usecases to implement for building fault tolerant, scalable architectures
  
code/ 
  
  deployment/
    Contains scripts to deploy webservers, databases, haproxy
  
  libcloud.conf
    Template file to include cloud provider details for libcloud
  
  case-1.py
    Implements code for usecase - 2 webservers with a load balancer and a database node
    
  To run the code:
    1. Set credentials in libcloud.conf
    2. Run python case-1.py
    Build your own use cases and try them!
