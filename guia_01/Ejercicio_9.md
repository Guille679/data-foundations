## Ejercicio 9 — Ordenamiento de cartas numeradas con un robot

**EJERCICIO DADO**
Tenés que explicarle a un robot cómo ordenar una pila de cartas numeradas del 1 al 10 que están desordenadas. El robot solo puede hacer estas acciones: mirar la carta de arriba de la pila, tomar una carta, dejar una carta en una de tres pilas auxiliares, y comparar dos cartas para ver cuál es mayor. Describí los pasos para que el robot ordene las cartas de menor a mayor.

**Objetivo:** Organizar una pila de 10 cartas desordenadas de menor a mayor (1 al 10) utilizando tres espacios auxiliares.

**Elementos necesarios:**

**ESTADO INICIAL (Entrada)**

Para que el robot opere, necesita identificar sus recursos:

- Pila A (Origen): Las 10 cartas desordenadas.
- Pila B (Auxiliar): Para mover cartas temporalmente mientras busca.
- Pila C (Destino): Donde quedará el mazo ordenado (el "estante").

**CAPACIDADES DEL ROBOT (Procesamiento)**
- Sensor visual: Mirar el valor de la carta superior.
- Manipulador: Tomar y dejar una carta por vez.
- Lógica: Comparar dos valores y determinar cuál es menor.


**Pasos:**
1. Búsqueda del Mínimo: El robot toma la primera carta de la Pila A y la memoriza como "la más chica encontrada hasta ahora".
2. Comparación Secuencial: Toma la siguiente carta de la Pila A. Si es menor que la que tiene en la mano, intercambia: deja la grande en la Pila B y se queda con la más chica. Si es mayor, la deja directamente en la Pila B.
3. Repetición de Ciclo: Repite el paso 2 hasta que la Pila A quede vacía. En su mano tendrá la carta más chica de todo el grupo.
4. Almacenamiento Final: Deja la carta que tiene en la mano en la Pila C (su primera carta del mazo ordenado).
5. Transferir todas las cartas de la Pila B a la Pila A, tomándolas de a una desde la cima de B y apilándolas en A.
6. Bucle de Finalización: Repite los pasos del 1 al 5 hasta que no queden cartas en la Pila A. El resultado será la Pila C con las cartas del 1 al 10.

