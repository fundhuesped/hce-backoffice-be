# Historia Clinica Electronica - Backend
Este repositorio contiene el servidor de logica de negocio del sistema de Historia Clinica Electronica


## Despliegues e Instalación en ambientes
Siendo root en el servidor a elección con el codigo del repositorio clonado ejecutar:
 
`git pull #Traer ultimos cambios`
`cd /carpeta-donde-estan-variables-de-entorno`
`source setenv.sh  #Levantar las variables de entorno`
`./start_docker.sh  #Levantar docker compose`
`docker ps # Verificar estan levantados los 3 docker`

## Luego correr las background tasks que cierra las sesiones automaticamente al finalizar el dia y procesa importaciones que tardan mucho
`docker exec -d hcebackoffice_be_1 python manage.py process_tasks`

## Si es necesario aplicar las migraciones a la base de datos:
`docker exec -ti hcebackoffice_be_1 /bin/bash`
`python manage.py migrate`

## Para debugging de problemas viendo los logs del docker creado:
`docker logs --tail 300 hcebackoffice_be_1`

