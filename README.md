<h1>Mateando</h1>
<h2>TP Final - Programación II</h2>

<p>Miembros del grupo:</p>
<ul>
<li>Baptista Carvalho, Gabriela</li>
<li>Calvo, Celeste</li>
<li>Leis, Ayrton</li>
<li>Moyano, Ma. Laura</li>
<li>Raña, Evelyn</li>
<li>Rey, Justina</li>
</ul>

<p>Clique <a href="https://ggabi40.github.io/UTN-FRRO-Programacion-II-Mateando/">aquí</a> para visitar el proyecto.</p>

<br>
<hr>
<br>
<h2>💻 Tecnologías:</h2>
<ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JS</li>
    <li>Python</li>
    <li>Flask</li>
    <li>Jinja</li>
</ul>

<p>Ejecutar:</p>
<code>pip install -r requirements.txt</code>



<br>
<br>
<br>
<br>

<hr>

<h2>Apartado para info:</h2>

<p>
 app/: Aquí es donde estará la lógica principal de la aplicación:

* static/: Aquí van los archivos estáticos como CSS, JavaScript y las imágenes que usará tu aplicación.

* templates/: En esta carpeta estarán las plantillas HTML que utilizan Jinja2. Generalmente incluyen un archivo base.html que sirve como base para otras páginas.

* models.py: Aquí defines los modelos de base de datos usando SQLAlchemy, que te permite interactuar con MySQL.

* routes.py: Define las rutas y vistas de tu aplicación (los endpoints que servirán contenido).

* forms.py: Si estás utilizando formularios con Flask-WTF, puedes definirlos aquí (opcional).

* config.py: Configuraciones como la conexión a la base de datos, las claves secretas, etc., van en este archivo.
</p>

<br>

<p>
Extras (Opcional):
</p>
<ul>
<li>requirements.txt: Este archivo contiene todas las dependencias necesarias para ejecutar el proyecto.</li>
</ul>

<h3>Archivo requirements</h3>
<ul>
<li>Flask (El framework web que utilizarás para construir tu aplicación)</li>
<li>Flask-MySQLdb (Permite la conexión entre Flask y MySQL utilizando el adaptador de MySQLdb)</li>
<li>Flask-SQLAlchemy (Es un ORM que te facilita la interacción con la base de datos utilizando Python en lugar de SQL crudo.)</li>
</ul>
<p>Flask y Flask-SQLAlchemy <b>ya poseen Jinja</b> en su paquete.</p>