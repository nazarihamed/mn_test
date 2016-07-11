#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
from mininet.clean import Cleanup

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   link=TCLink,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c1=net.addController(name='c1',
                      controller=RemoteController,
                      ip='10.0.0.3',
                      protocol='tcp',
                      port=6653)
    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch, inband=True)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch, inband=True)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch, inband=True)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch, inband=True)
    
    

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(s1, s2,delay='100ms')
    net.addLink(h3, s2)
    net.addLink(h4, s2)
    net.addLink(s2, s3, delay='1000ms')
    net.addLink(h5, s3)
    net.addLink(h6, s3)
    net.addLink(s3, s4, delay='1000ms')
    net.addLink(h7, s4)
    net.addLink(h8, s4)
    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start(net.controllers)
    net.get('s2').start(net.controllers)
    net.get('s3').start(net.controllers)
    net.get('s4').start(net.controllers)
    
    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()
    Cleanup.cleanup()
