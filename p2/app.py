from flask import Flask, Response, url_for, send_file
import os, random, string, svgwrite, time
from mandelbrot import *

app = Flask(__name__)

def notFound():
    return "<html><head><title>:(</title></head><body>:(<br><br>HTTP 404, not found.</body></html>"

def removeOldMandelbrot():
    current_time = time.time()
    cutoff = current_time - 86400
    for file in os.listdir("static/mandelbrot"):
        if os.path.isfile("static/mandelbrot/" + file):
            creation = os.stat("static/mandelbrot/" + file).st_ctime
            if creation < cutoff:
                os.remove("static/mandelbrot/" + file)

@app.route('/')
def inicio():
    return '''<html>
                <head>
                    <title>Práctica 2</title>
                    <link rel="stylesheet" type="text/css" href="static/style.css">
                </head>
                <body>
                    <h1>Práctica 2</h1>
                    <li><a href="/">/</a></li>
                    <li><a href="/user/username">/user/username</a></li>
                    <li><a href="/teststatic">/teststatic</a></li>
                    <li><a href="/google">/google</a></li>
                    <li><a href="/css">/css</a></li>
                    <li><a href="/mandelbrot/-1/-1/1/1/300/100">/mandelbrot/x1/y1/x2/y2/ancho/iteraciones</a></li>
                    <li><a href="/svg">/svg</a></li>
                </body>
              </html>'''

@app.route('/user/<username>')
def showUsername(username):
    return 'User: ' + username

@app.route('/teststatic')
def testStatic():
    return '''<html>
                <head>
                    <title>Flask Test</title>
                    <link rel="stylesheet" type="text/css" href="static/style.css">
                </head>
                <body>
                    <div align="center">
                        <br>
                        <h1>Testtesttest</h1>
                        <br>
                        <button type="button">Botón</button> 
                        <br>
                        <img src="static/google.png">
                    </div>
                </body>
              </html>'''


@app.route('/google')
def google():
    return app.send_static_file('google.png')

@app.route('/css')
def css():
    return app.send_static_file('style.css')

@app.route('/mandelbrot/<x1>/<y1>/<x2>/<y2>/<ancho>/<iteraciones>')
def generarMandelbrot(x1, y1, x2, y2, ancho, iteraciones):
    removeOldMandelbrot()
    nombre = str(x1) + str(y1) + str(x2) + str(y2) + str(ancho) + str(iteraciones) + ".png"
    if not os.path.isfile("static/mandelbrot/" + nombre):
        renderizaMandelbrot(float(x1), float(y1), float(x2), float(y2), int(ancho), int(iteraciones), "static/mandelbrot/" + nombre)
    
    return app.send_static_file("mandelbrot/" + nombre)
    
@app.route('/mandelbrot/<x1>/<y1>/<x2>/<y2>/<ancho>/<iteraciones>/<r>/<g>/<b>/<ncolores>/<color>')
def generarMandelbrotBonito(x1, y1, x2, y2, ancho, iteraciones, r, g, b, ncolores, color):
    removeOldMandelbrot()
    nombre = str(x1) + str(y1) + str(x2) + str(y2) + str(ancho) + str(iteraciones) + str(r) + str(g) + str(b) + str(ncolores) + str(color) + ".png"
    if not os.path.isfile("static/mandelbrot/" + nombre):
        paleta = getColorPaleta((int(r),int(g),int(b)), int(ncolores), int(color))
        renderizaMandelbrotBonito(float(x1), float(y1), float(x2), float(y2), int(ancho), int(iteraciones), "static/mandelbrot/" + nombre, paleta, int(ncolores))
    
    return app.send_static_file("mandelbrot/" + nombre)

@app.route('/svg')
def generarSVG():
    dwg = svgwrite.Drawing("static/test_svg.svg", profile='tiny')
    for x in range(random.randint(10, 50)):
        numero = random.randint(1, 3)
        if numero == 1:
            dwg.add(dwg.line((random.randint(0, 600), random.randint(0, 600)), (random.randint(0, 600), random.randint(0, 600)), stroke=svgwrite.rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), '%')))
        elif numero == 2:
            dwg.add(dwg.circle(center=(random.randint(0, 600),random.randint(0, 600)), r=random.randint(0, 100), fill=svgwrite.rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), '%')))
        else:
            dwg.add(dwg.rect(insert=(random.randint(0, 600),random.randint(0, 600)), size=(random.randint(0, 100),random.randint(0, 100)), rx=None, ry=None, fill=svgwrite.rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), '%')))
    
    dwg.save()
    return app.send_static_file("test_svg.svg")


@app.errorhandler(404)
def nf(a):
    return notFound()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
