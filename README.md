# Codes description
In this repository you may find some codes which are not directly related to physics or to the other repositories. Some of them are not optimized and they might be slow but they all work and the outputs were the main motivation to develop the codes rather than any useful purpose.

Barnsley_Fern.py constructs and represents a specific fractal structure which has the shape of a fern, known as the Barnsley fern. The code applies an iterated function system (IFS) using the appropriate affine transformations, available in [Wikipedia](https://en.wikipedia.org/wiki/Barnsley_fern).

Casino.py simulates the Roulette game in a casino and represents the results of long term profits and losses for different possible bets.

Competition_Chances.py

Dice.py 

Flock.py simulates the emergent flocking effect in nature, as it occurs for birds o fishes. It is based on the three basic relations that yield this phenomenon, given by [Craig Reynolds](https://www.red3d.com/cwr/boids/).

Game_of_Life.py generates the famous [Conway's game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). The game starts with a random configuration and the time flows following the 4 standard rules, the life of the cells is shown animated in time.

Mandelbrot.py

Maze.py creates a square maze building a random walk. It shows a nice output of the maze which becomes even more exotic for very large sizes, however the computation time might take too much time in that case. Besides, the solution may not even have a solution, but the code is quite easy to play with and you may complete it as you wish.

Sieve_of_Eratosthenes.py builds the algorithm to obtain all the prime numbers smaller than any integer number. The [sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) is based on 5 simple steps, but we actually implement a modification of the algorithm for an optimized version. This 

Sounds.py is a very simple code to read and analyze a .wav file. It is just a kind of example of how to work with the FFT function and shows the wave and the spectrum of frequencies of the sound. As it was uploaded it reads a .wav file which is a LA (only the fundamental 440 Hz) note extracted from youtube (YT).

String.py solves an extended version of the wave equation with two additional dispersive term. The effect of these terms is the generation of a more realistic guitar string sound. The solution to the equation is taken, shown as an animation (which may also be saved as a GIF) and converted into sound, so a .wav file is created. This code is mainly based on the solution given and explained in the following [YT video](https://www.youtube.com/watch?v=MavAU3adGk4).

Three_Body_Problem.py
