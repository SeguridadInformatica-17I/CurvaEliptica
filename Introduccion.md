---
layout: page
title: Introduccion
---
# Introducción
En los sistemas de criptografía asimétrica se utiliza 2 tipos de claves, las cuales son: la clave pública y la clave privada. En la cual mediante conceptos matemáticos podemos tener la certeza que conseguir la clave privada en cada unas de la partes(cifrado y descifrado) no sean faciles de calcular conociéndose la clave pública.

Este tipo de sistemas nos ayudan a encontrar solución a ciertos problemas matemáticos, como puede ser la realización de tests de primalidad, la factorización de números enteros, la
demostración del último teorema de Fermat o el logaritmo discreto, donde g e y son elementos de un grupo cíclico finito G, y x la solución a la ecuación $g^{x} = y$ $<=>$ $x = log_{y}$, este puede ser un problema de complejidad exponencial para ciertos grupos finitos de gran tamaño, sin embargo el problema inverso, puede ser resuelto mediante exponenciación discreta.

Un criptosistema basado en curva el ́ıptica puede lograr:
* menores longitudes de las claves
    * mayor rapidez de calculo
    * menos memoria y ahorro en transferencia de los datos
* con seguridad equivalente
* cuando se compara con criptosistemas clásicos, como el RSA

### Tamaño de las claves

![](/img/ima3.png)

### Curva elíptica

Una curva elíptica sobre un cuerpo $K$ es una curva algebraica sin puntos singulares que viene dada por una ecuación del tipo:

$$y^{2} + a_{1}xy + a_{3}y=x^{3} + a_{2}x^{2} + a_{4}x+a_{6},a_{i}∈K,$$

denominada ecuación general de Weierstrass.

Una curva el ́ıptica E(K) es:
* el conjunto de puntos que satisfacen la ecuaci ́on
* mas un punto O en el infinito

Según la característica del cuerpo K, usamos transformaciones lineales para simplificar la ecuación.

Con el conjunto de puntos G que forman la curva (i.e., todas las soluciones de la ecuación más un punto O, llamado punto en el infinito) más una operación aditiva +, se forma un grupo abeliano. Si las coordenadas x e y se escogen desde un cuerpo finito, entonces estamos en presencia de un grupo abeliano finito. El problema del logaritmo discreto sobre este conjunto de puntos (PLDCE) se cree que es más difícil de resolver que el correspondiente a los cuerpos finitos (PLD). De esta manera, las longitudes de claves en criptografía de curva elíptica pueden ser más cortas con un nivel de seguridad comparable.

[back to the homepage]({{ site.baseurl }}).
