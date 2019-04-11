# Breakout
For the second half of the semester, we will be recreating the classic Atari game, Breakout.

![Breakout](/docs/img/breakout.jpg)

## Purpose
Labs 10-14 will constitute the remainder of the semester and will involve the development of the classic Atari game Breakout.
Lab 9 was an introduction to working in real-time environments.
Now that you have had time to play with and experiments with developed code, it is time to start writing it yourself.

That being said, these labs serve 3 main purposes:
* Giving you exposure to larger codebases (similar to the first incremental project).
* Working with and achieving __milestones__ (you may already be familiar with this if you've taken ENGR 121).
* Working as part of a team to achieve success in coding.
 
> __PAIRED PROGRAMMING:__ We will be implementing paired programming in a similar fashion as the previous half of the semester.
Working as part of a group always presents a new set of challenges due to the differences and opinions of others.
I encourage everyone to treat this project as an opportunity to improve collaborating with others (even if you are already an excellent programmer).
Always keep in mind that companies are looking for individuals who can work well with a team, this is true across every discipline.

>__TAKE AWAY:__ At the end of the semester, you should have something that you would be proud to show off to your friends and family.
You may also be able to add this project as part of your resume when you're looking for internships.

## Schedule
In order to better help you succeed at this project, we have divided it into 5 parts.
Each part will consist of a 1-Week lab, and will have milestones that you will be required to meet.
The last lab of the semester will not be a work lab, but instead a time to present what you've achieved.

> __NOTE:__ This schedule and milestones of _future labs_ are subject to changes depending on the status of most groups.

* __Lab 10 - Inheritance__
  * This lab will focus on implementing game objects as the children of PyGame Sprites.
  * This lab will have you create all objects and multiple, different bricks.
* __Lab 11 - Real-time programming II__
  * This lab will focus on working in the update loop.
  * Unlike lab 9, there will be a larger emphasis on debugging movement code and fixing issues related to real-time systems.
  * In this lab you should also begin to track items such as lives and levels.
* __Lab 12 - Binary File I/O__
  * This lab will focus on using File I/O to store gamedata and allow a game to be saved.
* __Lab 13 - Integration__
  * This lab is designed to give you a week to add your own touches to the game.
  * Ideas will be given, but feel free to add whatever you want to the game.
  * This lab will offer you an opportunity to catch up if you have fallen behind.
* __Lab 14 - Presentations__
  * This week will consist of the end-of-semester "Super" quiz.
  * You will present your projects in 5 minute time slots.

>__NOTE: EVEN THOUGH THE ENTIRETY OF THE PROJECT WILL BE GIVEN IN WEEK 10, WE STRONGLY DISCOURAGE TEAMS FROM GOING AHEAD.
IF YOU AND YOUR PARTNER CHOOSE TO WORK AHEAD, PLEASE WORK TOGETHER, ANY CODE WHICH WAS NOT WORKED ON JOINTLY WILL NOT RECEIVE PARTICIPATION CREDIT.__

### Grading Overview
* 100 points | Week 10 Milestones (graded on Week 11)
* 100 points | Week 11 Milestones (graded on Week 12)
* 100 points | Week 12 Milestones (graded on Week 13)
* 100 points | Week 13 Milestones (graded on Week 14, as part of the presentation)
* 100 points | Week 14 Presentation
* 300 points | Final Project Submission

All weeks will count the same as a normal lab (100 points).
The final presentation will also count as a normal lab grade.
The final project submission will be due during finals week and will give you an opportunity to reclaim points if you've missed some milestones.

## Project Updates
Because this project is subject to change throughout the semester, the instructors may release a manual change from time to time.
Because we are using git to distribute this project, fetching changes is very simple.

```
git remote -v
```
This command will print out your origin and upstream repos.
Origin is the repository that you push to and upstream is an ancestor repository that you can fetch from.
```
git remote add upstream https://gitlab.pcs.cnu.edu/cpsc250-<instructor's last name>-<crn>-s19/cpsc250l-breakout-s19.git
```
This command is used to add the original repo as an ancestor repository you can fetch changes from, only run this command if the `git remmote -v` only returns an origin repo.

```
git fetch --all
```
This command will synchronize the repositories by fetching changes between them.
This effectively pulls the changes from the upstream repo.

```
git merge upstream/<branch name> --no-commit
```
Merges the changes from the ancestor repo.
The branch name will be given to you when you need to update.

```
git add --all
git commit -m "<Message>"
git push origin master
```
Add, commit, and push the changes to your remote repo (origin).

## Academic Integrity
Before beginning the project, I want to take the time to remind everyone that the CNU Honor Code applies to this lab course and this project.
Cheating under any circumstances will not be tolerated, and will result in a grade of a 0 and a report to CHECS.

### Cheating
This project will be more complex than projects given in the past, and will offer opportunities for students to write very diverse code.
With this in mind, code between groups should be very different.
Spotting copied code will be very easy with this project, please do not even attempt to copy code without documenting it.

### Collaboration & Empty Hands
Understanding this, I want groups to be successful.
To that end, I understand that sometimes a helping hand is needed.
You may work with individuals outside of your group, so long as you follow the empty hands policy (see the lab syllabus).
That is, you discuss ideas and concepts with other, but do not take anything away from the meeting (i.e. If you draw ideas on a whiteboard, the whiteboard should be erased, and you should not have taken notes from it).
Additionally, I expect all parties involved to cite their collaboration sessions as part of their code.
If I see similar code, I can excuse it more easily if satisficing documentation is provided. 

### Online Resources
Breakout is a classic game that many other schools may also use as introductory level projects.
Due to this, there will undoubtedly be repositories that contain complete or nearly complete solutions.
Please resist the urge to copy solutions from online.
You will find great satisfaction in getting your project to work by yourself.
If you copy from someone else, you will not get the same satisfaction; in essence, you will be cheating yourself out of the reward for coding.

If for some reason find yourself disobeying the above advice, please cite where your got your code from.
Failure to do so will be considered plagiarism, and will be treated the same as if you copied code from another student in class.
Please do not take a complete solution from online, I cannot give you credit for it even, if it is cited.
If you are stuck in a spot and need a nudge in the right direction, you may copy code snippets from online (e.g. GitHub, StackOverflow).
So long as you cite them, I will only take off a few points per instance.

# Lab 10 - Inheritance
This lab will be based on utilizing inheritance to help facilitate creating game objects.

__Why should we use inheritance?__
If you remember from lecture, child objects inherit attributes and functions from their parents.
In the case of PyGame and game development in general, a lot of work is required to setup a valid game object.
Fortunately, PyGame comes equipped with the `Sprite` class in the `sprite` module (`pygame.sprite.Sprite`).
This sprite object is a template that is already setup to work seamlessly in PyGame.

## Understanding Sprites

All sprites are composed of 2 primary elements, an image (which is what is seen on screen), and a collision field (which is used to determine the bounds of an object).
By separating these 2 elements, you gain increased control over the physics in the game environment.

The important object to take note of in this relationship is the bounding box, which is a nested class called `pygame.Rect`.
When you instantiate a new sprite object, you can refer to its bounding box via the `rect` attribute (e.g. `mysprite.rect`).
This bounding box is the principle method behind moving objects on screen (think about when you moved the paddle to the bottom of the screen in Lab 9).
There are 2 ways of easily moving sprites, the first is to use the `move` function, and the second is to use the sub-points on the rectangle (more on that later).
The move function is essentially a setter for the sprite, it takes in a list containing an x and y coordinate and moves the ball to the location specified.
The location is based on the screen location where the top left corner is the origin and the x-axis increased to the right, and the y-axis increases when going down (Y is inverted from a normal Cartesian coordinate system).

The other method, as described above, is to use the subpoints of the Rect object.
These points refer to 9 points on the rectangle's perimeter: `topleft`, `bottomleft`, `topright`, `bottomright`, `midtop`, `midleft`, `midbottom`, `midright`, and `center`. 
All of these points are set with a tuple containing an x and a y position (e.g. `(x, y)`).
There are also other dimensions which may be used to align the sprite, these include:
* `x` and `y`, which refers to the top left of the sprite.
* `top`, `left`, `bottom`, and `right`, which refers to either the x or y of a given side.
* `centerx` and `centery`, which refer to the x or y of the center of the Sprite.
> __NOTE:__ These dimensions only require single dimensional data, like an int.

As state earlier, you can also influence the size of the object, via its collision box.
This can be done by working with the following variables:
* `size`, which takes in a tuple containing the new width and height
* `width`, and `height`, which contains the elements individually

I recommend looking through the full __[Documentation](https://www.pygame.org/docs/ref/rect.html)__ for a the `pygame.Rect` object, as there is a lot to explore with this object.

## Creating the Objects

For this lab, we need to focus on 3 objects: a ball, a paddle, and a brick.
You can use the code from last week as a starting point, however, going forward we will be using this repository.
You should run the game to test your code and make sure that it is working.

### The Ball
The ball will bounce around on the sides of the screen, and will be deflected when it hits a Brick.
It will also be deflected when it hits the paddle.
Unlike in Tom's Pong, however, the ball will not bounce off of the bottom of the screen, but will fall through the screen.
The ball should start on top of the paddle, aligned on to the `centerx` of the screen.
> __NOTE:__ The ball does not need to start out stationary on the paddle or have user input to start, for this lab, having the ball launch from the start is sufficient.

### The Paddle
The paddle will move across the bottom of the screen to deflect the ball upwards.
The paddle should start in the bottom, middle of the screen.
The paddle should not be able to leave the screen.
That is, `screen.left <= paddle.left` and `paddle.right <= screen.right`.

The paddle should deflect the ball based on where the ball lands on the paddle (See below).
![Ball Deflection](/docs/img/ball_deflection.png)

### The Brick
A brick should sit in its designated location and not move.
A brick should have a health value associated with it.
When a ball impacts the brick, it should be damaged.
When a brick's health reaches 0, it should be destroyed (i.e. removed from the screen).

## Submission
For this lab, you will present your results to your instructor in the Week 11 Scrum.
Your instructor will ask additional questions regarding your implementation and other general knowledge.

## Rubric
* 40 - Participation
* 25 - Ball working correctly
  * 5 - Ball starts out on top of the paddle and is bounced upward.
    > You may also start the ball above the paddle and have it drop down (either implementation is acceptable.)
  * 10 - Ball is deflected when it hits a brick (Movement does not need to be perfect).
  * 10 - Ball is deflected when it hits the paddle.
  The ball should tend toward the left when hitting the left side of the paddle, and to the right when hitting the right.
* 5 - Paddle Working correctly
  * 5 - Paddle does not leave the bounds of the screen.
* 30 - Brick working correctly
  * 15 - Bricks should have health that is decreased when a ball hits it.
  * 15 - Bricks should be destroyed when their health reaches 0.

# Lab 11 - Real-Time Programming II: Game States
Now that we have created classes for each of the Breakout objects, it is time to get the game working.

## Game States
One of the most important aspects to creating a real-time project is to design it with various __[states](https://en.wikipedia.org/wiki/State_(computer_science))__ in mind.
For our game, all a state means is that we have a past, a present, and a future that we need to be aware of.

States all have a definition (what they do), and a transition (how they change over time).
These series of states make up a __state diagram__.
For any large project, your should define your state diagram by hand before implementing it in code (e.g. creating a whiteboard sketch, Microsoft Visio diagram, etc).

For our project, the model will be provided to you, your job is to translate it into code.

Let's create a simple model using Breakout.

#### State Definitions:
In Breakout, we have 3 primary states: a play state, a pause state, and a game over state.
* During the game state, the behavior of the program should allow it to take user input, process game changes, and display the changes back to the user.
* During the game over state, the game should sit idle and wait for a user to restart the game (classically, this would be an arcade machine waiting for a user to insert enough coins to play).
  In our case, this is just the game waiting for the user to press the space bar.
* During the pause state, the game should sit idle and wait for a user to un-pause the game.

#### State Transitions
Now that we have defined our states, we need to define our state transitions.
* We should have our game start in the game over state, since it is how the game will have ended previously.
  The Game over state should be what the game loads into upon initialization.
* The game over state is very simple to model: it transitions to the play state when and only when the user gives the input.
  * If the game is terminated, the state will not change.
* The play state is a little bit more complex, since it involves multiple branching paths.
  * The play state will transition into the pause state when the user pauses the game, and
  * the play state will transition to the game over state when the user runs out of lives or the user terminates the game manually.
* Finally, the pause state is very similar to the game over state since it transitions to the play state when a user un-pauses the game.

![State Diagram](/docs/img/breakout_states.png)
> Because your final game may be different than the given game, your diagram may eventually differ than what is described above.

## Implementing States
The obvious follow up questions is __"How do I write this in code?"__
There are many ways to implement state transitions.
In a larger project, you would likely use objects to contain various behaviors and change the object pointers to transition states.
In this project, it will be easier to use integer or boolean states to control the transitions.
Below is a __pseudocode__ example.

```
# NOTE: Escape is used to quit the game, space is used to start the game,
# and return is used to pause.
# Your code will vary!

GAME_OVER = 0
PLAY      = 1
PAUSED    = 2

state     = GAME_OVER
exitgame  = False

while not exitgame:
    # Exit the game
    if user_input() == ESC:
        exitgame = True
        continue

    # Game Over State
    if state == GAME_OVER:
        show_text("Game Over")
        show_subtext("Press space to play.")
        if user_input() == SPACE:
            state = PLAY
            continue

    # Paused State
    elif state == PAUSED:
        show_text("Paused")
        if user_input() == RETURN:
            state = PLAY
    
    # Play State
    else:
        run_game()
        
        if lives <= 0:
            state = GAME_OVER
            continue
        
        if user_input() == RETURN:
            state = PAUSED
            continue
```
> If you are unfamiliar with a continue statement, it is a control statement (similar to a break or return).
  A continue, however, does not break out of a loop, but instead goes to the top of a loop.
  For example, the continues in the pseudocode would all immediately jump up to the `while not exitgame` loop.

## Debugging Movement
In this lab you will start debugging the motion of the ball, and the collisions on bricks.
This is one aspect in which you will have a lot of freedom to design your own motion.
I encourage you to implement ideas outside of the given code to implement movement.
The only restriction is that your movement should not feel bad to play with, and you should not experience clipping with the paddle and the ball or a brick and the ball.

## Game Statistics
In addition to the states and movement, you will also start keeping track of the score, lives, and level.

When a user hits a block (or destroys a block, you can choose), the score should be incremented.

When a user destroys the last block in a level, a set of new blocks should appear as part of a new level.
Your ball should also be reset to its initial position when a level changes.
Your level should increment upon completion of the last level.

Every time the ball goes off screen, the lives of the player should decrease by 1.

When a user runs out of lives, the game should end.
When the user starts up the game again, the level should be reset to 1, the score should be set to 0, and the number of lives should be reset to the starting number.

## Writing Text to the Screen
In order to display statistics to the user, you will need to write to the screen.
The following code snippets may help.

__given.py__
```
import pygame

import random

#############################
# HELPERS FOR TEXT RENDERING
#############################

# Initialize the font library.
pygame.font.init()

class Fonts:
    TEXT_FONT     = pygame.font.SysFont('Impact', 30)
    TITLE_FONT    = pygame.font.SysFont('Impact', 100)
    SUBTITLE_FONT = pygame.font.SysFont('Impact', 50)

class Colors:
    WHITE      = (255, 255, 255)
    BLACK      = (  0,   0,   0)
    RED        = (255,   0,   0)
    GREEN      = (  0, 255,   0)
    BLUE       = (  0,   0, 255)
    CYAN       = (  0, 255, 255)
    MAGENTA    = (255,   0, 255)
    YELLOW     = (255, 255,   0)
    LIGHT_GREY = (192, 192, 192)
    GREY       = (128, 128, 128)
    DARK_GREY  = ( 64,  64,  64)

def draw_text_to_screen(screen, text, x, y, color, font):
    render_text = font.render(text, False, color)
    screen.blit(render_text, (x, y))
```

__main.py__
```
from src.given import Fonts
from src.given import Colors

# Write "Paused" to the screen
given.draw_text_to_screen(screen, 'Paused', <topleftx>, <toplefty>, Colors.WHITE, Fonts.TITLE_FONT)

```
## Submission
For this lab, you will present your results to your instructor in the Week 12 Scrum.
Your instructor will ask additional questions regarding your implementation and other general knowledge.

## Rubric
* 40 - Participation
* 25 - Working States in the Game
  * 15 - Implemented a Game Over Screen
    * 5 - Game Over screen is displayed when the game starts.
    * 5 - Game Over screen transitions to the game upon user input.
    * 5 - Game Over screen is displayed when the user runs out of lives
  * 10 - Working pause menu
    * 5 - Pause menu is triggered by user input. (Pause menu cannot be activated during the Game Over screen)
    * 5 - Pause menu is terminated by user input.
* 20 - Brick deflection is fluid and fun to play (i.e. not buggy)
* 15 - Game keeps track of score, lives, and level.
  * 3 - Score is increased when hitting bricks (or destroying them).
    > I will leave this as a creative choice to you.
  * 3 - Lives are decreased when the ball falls off the screen.
  * 3 - Levels are increased when a user destroys the last block on the screen.
  * 3 - New Bricks are generated when a user completes a level.
    > __NOTE:__ An ideal game would also reset the ball at this point.
  * 3 - Score, lives, and level are reset when it is game over.

# Lab 12 - Binary File I/O
One way that we will modernize this game is by allowing the user to save.
When the original Breakout was developed there was no way of saving a game, and once the power was turned off, all scores and progress were lost.

We will use binary file I/O to save and load the game.

## Binary File I/O
We will be saving the values as bytes for 2 reasons.
1. Raw binary is smaller than saved text.
2. Raw binary can be converted more easily into number values than string text.

When writing binary we will be using the python `struct` module to pack and unpack bytes.
Those bytes are then fed into a `bytearray` object which can be written to a file.

### Some Theory
The pack and unpack functions take 2 parameters, a `format string` and the `data objects` themselves.
The format string defines how your data is represented (e.g. how many ints, floats, or characters).
The format string also describes the `Endian` or arrangement of bytes.
`Little Endian` is a format which defines a byte order as `Least-Significant Bit (LSB)` to `Most-Significant Bit (MSB)`
`Big Endian` is the opposite, it defines the byte order in the standard `MSB` to `LSB` format.

For example the format string `'>id'` says that there is a integer followed by a floating point number represented in big endian format.

If we used the following binary string as an example, we would pull out. `5` and `5.0`.

`00000000 00000000 00000000 00000101 1000000 10100000 00000000 00000000`

This string contains 8 bytes, the first 4 represent a binary integer, and the second 4 bytes represent a binary floating point number.

Changing the `Endian` of a byte string does not simply reverse the order of the bits, instead it, changes the bit order of each byte.

If we were to rewrite the above string in `Little Endian` it would be written like so.

`10100000 00000000 00000000 00000000 0000000 00000000 00000101 00000001`

If you need more reference materials, please review the [slides](docs/Binary_File_IO.pdf) from class tonight.

### Some Practice
Now that we have seen how the formatting works, we can actually implement it.
The beauty of the `struct` module is that it allows us to skip having to manually calculate or write code to manipulate bits.

The following is some sample code for reading and writing in binary.

__read_binary.py__
```
import struct
import os.path

if __name__ == '__main__':

    # Instantiate list (i.e. Memory object)
    int_list   = []
    float_list = []

    # Open the file to read in binary
    with open(os.path.join("data", "test_file.dat"), "rb") as bin_in:
        # Read the file as raw binary
        ba = bytearray(bin_in.read())

    # Designate format
    format = '>id'
    
    # Designate the chuck size of the byte array.
    # A chunk is a volume of information that is extracted in a given
    # iteration through the bytearray.
    # This is the reverse of extending the byte array.
    chunk_size = struct.calcsize(format)

    # Determine how many chunks are in the bytearray
    num_chunks = len(ba) // chunk_size
    
    # For every chunk in the list
    for i in range(num_chunks):
        # Slice the bytearray into a given chunk of data
        chunk = ba[i * chunk_size : (i+1) * chunk_size]
        
        # Unpack the chunk into a tangible value
        int_value, float_value = struct.unpack(format, chunk)
        
        # Append the values to the list.
        int_list.append(int_value)
        float_list.append(float_value)

```

__write_binary.py__
```
import struct
import os

if __name__ == '__main__':

    # Define data
    int_list       = [1, 42, 13]
    float_list     = [3.14, 42.0, 3.14/2]

    # Designate format
    format='>id'

    # Instantiate an empty bytearray
    ba = bytearray()
    
    # iterate through each list
    for int_value, float_value in zip(int_list, float_list):
        # Pack each set of bytes
        chunk = struct.pack(format, int_value, float_value)
        # Append the bytes to the output
        ba.extend(chunk)

# Open the file to write binary and write the bytes.
file_path = os.path.join("data", "test_file.dat")
with open(file_path,"wb") as bin_out:
    bin_out.write(ba)
```

## Implementing Binary File I/O in Breakout
When adding save files, you should adhere to the following.

* The game should be saved whenever a user exits the screen.
* If there is a save file present upon loading the game, the previous game state should be loaded instead of starting a new game.
* If the user runs out of lives during the game, any previous save files should be deleted.
* If the game is loaded into its game over state, no save file should be created.

__Things you will need to keep track of.__
* Game
  * Score
  * Level
  * Lives
* Ball
  * Location
    * X-Position
    * Y-Position
  * Motion
    * Velocity
    * Theta
    * __OR__
    * X-Velocity
    * Y-Velocity
  * State __(Add this for Lab 13)__
    * Power-Up Status
      * Power-Up Type
      * Power-Up Time
* Paddle
  * Location
    * X-Position
    * Y-Position
* Bricks __(for each brick)__
  * Location
    * X-Position
    * y-Position
  * Status
    * Health
    * Power-Up Brick __(Add this for lab 13)__

### Binary File I/O Notes
When importing and exporting states, you will notice that various objects have different types of information.
This means that the binary format of a brick will differ from that of a ball.
When reading and writing binary files, you will need to use multiple formats when packing and unpacking data.

When importing data, your approach will be similar to that of lab 6.
You will take in the data and instantiate objects based on the data (e.g. given a Brick's location and health, instantiate that brick and add it to the screen).
   
## Submission
For this lab, you will present your results to your instructor in the Week 13 Scrum.
Your instructor will ask additional questions regarding your implementation and other general knowledge.

## Rubric
* 40 - Participation
* 20 - You can create a game save state.
* 20 - Loading data works.
* 10 - No extraneous files are created.
  > No files are created when it is game over.
* 10 - Stale save files are deleted once it is game over.

# Lab 13 - Integration
This will be the final lab for this project.
In this lab you will add to your game to make it stand out and be truly unique.

This lab is titled __integration__ because typically the final step in a software project the __integration__ and __test__ phase.
During this step, you will iron out all of the bugs in your project.
Keep in mind that a bug may be any faulty code that needs to be addressed, but it may also refer to the __User Experience (UX)__ of your game.

Upon the completion of the lab, your game should:
* Not crash! (This is important!)
  * If you have strange issues, you may want to consider implementing a __try/except__ block.
* Transition from state to state.
* Not have __artifacting__ (stale pixels that need to be removed from the screen).
* Have all text displaying correctly.
* Be intuitive:
  * You should not have to explain the nuances of your game to me, it should be very obvious where everything is.
  * You should tell me all of the inputs (Movement/pausing/starting the game) (I recommend putting these on the "Game Over" screen).
* Not have __spaghetti code__ (that is, code which is overcomplicated or difficult to read or modify).
* Be unique from everyone else's.

There are no general guidelines to this lab other than whatever you add should be significant.
> __NOTE:__ As a rule of thumb, you should put in at least the same level of effort into this lab as the other labs in the project.

For those who may have fallen behind in previous weeks, please use this lab as an opportunity to catch back up and created something you can be proud of.

## Ideas
Here are some implementation ideas that you may want to explore.
Pick a couple of these if you don't have any ideas.

* Use File I/O or Binary File I/O to save high scores and the names of the best players. __(Medium)__
* Add a power up to the game:
  * Add a damage powerup that destroys all bricks and is not deflected by bricks. __(Medium)__
  * Add a multi-ball powerup that allows for 3 balls to be present on the screen at once. __(Hard)__
  * Add a powerup that  temporarily increases the size of the paddle. __(Medium)__
* Add an acceleration due to gravity which changes how the ball moves. __(Medium)__
* Add varying coefficients of restitution that change how ball reflects (more or less velocity) __(Medium)__
* Modify the force that various bricks impart on the ball upon deflection. __(Medium)__
* Create a requirement that certain bricks must be destroyed before others. __(Hard)__
* Add sound effects or background music to your game. __(Easy-Hard)__
* Create new fancier sprites. (Please don’t simply pilfer online assets). __(Easy-Hard)__

## Polishing your Game
Before your demo and submit your final game, please make sure that the game itself looks and feels good to play.
Polish is very important on a front-facing product.

Additionally, since I will be checking through your code, please clean up your code and __refactor__ it to be as clean as possible.
If you need to tips on implementing this, please refer to the lab syllabus.

## Submission
For this lab, you will present your project during Lab 14.
If you have any addiitonal content other than the game, you will submit this via Scholar in the "Presentations Assignment".

## Rubric
* 40 - Participation
* 30 - You game has at lease 1 unique feature (or several smaller features)
* 20 - Your game has been polished up (i.e. you have decent looking sprites and other assets, ball movement is solid).
* 10 - Your game's code is polished.

> __NOTE:__ This last lab is meant as an opportunity to have fun and enjoy the fruits of your labor in the last weeks.
A lot of the grade is going to be based on effort.

# Presentations

The first 20 minutes of the final lab will involve taking the "Super" quiz.
The "Super" quiz will count for 2 quiz grades (4% of your overall grade).

The remaining 85 minutes will be spent on group presentations.
Each group will present their project.
The purpose of this lab is to gain additional practice presenting and evaluating the presentations of others.

I want you all to treat this as an "Elevator Pitch" to your future boss.
The purpose is to show what you've done, how it is unique, and what you've gained from it.

Keep in mind that this is will be a short presentation.
Realistically, it should not take more than 1-1.5 hours to put your slides together.
If you find yourself going over, please trim down the content before submission.
There is a "Goldilocks" amount of content that you should keep in mind.

This is __NOT__ a public speaking course, and I will __NOT__ grade you on your demeanor during the presentation.
Being nervous, using filler words (e.g. like, um, etc.) will not count against you.
I am only grading based on the quality and amount of content that you present.

## Presentation Layout

Please use the following format to structure your slides:

* Introduction slide (1 slide)
  > Who is in your team.
  
* Brief overview of your game (1-2 slide[s])
  > Describe the rules of your game.
  > Describe what unique things you did to your game.
  > Show some screenshots or gameplay video from your game.
  
* A brief diagram describing how your game works (1-2 slide[s])
  > Draw the states of your game.
  > Draw the state transitions.
  > Draw a diagram of your game (how classes interact).
  
* Challenges (1 slide)
  > What roadblocks did you hit along the way?
  > What design decisions did you have to make?
  
* Accomplishments/Lessons Learned (1 slide)
  > How did you overcome the aforementioned roadblocks?
  > What did you learn from this project?

I want you to work with __Google Slides__ for this project (see the Submission section for more information).

You and your partner must present for no fewer than __4 minutes__ and no longer than __6 minutes__.
If your presentation is too long or short I will take off 10 points per minute (__yes, I will be timing__).
> You and your partner should practice presenting before the final lab (At least run through the presentation once)!

If you take longer than 7 minutes, I will likely cut you off (don't make me do this)!

> __NOTE:__ You must submit (share) the presentation to me by the due date.
I will provide a computer and a clicker for you to present with.
I will load your presentations ahead of time, so everything will be ready to go and the order will mostly be random.

## SlideShows 101
Having to present on a topic is common for most disciplines, this is especially true in engineering fields.
Being able to present effectively is a valuable skill that comes from practice.
That being said, there are a few basic rules to follow when making a presentation.
> You will not be graded based on this section, these are only tips to help you improve your presentation skills.

__Content:__
* YOU should be doing the talking, not your slides.
In other words, __PowerPoint != Presentation__.
Presentations should contain only the basic bullet points to keep you on track during your presentation.
They should not contain all of your speech!
These layouts are affectionately called __word walls__, and they make for bad presentations.
* Presentations should convey visual ideas that are difficult to describe.
* You should know your audience, tailor your slides to match the level of detail required for your audience.

__Presenting:__
* You should know your presentation before you present, looking at your slides instead of your presentation reflects poorly.
* Going off on tangents will make it difficult for your audience to understand the key points.
* Try not to stray from the bullet points on each slide, this coincides with going off on tangents.
* Don't read verbatim from the slides, YOUR AUDIENCE CAN READ THEM!
  Elaborate on your points instead!
  Your audience will get an understanding of the subject matter from your points, your job is to fill in the blanks with your speech.
* Try to avoid lingering on slides, you will lose your audience's attention with stale slides.
  Exceptions to this are visual slides or highly detailed slides.
  Ways to avoid this with detailed visuals is to break up your slide into sections, or copy the visual onto multiple continuous slides.


### Live Demo (Optional)
I will allow up to 5 groups per class to show a live demo of their game.
You __MUST__ make sure that your game works and that you have a machine to present it with (you need an __HDMI Port__).
If you choose to show a live demo, you will be given a couple of extra minutes to setup and show the demo.
You can use this as an opportunity to practice demonstrating live software.

I will send out an email shortly to see who is interested in presenting a live demo.
The slots will be given on a __First-Come, First-Serve__ basis.
If you have a slot and are no longer able to present, please notify me immediately so that I can reallocate the slot.
Please keep the live demo as short and concise as possible, please do not go over 2 minutes with it.

If you present a live demo, your slides must still contain screenshots/live video gameplay.
You may use your live demo to help supplement your gameplay slides (i.e. You can go through your slides more quickly if you have a live demo).
> __NOTE:__ Presenting a live demo will neither hurt your grade nor help your grade.
It is only being offered to give you an opportunity to practice presenting live software.

## Submission
In order to receive credit for this lab, you must be present in lab to present your Breakout game.
You must also be present for the duration of the lab to watch other groups present, only excused absences will be allowed.
I will evaluate your presentation during class.

Given the number of groups, we will be constrained for time.
Therefore everyone must have a presentation ready to go.
In order to facilitate this, I want you to use Google Slides and __share__ your slides with me by the due date.
Please use your CNU Drive account (associated with your CNU email).
Please share to the appropriate email address:
* __mathew.bartgis.11@cnu.edu__
* __jonathan.hill.15@cnu.edu__

## Rubric
* 50 - Quality of your content.
  * 20 - Describe your game states definitions and state transitions.
  * 15 - Describe the architecture of your game.
  * 15 - Describe the technical challenges you faced.
* 50 - Quality of your slides.
  * 10 - None of your slides are __word walls__.
  * 15 - You have visuals of your game.
  * 15 - You have visuals/diagrams of your game's structure.
  * 10 - You have concise bullet points.

__Presentation Length:__
I will take the final score from above and take off points for going under 4 minutes or over 6 minutes.
For example, a presentation that goes for 6:30 minutes or 3:30 minutes would lose 5 points, while a project that goes for 4:00 minutes exactly or 5:59 minutes would not lose any points.

__Presenters:__
Each partner should present for an equal amount of time.
If one partner presents for a majority of the time, I will take off points from the entire group!

# Final Submission
As mentioned earlier, there will be a final submission for this project.
This final submission will be worth __300 points__.
This final submission needs to be submitted on an __individual__ basis (each partner submits).
Please do not forget to submit something!

The final submission deadline is due on the start of Week 14 (Presentations).

> __NOTE:__ I will not grade your programs on the day of the presentations.
Instead there will be a grace period extending until `Friday, 4/26/2019 at 11:59 pm`.
If you need to continue working on your program, you may take up until this time.

## Final Submission Rubric
Your final project will be graded as follows.
> __NOTE:__ This rubric does not contain participation credit, this submission will be graded on content.

* 60 - Game Mechanics
    * 10 - Your ball should be controllable with the paddle
      > You should not use the default `angle = -angle`.
    * 10 - Your ball should deflect off of the bricks in a clean manner.
      > Your ball should not phase through bricks on side hits or top/bottom hits.
    * 10 - Your ball should start on top of the paddle or bounce down to the paddle when a level starts or a new life is used.
      > An ideal solution would have the ball follow the paddle and get launched once the user hits a key.
    * 10 - Blocks should have variable health
    * 10 - Blocks should be identifiable by their health.
    * 10 - Blocks should disappear once their health <= 0.
* 50 - Game States
    * 10 - Your game should start in the Game Over phase (unless there is currently a saved game).
    * 10 - Your game should transition to the play phase on user input.
    * 10 - Your game should transition to the Game Over phase once the user runs out of lives.
    * 10 - Your game should transition to the Paused state on user input from the play state.
    * 10 - Your game should transition to the Play state on user input from the paused state.
* 40 - Game Stats
    * 10 - Your game should visually keep track of score
    * 10 - Your game should visually keep track of level count
    * 10 - Your game should visually keep track of lives
    * 10 - Your game should reset all stats when it is Game Over
* 50 - Game Saves
    * 15 - Your game should save to a binary file.
    * 15 - Your game should load from a binary file if one is available.
      > This is the condition when the game should bypass the Game Over state (however, you may still have it so long as the previous game is loaded on the state transition instead of a new game).
    * 10 - Your game should not create extraneous files
      > If you are in the game over screen, you should not make a save.
    * 10 - Your game should remove stale (old) save files once it is Game Over.
  50 - Game Design
    * 30 - Your game should have additional work put into it which makes it unique (Lab 13).
      > This will be effort based and will be derived from the amount of content added.
    * 10 - Your game should have multiple levels where new bricks are generated each time the level changes.
    * 10 - Your game should progressively become harder.
  
  50 - Game Quality
    * 20 - Your game should be aesthetically appealing.
      > You game should be smooth to play, not have any sprite or text artifacting, and have all sprites aligned properly.
        While not required, you may add new sprites, sound effects, or background music.
        Adding new content can ONLY HELP YOU!
    * 30 - Your code will be subject to a manual code inspection.
      I will be evaluating your code as follows
        * Frequent and concise comments added to your code.
        * Python documentation added to classes and functions.
        * Using proper variable, function, and class names.
        * Creating modular code (i.e. Reusing code where possible)
        * Effective use of classes (i.e. Using object instantiation where appropriate).


# Additional Documentation

[Command Line Interfaces](docs/cli.md)

[Installing with pip](docs/numpy_matplotlib_installation.md)

[Instantiation Example](docs/car_example.md)

[PyGame Docs & API](https://www.pygame.org/docs/)
