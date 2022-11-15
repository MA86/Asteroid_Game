# Asteroids Game

This is a prototype of Atari's Asteroids game. The purpose of this project is to learn low-level graphics libraries such as SDL2, as well as to learn various game architecture techniques and game object models. 

This project is part of a book that I'm currently reading (see below for name of the book).

## Technologies Used

Python, and SDL2 (Simple Directmedia Layer) which is a low-level 2D/3D programming library similar to OpenGL. Additionally, for the organization of classes, a technique that mixes *hierarchy game object model* and *composition game object model* is applied. 

For character movements, Newtonian physics is implemented using a technique called Velocity Verlet Integration.

New classes added for this project:

Components
- MoveComponent (for Newtonian physics)
- InputComponent (for keyboard movement)
- CircleComponent (for collision detection)

Game-specific Actors
- Ship
- Asteroid
- Laser

## Demonstration

![space_shooter](asteroid_game.gif)

Note: All source code for this game prototype can be found inside `.py` files.

*The book I'm currently reading for this project is called, **Game Programming in C++**.*
