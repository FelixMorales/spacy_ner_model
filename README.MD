Instrucciones:

# Archivo de configuración
Crear/Actualizar el archivo de configuración (config.cfg) siguiendo las instrucciones en la documentacion de Spacy  (https://spacy.io/usage/training#quickstart)

# Entrenamiento
La data de entrenamiento y la data de validación del entrenamiento se encuentran en los archivos "data/training_data.json" y "data/validation_data.json" respectivamente, se puede modificar la data siempre y cuando se mantenga el formato actual de ambos archivos.

Una vez actualizado ambos archivos que contienen la data de entrenamiento y validación del entrenamiento, se deben parsear a "spacy format", para eso se debe ejecutar el script "format_data.py"

Finalmente, para entrenar el modelo se debe ejecutar el comando:

```shell
> python -m spacy train config.cfg --output ./
```

Esto generará el modelo entrenado en la carpeta "model-best"

# Validar entrenamiento
Escribir el texto de prueba en el archivo "test_data/test_text.txt" y luego ejecutar el script "test_custom_model.py" para validar el modelo entrenado usando el texto de prueba especificado.



Data de entrenamiento extraida del tutorial: https://www.youtube.com/watch?v=p_7hJvl7P2A
