?
m??\w2  ?            	   @   s?  d  Z  d d l Td d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z
 d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d a e j d ? a e j d ? a e e j ?  ? j d d ? Z e e j ?  ? j d d ? Z d	 Z d a e j d
 d d d d d d d ? Z e j ?  a  d d d d d d d d g a! d d ?  Z" d d ?  Z# d d ?  Z$ d d ?  Z% d d ?  Z& d d ?  Z' d d ?  Z( d  d! ?  Z) d" d# ?  Z* d$ d% ?  Z+ e j j, ?  Z- e- e j. d& d/ ? Z/ e e/ ? j0 d( ? Z1 e1 d j0 d) ? Z2 e2 d* d+ e2 d' d+ e2 d Z3 e j j, ?  Z- e e- ? j0 d( ? Z4 e4 d j0 d) ? Z5 e5 d* d+ e5 d' d+ e5 d Z6 e j d ? Z7 e8 d, d- ? Z9 e9 j: ?  Z; e9 j< ?  e; j0 d. ? Z; e6 d( e e7 ? Z= e; d Z> e; d' Z? e; d* Z@ eA e> e= ? e+ e> e= e e? ? e e@ ? ? d S)0u  
Estacionamientos unicos de México
Este archivo es para remplaar a acceso4.py
Funcion: 		Funcion de imprimir boleto
Descripcion:	

Funciones que se pueden usar:
	1) imprimirBoletoT tiempo corto formato largo
	2) imprimirBoleto  tiempo largo formato pequeño

?    )?*N?6z%Y-%m-%dz%H:%M:%S?
? zA/home/pi/Documents/eum/app/caseta/EUM_EXPE/CodigosQR/outputQR.png?database?caseta?user?postgres?password?Postgres3UMd6?host?	localhostc              C   s?   t  j d d ? }  |  j d d d d ? |  j d t t ? d ? |  j d d	 d d ? |  j d
 ? |  j d ? |  j d ? d  S)Ni  ?   ?size?2x?align?centerzBienvenido 
r   ?normalz?La empresa no se hace responsable por objetos
personales,fallas mecanicas  y/o  electricas,
siestros ocasionados por derrumedbes,temblores,
terremotos o fenomenos naturales,asi como ro-
bo de accesorios o vandalismo en su vehiculo.
z?Por robo total de acuerdo a los terminos  del
seguro contratado.Boleto Perdido.Se entregara
el  vehiculo  a quien acredite la  propiedad.
Costo del boleto perdido es de $100.00
z?Al recibir este boleto acepta las condiciones
del seguro contra robo total. PARKING TIP S.A
DE  C.V.  -R.F.C PTI120210571. Escobillera 13
Col.Paseos de Churubusco Iztapalapa CDMX C.P.
09030 Horario de Lunes-Domingo de 7 a 22 hrs 
)?printer?Usb?set?text?str?PATH_NOMBRE_PLAZA)?Generic? r   ?./home/pi/Documents/eum/app/caseta/corte/rt2.py?imprimirHeader(   s    r   c             C   s?   t  j d d ? } | j d t d ? | j d t |  ? d | d | d ? | j |  d | d | d | ? | j ?  d  S)Ni  r   zExpedidora #r   z	Folio: GM? )r   r   r   ?PATH_NUMERO_TERMINALr   ?qr?cut)ZnoBolZterminalEntZfechaIn?horaEntr   r   r   r   ?
imprimirQR2   s
    +%r#   c             C   s  t  j d d ? } t j t ? } t  j d d ? } | j d d d d ? | j d t t ? d ? | j d d	 d d ? | j d
 ? | j d ? | j d ? t	 j
 d ? } | j d t |  ? d ? | j d t d | d | d ? | j | ? | j ?  d  S)Ni  r   r   r   r   r   zBienvenido 
r   r   z?La empresa no se hace responsable por objetos
personales,fallas mecanicas  y/o  electricas,
siestros ocasionados por derrumbes,temblores,
terremotos o fenomenos naturales,asi como ro-
bo de accesorios o vandalismo en su vehiculo.
z?Por robo total de acuerdo a los terminos  del
seguro contratado.Boleto Perdido.Se entregara
el  vehiculo  a quien acredite la  propiedad.
Costo del boleto perdido es de $100.00
z?Al recibir este boleto acepta las condiciones
del seguro contra robo total. PARKING TIP S.A
DE  C.V.  -R.F.C PTI120210571. Escobillera 13
Col.Paseos de Churubusco Iztapalapa CDMX C.P.
09030 Horario de Lunes-Domingo de 7 a 22 hrs 
z%H:%M:%SzFolio: zExpedirora #r   )r   r   ?imagen?cambiarTamQR?PATH_CODIGOS_QRr   r   r   r   ?time?strftimer   ?imager!   )?folio?terminal?fechar   ?codQR?
horaActualr   r   r   ?imprimirBoletoT<   s    %r/   c             C   sV  t  d t d ? t  d t d ? t  |  d ? t j d d d d ? t j t t ? d ? t j d d	 d d ? t j d
 ? } t j d | d d |  d d | d d t | ? d ? t j	 | d | d |  d | d | d t | ? d ? t j d d	 d d ? t j d ? t j d d d d ? t j d ? t j
 ?  d  S)NzBienvenido 
 r   zExpedirora: r   r   r   r   z

r   z%H:%M:%SzHora de entrada:z    zFecha: zHora de Pago:z      z	Pagado: $z.00
z+
Presentar al salir. Valido por 15 minutos
zGracias por su visita!)?printr   r   r   r   r   r   r'   r(   r    r!   )r,   ZhoraEntradaZcostillor*   Z
expedidorar.   r   r   r   ?imprimirBoletoC2N   s    ??r1   c             C   s  t  j d d ? } t j t ? } t d t d ? t d ? t d t |  ? d ? t d t d ? t | d ? t d t | ? ? t  j d d ? } | j	 d	 d
 d d ? | j
 t t ? d ? | j	 d	 d d d ? t j d ? } | j
 d | d d | d d | d d ? | j | ? | j	 d	 d d d ? | j
 d ? | j	 d	 d
 d d ? | j
 d ? | j ?  d  S)Ni  r   zBienvenido 
 r   zTerminos y condicioneszFolio: zExpedirora: zCODIGO QR: r   r   r   r   z

r   z%H:%M:%SzEntrada:z    zFecha: zSalida:zPagado: $100.00
z+
Presentar al salir. Valido por 15 minutos
zGracias por su visita!)r   r   r$   r%   r&   r0   r   r   r   r   r   r'   r(   r)   r!   )r*   r+   r,   r   r-   r.   r   r   r   ?imprimirBoletoCg   s(    
1r2   c             C   s?   t  j d d d d ? t j d ? } t  j d d d d ? t  j d ? t  j d ? t  j d	 ? t  j d d
 ? t  j d t |  ? d ? t  j d t | ? d ? t  j | d ? t  j d d d d ? t  j | ? t  j ?  d  S)Nr   r   r   r   z
output.pngzMacro Plazar   z TECAMACz3.jpgr   zFolio: z	Entrada: zMacro Plaza
z	 TECAMAC
)r   r   r$   r%   r   r)   r   r!   )r*   r+   r,   r-   r   r   r   ?imprimirBoleto?   s    
r3   c              C   sY   t  j d d ? }  |  j d d d d ? |  j d t t ? ? |  j d d d d ? d  S)	Ni  r   r   r   r   r   zBienvenido 
r   )r   r   r   r   r   r   )r   r   r   r   ?header?   s    r4   c               C   s   t  j ?  d  S)N)r   r!   r   r   r   r   ?footer?   s    r5   c               C   s'   t  j d d d d ? t  j d ? d  S)Nr   r   r   r   zBienvenido

)r   r   r   r   r   r   r   ?informacionEXT?   s    r6   c       "      C   s?  d } t  j ?  } t d d ? } | j ?  } | j d ? } | d }	 | d }
 | d } | j ?  d } t j d	 |  d
 | d ? x> t D]6 } | t | d ? d t t	 | d ? ? d } q? Wt
 | ? t j d |  d
 | d ? xC t D]; } t | d ? } | d k r!d } q? t	 | d ? } q? Wt j d d d d d d d d ? } | j ?  a | j ?  } t
 |  | ? t j d |  d
 | d ? x? t D]? } t
 d | d | d ? | j d t | d ? d ? x | D] } t
 | d ? q?Wt
 d t ? t
 d | d | d ? | d t t	 | d ? d <t
 d t ? t d  t | d ? d! t | d ? d a q?Wt j d |  d
 | d ? x t D] } t
 | d ? q?Wd" } d" } d" } d" } d" } d" } d" } d" } d" } d" } d" } | d# |	 d$ | d# t | ? d# | d# t | ? d# t t d% ? d# t t d& ? d# t t d' ? d# t t d( ? d# | d# | d# | d# | d# t t d ? d# t | ? d# | d# | d# | d# | d# | d# | d# | a t j d) d' d* d( d+ d' ? } t j d, ? } t
 d- | ? | d k r?yY | j t ? | j d. d/ ? | j d0 d1 ? } t d2 d3 ? } | j | ? | j ?  Wq?t
 d4 ? d5 SYq?Xn/yt
 d6 | ? d7 | k r?d8 } n d9 } i | d: 6d" d; 6t t d% ? d< 6d" d= 6t | ? d> 6t t d& ? d? 6t t d' ? d@ 6t t d( ? dA 6d" dB 6| dC 6| dD 6t | ? dE 6t dF t dG 6t | ? dH 6| dI 6dJ dK 6t dL 6}  t j dM dN |  ?}! t
 dO |! j dP | ? Wn t
 dQ ? dR SYn Xd  S)SN?-z;/home/pi/Documents/eum/app/caseta/archivos_config/datos.txt?r?,r   r   ?   r   zNselect costo,COUNT("idBoleto") from "BOLETO" where "fechaExpedicion" BETWEEN 'z' and 'z' group by costo ?:r   zCselect SUM("costo") from "BOLETO" where "fechaExpedicion" BETWEEN '?'?Noner   r   r   r	   r
   r   r   r   zMselect tipo,COUNT("idBoleto") from "BOLETO" where "fechaExpedicion" BETWEEN 'z' group by tipo Ztipazosz)select nombre from "TIPO" where "idTipo"=ZTIPOSSSSSSSSSSSSSSSSS1ZTIPOSSSSSSSSSSSSSSSSS2ZTIPOSSSSSSSSSSSSSSSSS3zPagos z --> ?0?;z; ;?   ?   ?   ?   ?versionZbox_sizeZborderz'ping -c 1 parkingtip.pythonanywhere.com?conexionServZfitTZ
back_colorZblackz//home/pi/Documents/eum/app/iconos/outputQR2.png?wbz#Error de registro del corte privadozError registro corte privadozturno:?VZ
VespertinoZMatutino?turno?boletajeZrecuperadosZselladosZ
noSelladosZincompletosZpropinaZ
sinpropina?	cortesias?toleranciasZ
locatariosZcaja?TZcreatedZingresoZdetalles?1Z	encargadoZsucursal_idz8https://parkingtip.pythonanywhere.com/api/cortes/create/?jsonz
Result...:z, turno:z#Error de registro del corte publicozError registro corte publico)?horaZmostrarFechayHora?open?readline?split?close?curZexecuter   ?intr0   ?psycopg2?connect?cursor?tipos?dats?qrcodeZQRCode?os?systemZadd_dataZmakeZ
make_imageZsave?fechaHoy?horaHoy?sucursal?requestsZpostr   )"?fecha1?fecha2rH   r*   rI   r,   ?infileZdatosZarrZplazaZ	localidadZidCajeroZtotZreg?connZcur2ZregaZsinSelloZlocalesZ
canceladosZproovedoresrK   rJ   ZgastosZnominaZbonosZdobletesZanticipoDeDepositosr    rE   Zimg?fZpayloadr8   r   r   r   ?checale?   s?    



4
	$2?		
	

rg   Zdaysr   r   r7   r:   ?/zB/home/pi/Documents/eum/app/caseta/archivos_config/fechaDeCorte.txtr8   r9   ?????)B?__doc__ZescposprinterZtratarImagenr$   ZconfiguracionEXPZarchivoConfiguracionr'   rV   Zpsycopg2.extrasZfechaUTCrO   Zdatetimer[   ra   rN   r\   ?sysr`   r(   r^   r_   r   ZgetName?replacer   Z	getNumTerr   r&   rZ   rW   re   rX   rT   rY   r   r#   r/   r1   r2   r3   r4   r5   r6   rg   ZtodayZhoyZ	timedeltaZayerrR   ?m?nZ	fechaayer?a?bZfecr"   rP   rd   rQ   ?crS   rc   rb   rH   r*   r0   r   r   r   r   ?<module>   sf   
$

?""



