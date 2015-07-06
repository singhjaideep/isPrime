import time
from flask import Flask, jsonify, abort
app = Flask(__name__)

def isprime(input):
    returndict = {
        'id': input,
        'title': u'API that returns whether the number is prime or not (NOT optimised)',
        'isprime': True,    #Default
        'description': u'Prime Number', #Default
        'time': u'',
    }
    if input % 2 == 0 :
        returndict['description'] = u'Divisible by 2'
        returndict['isprime'] = False
        return returndict
    else:
        for i in xrange(3, input/2, 2):
            if input % i == 0:
                returndict['description'] = u'Divisible by %d' % i
                returndict['isprime'] = False
                return returndict
    return returndict

@app.route('/api/isprime/<int:input>', methods=['GET'])
def is_prime(input):
    start_time = time.time()
    output = isprime(input)
    if len(output) == 0:
        abort(404)
    output['time'] = str(round(time.time() - start_time, 2)) + ' sec'
    return jsonify({'output': output})

if __name__ == '__main__':
    isprime(257)
    app.run(debug=True)