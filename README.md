# StopWatch

Módulo mediante el cual cronometrar secciones de código.

Para cronometrar una sección de código instanciar un `StopWatch` y, antes de la sección en cuestión, iniciar el reloj con `start()`, para luego de la misma detenerlo con `stop()`. Note que el método `stop()` retorna el tiempo transcurrido, en segundos, desde la última llamada a `start()`.

## Ejemplo:

```python
import numpy as np
from binary_search import binary_search

if __name__ == "__main__":
  
  example_arr = np.arange(0, 1001)

  stopwatch = StopWatch()
  stopwatch.start()
  index = binary_search(example_arr, 42)
  elapsed_time_ms = 1000 * stopwatch.stop()
```
En el ejemplo anterior tenemos un caso en que nos interesa cronometrar el tiempo que demora una implementación particular de búsqueda binaria, en encontrar el indice en que se sitúa el número 42 dentro del arreglo `example_arr` (en el cual se encuentran todos los numeros naturales del 0 al 1000, de manera ordenada), donde finalmente guardamos el tiempo, convertido a milisegundos, en la variable `elapsed_time_ms`.
