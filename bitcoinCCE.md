---
layout: page
title: Bitcoin - CCE
---

## ¿Por qué se utiliza Criptografía de Curva Elíptica en Bitcoin? ECDSA (VI)

> ECDSA. Elliptic Curve Digital Signature Algorithm es una modificación del algoritmo DSA que emplea operaciones sobre puntos de curvas elípticas en lugar de las exponenciaciones que usa DSA (problema del logaritmo discreto). La principal ventaja de este esquema es que requiere números de tamaños menores para brindar la misma seguridad que DSA o RSA. Existen dos tipos de curvas dependiendo del campo finito en el que se definan, que pueden ser GF(P) o GF(2m).

El protocolo Bitcoin utiliza el algoritmo ECDSA (Elliptic Curve Digital Signature Algorithm) para la creación de claves privadas y públicas. ECDSA es una variante del Digital Signature Algorithm (DSA) que utiliza la criptografía de curva elíptica (Elliptic curve cryptography – ECC) como variante de la criptografía asimétrica o de clave pública. En este artículo vamos a describir las principales características de la criptografía de curva elíptica y su aplicación en el protocolo Bitcoin.

La criptografía de curva elíptica puede ser más rápida y usar claves más cortas que los métodos antiguos — como RSA — al tiempo que proporcionan un nivel de seguridad superior.

Los primeros algoritmos de cifrado de clave pública se basaban en la factorización de números primos grandes, tal como describimos en nuestro artículo sobre las bases matemáticas del algoritmo RSA, pero estos ya no se consideran seguros cuando se cuándo utilizan claves cortas. La criptografía de curva elíptica con los actuales medios técnicos genera claves “intractable” en inglés, que traducido al español significa “difícil de resolver” pero no imposible, aunque con la tecnología actual tardaría miles de años.

## ¿Por qué utiliza el protocolo de Bitcoin criptografía de curva elíptica?

Uno de los problemas más importantes al que se tenía que enfrentar Satoshi Nakamoto cuando creó el protocolo Bitcoin fue la distribución de las claves públicas. Era importante poder utilizar claves públicas cortas, pero seguras que se pudieran compartir en códigos QR, imprimir en dispositivos físicos y compartir por teléfono si hacía falta.

La principal ventaja de la criptografía de curva elíptica es la posibilidad de crear claves más pequeñas, reduciendo así requisitos de almacenamiento y transmisión. Una clave basada en la criptografía de curva elíptica puede dar el mismo nivel de seguridad con un clave de 256 bits como un algoritmo RSA con una clave de 2048 bits.

El algoritmo ECDSA crea claves de 256 bits de longitud codificados con el sistema de numeración posicional Base58 de Bitcoin que da claves de 44 dígitos sin incluir el número de versión o dígitos de control. Una clave con RSA necesitaría de 350 dígitos.

La razón principal para utilizar criptografía de curva elíptica era pues facilitar el manejo de las direcciones públicas del protocolo Bitcoin.

Aun así, Satoshi Nakamoto decidió que los 44 dígitos eran demasiados para una dirección pública y decidió aplicar un proceso de funciones hash para la creación de las claves públicas que explicaremos en otro artículo. La clave pública ECDSA inicial acaba al final de ese proceso de hash en 160 bits que, incluyendo los datos de versión y los dígitos de control, tienen desde 27 a 34 dígitos. Por ejemplo como esta dirección pública: 1DZEazabbJqtr2uciLFNxvgm1GBuS5kaej
