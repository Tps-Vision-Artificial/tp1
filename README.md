# Trabajo Practico N 1
## Proyecto
Los alumnos elegirán al menos tres objetos reconocibles por su contorno, usarán una imagen de cada uno como referencia de cada tipo de objeto, y les asignarán un nombre a cada uno.
Prepararán el ambiente controlado para evitar correcciones por software que de otro modo pueden resultar muy demandantes, y así poder concentrarse en el objetivo del proyecto.
El sistema detectará y clasificará los objetos en la imagen de la webcam en tiempo real.

## Output

La salida del sistema es una ventana con la imagen original anotada de la siguiente manera:
  localización de objetos relevantes
    en verde para objetos reconocidos
      alternativamente se puede asignar un color particular a cada clase de objeto
    en rojo para objetos desconocidos
    evitando mostrar contornos de ruidos y elementos espúreos
    se puede anotar el contorno del objeto o un rectángulo que lo contenga
  etiqueta con el nombre del objeto

Se puede decorar la imagen con anotaciones adicionales.  Las anotaciones se pueden hacer sobre la imagen completa o sobre la región de interés, y se puede usar la versión color o en escala de grises.  Es válido y deseable mostrar otras ventanas con pasos intermedios.

