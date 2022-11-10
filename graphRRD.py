import rrdtool
import time
from reportlab.pdfgen import canvas

tiempo_actual = int(time.time())
mi = 0
con = 0
seg = 0
print("GENERAR REPORTE\n")
print("Cuantos minutos de reporte quieres? ")
mi = input()
con = int(mi)
seg = int(con*60)
print(seg)
tiempo_inicial = tiempo_actual - seg

ret = rrdtool.graph( "PaquetesUnicast.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_actual),
                     "--vertical-label=Bytes/s",
                     "--title=Paquetes unicast que ha recibido una interfaz\n Usando SNMP y RRDtools",
                     "DEF:PaquetesRecibidosU=traficoRED.rrd:inoctets:AVERAGE",
                     "CDEF:escalaIn=PaquetesRecibidosU,8,*",
                     "CDEF:Nivel1=escalaIn,5,LT,0,escalaIn,IF",
                     "VDEF:maximoIn=escalaIn,MAXIMUM",
                     "LINE3:escalaIn#FF0000:Paquetes de entrada",
                     "LINE3:Nivel1#00FF00:Paquetes de entrada(Nivel 1)")

ret = rrdtool.graph( "PaquetesRecibidos.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_actual),
                     "--vertical-label=Bytes/s",
                     "--title=Paquetes recibidos a protocolo IPv4, incluyendo los que tienen erroes \n Usando SNMP y RRDtools",
                     "DEF:PaquetesRecibidos=traficoRED.rrd:inoctet:AVERAGE",
                     "CDEF:escalaIn=PaquetesRecibidos,8,*",
                     "CDEF:Nivel1=escalaIn,5,LT,0,escalaIn,IF",
                     "VDEF:maximoIn=escalaIn,MAXIMUM",
                     "LINE3:escalaIn#FF0000:Paquetes Recibidos",
                     "LINE3:Nivel1#00FF00:Paquetes Recibidos(Nivel 1)")

ret = rrdtool.graph( "MensajesIcmp.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_actual),
                     "--vertical-label=Bytes/s",
                     "--title=Mensajes recibidos echo que ha enviado el agente \n Usando SNMP y RRDtools",
                     "DEF:PaquetesRecibidos=traficoRED.rrd:inocte:AVERAGE",
                     "CDEF:escalaIn=PaquetesRecibidos,8,*",
                     "CDEF:Nivel1=escalaIn,5,LT,0,escalaIn,IF",
                     "VDEF:maximoIn=escalaIn,MAXIMUM",
                     "LINE3:escalaIn#FF0000:Mensajes Recibidos",
                     "LINE3:Nivel1#00FF00:Mensajes Recibidos(Nivel 1)")

ret = rrdtool.graph( "SegmentosRecibidos.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_actual),
                     "--vertical-label=Bytes/s",
                     "--title=Segmentos recibidos, incluyendo los que se han recibido con errores\n Usando SNMP y RRDtools",
                     "DEF:PaquetesRecibidos=traficoRED.rrd:inoct:AVERAGE",
                     "CDEF:escalaIn=PaquetesRecibidos,8,*",
                     "CDEF:Nivel1=escalaIn,5,LT,0,escalaIn,IF",
                     "VDEF:maximoIn=escalaIn,MAXIMUM",
                     "LINE3:escalaIn#FF0000:Segmentos Recibidos",
                     "LINE3:Nivel1#00FF00:Segmentos  Recibidos(Nivel 1)")

ret = rrdtool.graph( "DatagramasEntregados.png",
                     "--start",str(tiempo_inicial),
                     "--end",str(tiempo_actual),
                     "--vertical-label=Bytes/s",
                     "--title=Datagramas entregas a usuario UDP\n Usando SNMP y RRDtools",
                     "DEF:PaquetesRecibidos=traficoRED.rrd:inoc:AVERAGE",
                     "CDEF:escalaIn=PaquetesRecibidos,8,*",
                     "CDEF:Nivel1=escalaIn,5,LT,0,escalaIn,IF",
                     "VDEF:maximoIn=escalaIn,MAXIMUM",
                     "LINE3:escalaIn#FF0000:Datgramas Entragados",
                     "LINE3:Nivel1#00FF00:Datgramas Entregados(Nivel 1)")

c = canvas.Canvas('Contabilidad.pdf')
c.drawString(50,800,"Administracion de Servicios en Red"),
c.drawString(50,775,"Practica 2"),
c.drawString(50,750,"Christian Fernan Reyes Gonzalez    4CM13"),
c.drawString(50,725,"Administracion de Contabilidad")
c.drawImage("PaquetesUnicast.png", 0, 500, width=275,height=175),
c.drawImage("PaquetesRecibidos.png", 300, 500, width=275,height=175)
c.drawImage("MensajesIcmp.png", 0, 300, width=275,height=175),
c.drawImage("SegmentosRecibidos.png", 300,300, width=275,height=175),
c.drawImage("DatagramasEntregados.png", 175,100,width=275,height=175)

c.save()