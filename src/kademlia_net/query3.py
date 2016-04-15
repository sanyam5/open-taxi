from twisted.internet import reactor
from twisted.python import log
from kademlia.network import Server
from kademlia.crawling import NodeSpiderCrawl, ValueSpiderCrawl
from kademlia.node import Node
from kademlia.protocol import KademliaProtocol
from kademlia.storage import ForgetfulStorage, IStorage
import sys

log.startLogging(sys.stdout)

def done(result):
    print "Key result:", result
    reactor.stop()

def setDone(result, server):
    server.get("3").addCallback(done)

def bootstrapDone(found, server):
    server.set("3", "a value").addCallback(setDone, server)

# def bootdone(found, server):
peer = Node(id = "2000", ip='127.0.0.1', port='5672')
kp = KademliaProtocol(sourceNode=peer, storage=ForgetfulStorage(), ksize=20)
# nodetofind = Node("3000", ip='127.0.0.1', port='5673')
nodetofind = Node("3000")
crawl = ValueSpiderCrawl(protocol=kp, node=nodetofind, peers=[peer], ksize=20, alpha=3)
# crawl = NodeSpiderCrawl(protocol=kp, node=nodetofind, peers=[peer], ksize=20, alpha=3)

print crawl.find()
# server = Server(ksize=1)
# server.listen(6777)
# # server.bootstrap([('127.0.0.1', 8468)]).addCallback(bootstrapDone, server)
# server.bootstrap([('127.0.0.1', 8468)]).addCallback(bootdone, server)


reactor.run()
