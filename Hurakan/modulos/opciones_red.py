# funcion de herramientas de red
import os


def red(selec):
    comandos_red = {1: "ipconfig /release",2: "ipconfig /renew",3: "ipconfig /flushdns",4: "arp -a",5: "nersh int ip reset",6: "netsh winsock reset",7: "netsh dns cache delete" }
    selcec_red = comandos_red[selec]
    os.system(selcec_red)