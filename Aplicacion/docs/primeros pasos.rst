primeros pasos
=====

Guía de uso
------------

Descripción:
La aplicación permite almacenar y manipular una base de datos de temperatura horaria de C.A.B.A. para un día determinado, permitiendo al usuario realizar las siguientes acciones:

1- Agregar datos horarios de temperatura a medida que estos se miden con instrumento.

2- Consultar un dato de temperatura determinado en una hora determinada.

3- Modificar un dato de temperatura (por ejemplo si se considera que hubo un error del instrumento y se realizó nuevamente la medición).

4- Eliminar un dato de temperatura (similar al ejemplo anterior, pero pasó demasiado tiempo como para volver a tomar el dato de esa hora).

5- Presentar los datos de forma gráfica para analizar.

Funcionamiento:

1. Al ejecutar la aplicación, la misma abre una ventana indicando las referencias y formato de datos a ingresar. Una vez informado, el usuario la debe cerrar para continuar.

2. Una vez realizado esto, se abre automáticamente la interface de la aplicación.

3. Relativo a los archivos que utiliza la aplicación:   

   3.1. Si en el directorio ya existe un archivo "mibase.db", se puede trabajar sobre ella desde un inicio (por ejemplo visualizar el gráfico on consultar datos). Caso contrario, primero habrá que dar de alta al menos un dato o se acentará un error en el registro "log.txt".

   3.2. Si en el directorio ya existe un archivo "mibase.db" y/o "marcha.png", se puede visualizar el gráfico desde un inicio. Caso contrario, primero habrá que dar de alta al menos un valor o se acentará un error en el registro "log.txt".

4. Relativo a las funcionalidades:

   4.1. Alta: Solo se pueden ingresar datos en horas no repetidas, de lo contrario se acentará un error en el registro "log.txt".

   4.2. Modificación: Permite modificar un valor de temperatura en un horario en el que ya exista un registro "log.txt".

   4.3. Baja: Solo se podrá dar de baja registros en horas dadas de alta previamente, caso contrario se acentará un error en el registro "log.txt".

   4.4. Consulta: Solo se podrá dar de consultar registros en horas dadas de alta previamente, caso contrario se acentará un error en el registro "log.txt".
