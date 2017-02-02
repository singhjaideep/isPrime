import time
from flask import Flask, jsonify, abort
app = Flask(__name__)

def calcprime(n):
    returndict = {
        'id': n,
        'title': u'API that returns whether the number is prime or not (NOT optimised)',
        'isprime': True,    #Default
        'description': u'Prime Number', #Default
        'time': u'',
    }
    #Using Sieve Of Eratosthenes
    from math import sqrt
    num = n+1
    sqrtn = int(sqrt(num))
    noprimes = {j for i in xrange(2,sqrtn) for j in xrange(i**2,num,i)}
    primes = {i for i in xrange(num) if i not in noprimes}
    if n in primes:
        returndict['description'] = u'NOT a prime number'
        returndict['isprime'] = False
        return returndict
    return returndict

@app.route('/api/isprime/<int:input>', methods=['GET'])
def is_prime(input):
    start_time = time.time()
    output = calcprime(input)
    if len(output) == 0:
        abort(404)
    output['time'] = str(round(time.time() - start_time, 2)) + ' sec'
    return jsonify({'output': output})

@app.route('/')
def hello_world():
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')