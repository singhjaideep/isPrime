# isPrime
Sample flask api to return whether a number is prime or not. Can be optimised infinitely.

## How to run:
1. Download/Setup docker environment in your machine.
2. Git clone this repo
   ```
   git clone https://github.com/singhjaideep/isPrime.git isPrime
   ```
3. cd into isPrime/ and build/run docker-compose
   ```
   docker-compose up --build
   ```
4. API is viewable at http://DOCKERMACHINEIP:500

## How to use:
- GET
  - Example to find out if 9 is prime or not, GET call would be http://DOCKERMACHINEIP:5000/api/isprime/9

## Future enhancements:
- Add numpy
- Make frontend app
