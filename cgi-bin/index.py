#!/usr/bin/env python
# python -m http.server 8080 --cgi

import cgitb, cgi
from functions import encrypt

cgitb.enable()

print("""
<html lang="pt-br">
<head>
    <meta charset="utf-8">
    <title>Translator | Morse Code</title>
    <link rel="stylesheet" type="text/css" href="../estilo.css">
</head>
<body> 
    <div class="app">
        <div class="screen">
            <div class="form">
                <h2>Tradutor de Morse Code</h2>
                <form action="" method="post">
                    <div class="form-input">
                        <label>Digite seu texto</label>
                        <input type="text" name="message" id="message">
                    </div>
                    <div class="form-input">
                        <button id="translate" type="submit">Traduzir</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
""")

form = cgi.FieldStorage()
message = form.getvalue("message")

if message:
    message = str(message)
    result = encrypt(message.upper())

    print(f"""
           <br>
           <div class="result">
                  <h4>Texto digitado: {message}</h4>
                  <h4>Translation: {result}</h4>
           </div>
       """)

print("""</body></html>""")