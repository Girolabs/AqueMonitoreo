# AqueMonitoreo

Monitoreo de la gestion municipal para Asuncion/Paraguay.

Este proyecto fue una iniciativa de [Aquienes Elegimos Paraguay](http://aquieneselegimos.org.py)  y el [CIRD](http://cird.org.py).

Fue desarrollado por [Girolabs](http://girolabs.com).


Esta obra está licenciada bajo la Licencia Creative Commons Atribución 4.0 Internacional. Para ver una copia de esta licencia, visita http://creativecommons.org/licenses/by/4.0/.

El sitio web esta diponible en [monitoreo.aquieneselegimos.org.py](http://monitoreo.aquieneselegimos.org.py).

Para levantar el curso de manera local seguir los siguientes pasos.

```bash
git clone git@github.com:yank07/AqueMonitoreo.git
cd Aquemonitoreo
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```
