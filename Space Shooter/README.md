# SPACE SHOOTER
#### Video Demo:  <URL HERE>
#### Description: 
      For my final project on CS50X, I choose to build a game with the pygame library. The game is a generic space shooter that I will continue to implement and improve after the couse. When you open the game, you see a title menu, that asks the player to click with the mouse to start the game. You can play with the key arrows for movement and the space
      bar to shoot, The game runs forever, until user loses 5 lives or his health bar goes to 0.

#### /Assets:
      Contains all necessary files for the game in separeted folders. The background contains the background image. The bullets have the png files of the player and enemy bullets.
      Fonts contains a pixelated font for the text renders in game. Ships contains the ship images and the sounds have the background music and sound effects. All the assets used in this project are of public domain and don't have copyrights.

#### Constants.py: 
      In this file, you have all the constants of the game. width and height of the screen, that is used in the classes and functions to determine the size of things, you can alter
      the width and height without compromising the code. You also have all loaded images, background, and sound effects of the game, the sound effects are strangely lound, so there's a function in the file called set_volume() that puts the volumes on 10% to not jumpscare the user.

#### Ships.py:
      In this file, you have all the classes of the project and the collide function. The collide function can detect when the mask of obj1 overlaps with the mask of the obj2.
      The Ship class, have all the characteristics of the player and enemy ships, the position, draw, the height and width of the obj and also a cooldown to shoot the bullets.
      The enemy and player classes inherit those characteristics but also have unique ones like the health bar of the player and the enemy have a dict with the 3 possible enemies
      to spawn. The bullet class, prevents the bullet of existing off_screen, because the enemies spawn in a negative X position, to arrive in the screen in different timings, besides that, is all very well explained in the comments.

#### Project.py:
     This is the main file of the game. Where you import all necessary classes, constants libraries and functions for the game to work. The Project have a main function that instance and use all the classes and a main_menu() function that provides the player a menu before the game starts, and calls the main() function when the user click with the mouse.
     When the main() function is called the game render the texts and draw the background and ships. The game runs in a loop and this loop can end when the user closes the app,
     user loses the 5 lives or his health bar goes to 0. You start with 5 enemies being added to a list, and the pygame draw those 5 enemies in random position off screen in the negative X axis. After the 5 enemies dies, you have a loop that increment +2 enemies for the next wave and add alls those enemies in the list again.
     In the player movement you have dynamic conditionals, that user the constant of the height and width to prevent the player of going off_screen or the ship to also partially going off the screen.

#### Future of the project:
     In this state, the game has "no end" and you don't have a clear objective besides to destroy each ship that appears on the screen. I pretend to implement in the future loot from the enemies, for the player to refil his life bar or recover lost lives. Also I want to implement the ability to the player to upgrade his weapon and also get a "superpower" loot. Each 5 levels that user pass, he will face a boss. I'm starting after this course, the CS50 AI and hope to use some knowledge from the course to implement AI for the enemy.

      