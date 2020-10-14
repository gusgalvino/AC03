import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def primos():
    primos = []
    limite = 100
    n = 1
    c = 1
    while c <= limite:
        divisores = 0
        for i in range(1, n+1):
            if n % i == 0:
                divisores += 1
        if divisores == 2:
            primos.append(n)
        n += 1
        c = len(primos)
    return str(primos).strip('[]')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
