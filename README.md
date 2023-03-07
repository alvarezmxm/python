#Pasos del juego de piedra, papel o tijera.

Para correr el juego debes de seguir las siguientes instrucciones en la TERMINAL:

```sh
cd juego
python3 main.py

```

#Graficas2

Para correr el programa de las graficas debes de seguir los siguientes pasos en la Terminal:

```sh
cd graficas2
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py

```

#web-server
Para correr el programa el web-server debes de seguir los siguientes pasos en la Terminal:

```sh
#Creacion del contenedor
docker-compose build

#Levantamos/activamos el contenedor llamado "web-server"
docker-compose up -d

#Revision de que el contenedor este activo
docker-compose ps

#Validacion del web-server en la maquina local
http://localhost/contact
http://localhost/
```
Nota: Los pasos para el web-server debes de tener Docker en tu S.O