# Adóptame
![Taller de Aplicaciones Distribuidas](https://img.shields.io/badge/Taller%20de%20Aplicaciones%20Distribuidas-38BCAC)
![Proyecto Final](https://img.shields.io/badge/Proyecto%20Final-50BC38)

![Visualización1](images/image1.jpeg)
![Visualización2](images/image2.jpeg)
![Visualización3](images/image3.jpeg)
![Visualización4](images/image4.jpeg)
![Visualización5](images/image5.jpeg)
![Visualización6](images/image6.png)
![Visualización7](images/image7.png)
![Visualización8](images/image8.png)
![Visualización9](images/image9.png)

## 1. Descripción del proyecto
Adóptame es un proyecto implementado como plataforma con microservicios que tiene como finalidad integrar los datos de los albergues de mascotas de Lima en un solo espacio, con la finalidad de facilitar la adopción desde un único punto de acceso.

## 2. Estado del proyecto
![Badge Finalizado](https://img.shields.io/badge/STATUS-FINALIZADO-green)

## 3. Tecnologías utilizadas
![Windows 11](https://img.shields.io/badge/Windows%2011-%230079d5.svg?style=for-the-badge&logo=Windows%2011&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-217346.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

### Microservicio principal
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

### Microservicio hijo 1
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

### Microservicio hijo 2
![Java 22](https://img.shields.io/badge/java%2022-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white)
![SpringBoot](https://img.shields.io/badge/springboot-%236DB33F.svg?style=for-the-badge&logo=spring&logoColor=white)
![Oracle](https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white)

### Microservicio hijo 3
![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
![Express.js](https://img.shields.io/badge/express.js-%23404d59.svg?style=for-the-badge&logo=express&logoColor=%2361DAFB)
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)

### Frontend
![Angular](https://img.shields.io/badge/angular-%23DD0031.svg?style=for-the-badge&logo=angular&logoColor=white)
![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)

## 4. Guía de instalación
1. Clonar el repositorio en su IDE:
    ```
    https://github.com/caroSeminario23/TAD_Adoptame.git
    ```

2. Crear las bases de datos para cada microservicio y ejecutar los scripts para la estructura y población de datos.

3. Configurar los siguientes archivos (de acuerdo con las plantillas del repositorio):
    - .env (para los servicios de Flask y Express)
    - application.properties (para el servicio en SpringBoot)

4. Guardar los cambios.

5. Crear entornos virtuales los servicios de Python y acceder a ellos.

6. Desplegar los servidores del backend en local:
    - Principal: ```python app.py```
    - Hijo 1: ```python app.py```
    - Hijo 2: ```mvn spring-boot:run```
    - Hijo 3: ```node app.js```

7. Desplegar la página web del frontend en local: ```ng serve```

## 5. Licencia
[![Licencia](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)

## 6. Autores
- Carolina Seminario (caroSeminario23) → Backend y frontend
- Fiorella Perez → Frontend
- Jhosselin Clemente → Frontend
- Jamil Tuncar (JamilTuncarQ) → Backend
- Leo Soto → Frontend
- Jesús Vasquez → Frontend
- Wilson Leyva → Frontend