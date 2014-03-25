from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(

    darkcoin=math.Object(
        PARENT=networks.nets['darkcoin'],
        SHARE_PERIOD=15, # seconds
        NEW_SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
        SPREAD=30, # blocks
        NEW_SPREAD=30, # blocks
        IDENTIFIER='496247d46a00c115'.decode('hex'),
        PREFIX='5685a273806675db'.decode('hex'),
        P2P_PORT=7902,
        MIN_TARGET=4,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=7903,
        BOOTSTRAP_ADDRS='p2phash.com asia02.poolhash.org asia01.poolhash.org 157.56.161.11 54.186.8.140 62.141.39.175 mightypool.net 85.131.127.26 213.229.88.102 cryptohasher.net darkcoin.fr'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-drk',
        VERSION_CHECK=lambda v: True,
    ),


    darkcoin_testnet=math.Object(
        PARENT=networks.nets['darkcoin_testnet'],
        SHARE_PERIOD=15, # seconds
        NEW_SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
        SPREAD=30, # blocks
        NEW_SPREAD=30, # blocks
        IDENTIFIER='17cf94c1ae12e98f'.decode('hex'),
        PREFIX='5559f46dfee6881f'.decode('hex'),
        P2P_PORT=17902,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=13990,
        BOOTSTRAP_ADDRS=''.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-drk',
        VERSION_CHECK=lambda v: True,
    ),

)
for net_name, net in nets.iteritems():
    net.NAME = net_name
