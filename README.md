
<img src="static/images/LogoGrupo43_Uninorte.png"><h1>Grupo43</h1>
### Contenido python + Flask

## DESARROLLO DE LA PRACTICA

siga los siguientes pasos


# 1. Crea un archivo base.html
	a. Inserta un condicional de si la sesión existe, muestre la opción de logout.
	   DESARROLLO WP06 archivo=base.html , Linea=7
        {% if g.user %}
        {% else %}
        {% endif %}
	   Hay que hacer el cerrar sesion 
	   DESARROLLO WP07 archivo=app.py , linea=217
	   @app.route( '/logout' )
		def logout():

		
	b. Si no hay sesión, dar opción de login y register.
	   DESARROLLO WP08 archivo=base.html , Linea=19
            <li>
              <a href="{{ url_for('register') }}">Registrarse</a>
            </li>
            <li>
              <a href="{{ url_for('login') }}">Iniciar Sesión</a> 
            </li>

	c. Sin importar si hay o no sesión, se debe mostrar un enlace para la página Contáctenos.
	   DESARROLLO WP09 archivo=base.html , Linea=27
	    <li>
          <a href="{{ url_for('contacto') }}">Contactenos</a>
        </li>
	   
# 2. Modifica los archivos html creados hasta el momento para incluir una extensión de base.html
	DESARROLLO WP10 archivo=*.html , Linea=1 de cada uno
	{% extends 'base.html' %}
	
# 3. Crea un archivo send.html con un formulario para enviar mensajes que incluya los
	campos: para, asunto y mensaje. La acción ‘submit’ del formulario será la URL para send.
	DESARROLLO WP11 archivo=send.html , Linea=1
	
# 4. Dentro del archivo app.py
	a. Dentro de la petición de register, modifica el password antes de insertarlo en la base
	de datos. Usa la función generate_password_hash antes de realizar el insert. (realiza
	pip install werkzeug e importa: from werkzeug.security import
	generate_password_hash, check_password_hash)
	DESARROLLO WP01 archivo=app.py , 
	@app.route( '/register', methods=('GET', 'POST') )
	def register(): linea-59 y linea:9
	generate_password_hash(password))
	from werkzeug.security import generate_password_hash, check_password_hash

	b. Crea la función login_required que valide si existe un usuario y sino, reenvíe al
	usuario a la vista /login.
	DESARROLLO WP05 archivo=app.py , 
	def login_required(view): linea-135
    @functools.wraps( view )
	El proposito de este programa es enviar mensajes
	se debe crear una ruta llamada enviar mensajes que se va a llamar send
	linea-158
	@app.route( '/send', methods=('GET', 'POST') )
	@login_required
	def send():
	Pero solo pueden enviar mensajes las personas que ya iniciaron sesion
 	no se puede entrar a send(para enviar mensaje porque enviar mensaje solo es para las personas con id)
	entonces login_required se encarga de validar el usuario
	hay que importar la funcion 
	import functools
	esta no es de flask es generica
	
	c. Modifica la función login para validar el password ingresado contra el almacenado.
	Para ello, puedes validar con la función check_password_hash.
	DESARROLLO WP02 archivo=app.py , 
	@app.route( '/login', methods=('GET', 'POST') )
	def login(): linea-74
	#Validar contraseña hash linea-107
	result = check_password_hash(store_password, password)
	
	d. Modifica la función login. Si el usuario y la contraseña fueron ingresados
	exitosamente, vamos a eliminar la sesión anterior y asignar la nueva sesión al nuevo
	usuario.
	DESARROLLO WP03 archivo=app.py , 
	@app.route( '/login', methods=('GET', 'POST') )
	def login(): linea-111
	#manejo de sesiones - hay que importar session que es de flask
	#se maneja como si fuera un diccionario
	#la sesion se conserva, se guarda en el servidor
	# a diferencia de g esta no se guarda la g se destruye
	from flask import session
	session.clear()
    session['user_id'] = user[0]

		
	e. Crea una función para la ruta /logout que cierre la sesión y redireccione a
		login.html.
	DESARROLLO WP07 archivo=app.py , linea=217
	   @app.route( '/logout' )
		def logout():

	
	f. Crea una función para la ruta /send que valide o haga llamado a login_required,
	valide los campos del formulario de la página send.html e inserte el mensaje
	enviado en la base de datos.
	DESARROLLO WP13 archivo=app.py , linea=158
	@app.route( '/send', methods=('GET', 'POST') )
	@login_required
	def send():
		if request.method == 'POST':
			from_id = g.user['id']
			to_username = request.form['para']

	
	g. Crea una función app.before_request que se ejecuta previo a cada request y
	valide el usuario de la sesión.
	DESARROLLO WP04	 archivo=app.py , 
	@app.before_request
	def load_logged_in_user():	linea-204
	from flask import g

	
	h. Modifica la función de entrada para reenviar a la vista send si existe un usuario o a la vista
	login si no existe.
	DESARROLLO WP12	 archivo=app.py , linea=17
	@app.route( '/' )
	def index():
		if g.user:
			return redirect( url_for( 'send' ) )
		return render_template( 'login.html' )
	
	
	i. Modifica la función register, para que si existe el usuario envíe a send sino a register.
	DESARROLLO WP14 archivo=app.py , linea=24
	@app.route( '/register', methods=('GET', 'POST') )
	def register():
		if g.user:
			return redirect( url_for( 'send' ) )
		try:
			if request.method == 'POST':
				name= request.form['nombre']
				username = request.form['username']

	
	j. Crear una función downloadpdf que retorne un archivo que se encuentre en
	resources/doc.pdf ejemplo: return send_file("resources/doc.pdf",
	as_attachment=True).
	DESARROLLO WP15 archivo=app.py , linea=146
	@app.route( '/downloadpdf', methods=('GET', 'POST') )
	# @login_required
	def downloadpdf():
		return send_file( "resources/doc.pdf", as_attachment=True )
	
	#hay que importar la libreria
	from flask import send_file
	#as_attachment=True
	significa que lo descargue enseguida

	En base.html linea=9 se agrega el enlace
    <a class="action" href="{{ url_for('downloadpdf') }}">Descargar doc pdf</a>
	
	k. Crea una función downloadimage que retorne un archivo que se encuentre en
	resources/image.png.
	DESARROLLO WP16 archivo=app.py , linea=152
	@app.route( '/downloadimage', methods=('GET', 'POST') )
	@login_required
	def downloadimage():
		return send_file( "resources/image.png", as_attachment=True )

	En base.html linea=12 se agrega el enlace
    <a class="action" href="{{ url_for('downloadimage') }}">Descargar imagen</a>

	
  	l. Modifica la función login para que cuando se confirme la sesión, se cree una cookie
	del tipo ‘username’ y almacene el usuario.
	DESARROLLO WP17 archivo=app.py , linea=114
                        session.clear()
                        session['user_id'] = user[0]
                        resp = make_response( redirect( url_for( 'send' ) ) )
                        resp.set_cookie( 'username', username )
                        return resp
	#make_response es para agregar encabezados HTTP adicionales a una respuesta dentro del código de una vista.
	#se usa para crear sesiones, crea un objeto con el tipo de respuesta
	#con este objeto se pueden hacer otros procesos
	
	#se debe importar make_response
	from flask import make_response
	
	#set_cookie
	es para crear la cookie , con el nombre de la cookie y el valor de la cookie
	
	m. Modifica la función send para que recupere la cookie creada y en los mensajes de
	error incluya el valor de username.
	DESARROLLO WP18 archivo=app.py , linea=167-188
	nom_cookie=request.cookies.get('username','usuario')
	#Asi se consigue el valor de una cookie
	request.cookies.get(nombre de la cookie,mensaje en caso de no existir la cookie)
	
	
# 5. Modifica el archivo base.html y adiciona dos link para downloadpdf y downloadimage 
	si existe el usuario.
	DESARROLLO WP19 archivo=base.html , linea=9,12
	
Nota: En caso dado encuentres errores al momento de realizar flask run, ejecuta python3
app.py

