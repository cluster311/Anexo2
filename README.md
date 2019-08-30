# Anexo II
Generación para impresión del "Comprobante de Atención de Beneficiarios de Obras Sociales" (Conocido como Anexo II).  
Según [Resolucion 487/2002](http://servicios.infoleg.gob.ar/infolegInternet/anexos/75000-79999/77280/texact.htm).  

```
Art. 2° — Los Hospitales Públicos de Gestión Descentralizada deberán 
  cumplimentar el "Comprobante de Atención de Beneficiarios de Obras Sociales", 
  que se agrega como Anexo II, que pasa a formar parte integrante de la presente 
  Resolución, con carácter de Declaración Jurada, firmado por el médico actuante 
  o Jefe del Servicio, con sello y número de matrícula, y el responsable 
  administrativo del Hospital, con sello, cargo y aclaración de firma, 
  con la correspondiente suscripción o firma del beneficiario, 
  familiar o responsable.
```
Documento original usado de base [acá](originales/Anexo-II-RESOLUCION-487-2002.gif).  

## Herramienta desarrollada

Este instrumento toma un diccionario con datos y genera un HTML listo para imprimir, firmar y sellar.  

## Instalacion 

```
pip install anexo2
```

## Uso

```python
hostpital = {}
beneficiario = {}
obra_social = {}
data = {
  'hospital': hostpital,
  'beneficiario': beneficiario,
  'obra_social': obra_social
}
from anexo2.docs import Anexo2
anx = Anexo2(data=data)
print(anx.get_html())
```

Resultado
```html
<html>
</html>
```


