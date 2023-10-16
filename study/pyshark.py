import sys
from scapy.all import *

while True:
    sniff(prn=lambda x: x.show())
