# AqueMonitoreo

Monitoreo de la gestion municipal para Asuncion/Paraguay.

Este proyecto fue una iniciativa de [Aquienes Elegimos Paraguay](http://aquieneselegimos.org.py)  y el [CIRD](http://cird.org.py).

Fue desarrollado por [Girolabs](http://girolabs.com).


Esta obra está licenciada bajo la Licencia Creative Commons Atribución 4.0 Internacional. Para ver una copia de esta licencia, visita http://creativecommons.org/licenses/by/4.0/.

El sitio web esta diponible en [monitoreo.aquieneselegimos.org.py](http://monitoreo.aquieneselegimos.org.py).

Para levantar el curso de manera local seguir los siguientes pasos.
En el caso de utilziar CentOS instalar los siguientes paquentes.(Atencion, para CentOS se podria necesitar otro paquete adicional para la libreria PILLOW)
```bash
sudo yum install python-devel
sudo yum install zlib-devel
sudo yum install libjpeg-turbo-devel
```
En el caso de utilizar Ubuntu instalar los siguientes paquentes

```bash
sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk 
sudo apt-get install python-dev
```

Proseguir con la instalacion de la plataforma.


```bash

pip install virtualenv
git clone git@github.com:yank07/AqueMonitoreo.git
cd Aquemonitoreo
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```

Luego crear el usuario de Superadministrador para el panel de Administrador. Igrersar nombre de usuario y contraseña


```bash
python manage.py createsuperuser

```bash

Ingresar al panale de administracion [http://localhost:8000/admin/](http://localhost:8000/admin/).