# Puzzlebot Signal Detection

Repositorio para la detección de señales de tránsito utilizando un modelo YOLO (11n) integrado en un entorno ROS2 para un Puzzlebot y una Rubik Pi 3.

## Descripción

Este proyecto implementa un sistema de visión por computadora capaz de detectar señales de tránsito utilizando modelos YOLO entrenados específicamente para el reto. El sistema se encuentra integrado dentro de un workspace de ROS2 y está diseñado para ejecutarse en un Puzzlebot.

El repositorio incluye:

* Workspace de ROS2.
* Paquete de detección de señales.
* Modelos YOLO entrenados.
* Archivos de configuración.
* Scripts necesarios para ejecutar el sistema.

## Estructura del repositorio

```text
Puzzlebot-SignalDetection/
├── ros2_ws_minichallenge7/
│   ├── src/
│   ├── build/
│   ├── install/
│   └── log/
├── my_model/
├── README.md
└── .gitignore
```

> Nota: las carpetas `build`, `install` y `log` pueden no aparecer en el repositorio ya que se generan automáticamente durante la compilación del workspace.

## Requisitos

* Ubuntu 22.04
* ROS2 Humble
* Python 3.10+
* OpenCV
* Ultralytics YOLO
* Colcon

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/leyvagael/Puzzlebot-SignalDetection.git
```

Entrar al workspace:

```bash
cd Puzzlebot-SignalDetection/ros2_ws_minichallenge7
```

Instalar dependencias:

```bash
pip install ultralytics opencv-python
```

Compilar el workspace:

```bash
colcon build --symlink-install
```

Sourcear el workspace:

```bash
source install/setup.bash
```

## Ejecución

Verificar que el paquete exista:

```bash
ros2 pkg list | grep SignalDetector
```

Ejecutar el nodo:

```bash
ros2 run SignalDetector detector_node
```

> El nombre del ejecutable puede variar dependiendo de la configuración del paquete.

## Modelos

El repositorio incluye distintos modelos YOLO entrenados para la detección de señales.

Los modelos se encuentran dentro de las carpetas:

```text
Debloated_model/
EdgeImpulse_model/
```

## Dataset

El dataset utilizado para el entrenamiento no se incluye completamente dentro del repositorio debido al tamaño de los archivos.

## Tecnologías utilizadas

* ROS2 Humble
* Python
* YOLO
* OpenCV
* Ultralytics

## Autores

* Gael Leyva
* Uriel Crespo
* Arturo Pérez
* Martín Martínez
