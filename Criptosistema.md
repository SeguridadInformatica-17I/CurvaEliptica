---
layout: page
title: Criptosistema
---

Un [Criptosistema](http://www.segu-info.com.ar/criptologia/criptosistema.htm) se define como la quíntupla (m,C,K,E,D), donde:

* m representa el conjunto de todos los mensajes sin cifrar (texto plano) que pueden ser enviados.
* C Representa el conjunto de todos los posibles mensajes cifrados, o criptogramas.
* K representa el conjunto de claves que se pueden emplear en el Criptosistema.
* E es el conjunto de transformaciones de cifrado o familia de funciones que se aplica a cada elemento de m para obtener un elemento de C. Existe una transformación diferente Ek para cada valor posible de la clave K.
* D es el conjunto de transformaciones de descifrado, análogo a E.

Todo Criptosistema cumple la condición Dk(Ek(m))=m.

Existen dos tipos fundamentales de Criptosistemas utilizados para cifrar datos e información digital y ser enviados posteriormente después por medios de transmisión libre.

* Simétricos o de clave privada: se emplea la misma clave K para cifrar y descifrar, por lo tanto el emisor y el receptor deben poseer la clave. El mayor inconveniente que presentan es que se debe contar con un canal seguro para la transmisión de dicha clave.

* Asimétricos o de llave pública:se emplea una doble clave conocidas como Kp (clave privada) y KP (clave Pública). Una de ellas es utilizada para la transformación E de cifrado y la otra para el descifrado D. En muchos de los sistemas existentes estas clave son intercambiables, es decir que si empleamos una para cifrar se utiliza la otra para descifrar y viceversa.

[back to the homepage]({{ site.baseurl }}).
