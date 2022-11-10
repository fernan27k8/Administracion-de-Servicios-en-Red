import time
import rrdtool
from getSNMP import consultaSNMP

paquete_unicast = 0
paquete_recib_ip = 0
mensajes_icmp = 0
segmentos_recib = 0
datagramas_entregados = 0

while 1:
    paquete_unicast = int(
        consultaSNMP('comunidadASRwin','172.100.85.132',
                     '1.3.6.1.2.1.2.2.1.1.1'))
    paquete_recib_ip = int(
        consultaSNMP('comunidadASRwin','172.100.85.132',
                     '1.3.6.1.2.1.2.2.1.14.1'))
    mensajes_icmp = int(
        consultaSNMP('comunidadASRwin','172.100.85.132',
                     '1.3.6.1.2.1.5.21.0'))
    segmentos_recib = int(
        consultaSNMP('comunidadASRwin','172.100.85.132',
                     '1.3.6.1.2.1.6.10.0'))
    datagramas_entregados = int(
        consultaSNMP('comunidadASRwin','172.100.85.132',
                     '1.3.6.1.2.1.7.1.0'))

    valor = "N:" + str(paquete_unicast) + ':' + str(paquete_recib_ip) + ':' + str(mensajes_icmp) + ':' + str(segmentos_recib) + ':' + str(datagramas_entregados)
    print (valor)

    rrdtool.update('traficoRED.rrd', valor)
    rrdtool.dump('traficoRED.rrd','traficoRED.xml')
    time.sleep(1)

if ret:
    print (rrdtool.error())
    time.sleep(300)