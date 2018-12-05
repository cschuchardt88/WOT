import BigWorld

def init():
    BigWorld.serverDiscovery.searching = 1
    
    for server in BigWorld.serverDiscovery.servers:
            print server