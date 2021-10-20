import yagmail as yagmail
from flask import Flask, render_template, flash, request
import os
import utils

# correo = 'ecvasquez@uninorte.edu.co'
# correo = 'favillegas@uninorte.edu.co'
correo = 'favillegas@uninorte.edu.co'

yag = yagmail.SMTP('brf.noreply@gmail.com', 'Uninorte43!')	

link = '\n\nhttps://accounts.google.com/signin/v2/usernamerecovery?hl=en&continue=https%3A%2F%2Fmail.google.com&service=mail&ec=GAlAFw&flowName=GlifWebSignIn&flowEntry=AddSession'

yag.send(to=correo, subject="Password recovery", contents= 'Use this link to change your password.' + link)


flash('Revisa tu correo para activar tu cuenta')
# return render_template('login.html')


