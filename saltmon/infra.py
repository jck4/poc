# infra.py:

import csv

class Generic_Instance():
  
  def __init__(self, name: str, 
                  network: str, 
                  subnet: str, 
                  ip: str, 
                  cpus: str, 
                  ram: str, 
                  storage: str, 
                  type:str , 
                  public: str):

    self.name = name
    self.network = network
    self.subnet = subnet
    self.ip = ip
    self.cpus = cpus
    self.ram = ram
    self.storage = storage
    self.type = type
    self.public = public

instances = list()

with open('infra.csv','r') as csv_file:
    servers = csv.DictReader(csv_file)
    for server in servers:
      instances.append(Generic_Instance(**server))


