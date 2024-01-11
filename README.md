# 4-equals-10-solver
Solver for the game '4=10' 

Given 4 numbers, the objective is to use basic operations (add, subtract, multiply, divide) to reach 10. All numbers must be used. One set of parenthases is allowed

The game: https://play.google.com/store/apps/details?id=app.fourequalsten.fourequalsten_app&amp;hl=en_CA&amp;gl=US

The solver is quite 'dumb'. It just creates every possible expression from the 4 numbers, allowed operations, and the different placements for parenthases. Once it has all of the expressions as strings, it evaluates each one and saves its value. Then it prints out the expressions that equal 10, as well as the number of solutions. 
