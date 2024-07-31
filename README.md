# README.md
In this repository you may find multiple Python codes (in .py format) related to a wide variety of topics. The do not have a specific purpose, but still they have interesting outputs and different applications. Some of them might be further optimized, however, they all work and the outcomes were the main motivation to develop the codes rather than any practical application.

[Barnsley_Fern.py](https://github.com/HuidobroMG/Python-Codes/blob/main/Barnsley_Fern.py) constructs and represents a specific fractal structure which has the shape of a fern, known as the Barnsley fern. The code applies an iterated function system (IFS) using the appropriate affine transformations, available in [Wikipedia](https://en.wikipedia.org/wiki/Barnsley_fern).

Casino.py simulates the Roulette game in a casino and represents the results of long term profits and losses for different possible bets: Red/Black, 1 dozen or 2 dozens.

Competition_Chances.py simulates the possible strategies to consider in one part of the exam for the Spanish high school teacher position. In short, it computes the probabilities that, from a finite set of randomly extracted balls, at least one of them carries one of the topics that you have studied.

Dice_Coin.py simulates two different random experiments and checks some effects. First, we roll a die multiple times to find that all the possible outcomes tend to appear equiprobably, and shows that the number of times that each value appears tends to the same value with the increasing amount of experiments. Next, we consider the flip coin experiment, and find the Gaussian distribution of the number of heads, which is a manifestation of the [Central Limit Theorem](https://en.wikipedia.org/wiki/Central_limit_theorem).

Flock.py simulates the emergent flocking effect in nature, as it occurs for birds o fishes. It is based on the three basic relations that yield this phenomenon, given by [Craig Reynolds](https://www.red3d.com/cwr/boids/).

Game_of_Life.py generates the famous [Conway's game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). The game starts with a random configuration and the time flows following the 4 standard rules, the life of the cells is shown animated in time.

Guitar_String.py solves an extended version of the wave equation with two additional dispersive term. The effect of these terms is the generation of a more realistic guitar string sound. The solution to the equation is taken, shown as an animation (which may also be saved as a GIF) and converted into sound, so a .wav file is created. This code is mainly based on the solution given and explained in the following [YT video](https://www.youtube.com/watch?v=MavAU3adGk4).

Mandelbrot.py [Mandelbrot set](https://en.wikipedia.org/wiki/Mandelbrot_set).

Maze.py creates a square figure which aims to simulate a maze. The algorithm implements a random walk combined with some simple [rules](https://en.wikipedia.org/wiki/Maze_generation_algorithm) standard in the maze construction. The output becomes even more exotic for very large sizes, however the computation time might take too much time in that case. Besides, the solution may not even have a solution, but the code is quite easy to play with and you may complete it as you wish.

Mortgage.py

Pendulum_Spring.py 

Sieve_of_Eratosthenes.py builds the algorithm to obtain all the prime numbers smaller than any integer number. The [sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) is based on 5 simple steps, but we actually implement a modification of the algorithm for an optimized version. This algorithm has many applications, one of them is the Goldbach conjecture and, within this repository, is used in the Spiral.py code.

Sound_Decomposition.py is a very simple code to read and analyze a .wav file. It is just a kind of example of how to work with the FFT function and shows the wave and the spectrum of frequencies of the sound. As it was uploaded it reads a .wav file which is a LA (only the fundamental 440 Hz) note extracted from youtube (YT).

Prime_Spiral.py

Three_Body_Problem.py
