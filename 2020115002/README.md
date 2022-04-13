# Clash of Clans

## Introduction

The game is terminal-based where I display the village base using ascii chart. The base.render() function is called again and again in game.py in order to display the base (rendering the changes that have taken place). The user input is taken in base.get_key() using input_to() function from input.py. The timeout for input is set to 0.5 seconds. I have used the OOPS concepts (Polymorphism, Encapsulation, Inheritance and Abstraction) to deliver the required functionalities.

## Village

- Spawning points:
  There are 3 spawing points for the troops:
  Barbarians:
  i - (70,5)
  j - (70,40)
  k - (10.40)

  Archers:
  b - (70,5)
  n - (70,40)
  m - (10.40)

  Balloons:
  z - (70,5)
  x - (70,40)
  c - (10.40)

- Town Hall:
  Coordinates: (45,20)
  Width: 4
  Height: 3
  Hitpoints: 300

- Huts:
  Width: 1
  Height:1
  Hitpoints: 20
  There are 5 huts in total around the corners of the village.

- Cannons:
  Coordinates: (30,15), (55,30)
  Width: 2
  Height: 1
  Hitpoints: 50
  Damage: 10

  The cannon attacks ground troops within a raduis of 10. It targets a single troop until it dies or goes out of range. The time delay for shooting is 1 second.

- Wizard Towers:
  Coordinates: (35,15), (50,30)
  Width: 2
  Height: 2
  Hitpoints: 50
  Damage: 10

  At a given point, the wizard tower can only target a single troop. The wizard tower deals AoE damage in a 3x3 tile area around the troop it is attacking. The time delay for shooting is 1 second. The wizard tower attacks ground as well as air troops.

- Walls:
  Width: 1
  Height: 1
  Hitpoints: 10
  Walls are present around the townhall and the two cannons.  

All the buildings (except walls) change in colour from green to yellow to red based on their hitpoints. Once the hitpoints become 0, they disappear from the village base. Walls only have one colour and they disappear when destroyed.

## Levels
A level system is implemented in the game. For higher levels, the number of cannons and wizard towers increases:

- Level 1:
  2 cannons {(30,15), (55,30)}
  2 wizard towers {(35,15), (50,30)}

- Level 2:
  3 cannons {(30,15), (55,30), (65,15)}
  3 wizard towers {(35,15), (50,30),(60,15)}

- Level 3:
  4 cannons {(30,15), (55,30), (65,15),(25,30)}
  4 wizard towers {(35,15), (50,30),(60,,15),(30,30)}

## Hero

The user can either select king or queen.
He needs to press '1' for king and '2' for queen.

### King

Coordinates: (70,15)
Width: 3
Height: 2
Hitpoints: 200

The king's health is displayed by a health bar.

Movement:
The King is controlled with W/A/S/D which correspond to Up/Left/Down?Right.
<SPACE> is used for sword attack. The King attacks a single building with a sword when he is in contact with the building. In case of multiple buildings in contact, the priority order to attack is: Townhall > Cannons > Hut > Wall.
The movement of the King is restricted, i.e. he cannot move through the buildings unless they are destroyed.

'l' is used for axe attack where the king can attack any building within the radius of 5.
Time delay for action: 0.25 seconds.

Colour:
Normal: Magenta
Attack with sword: Red
Attack with axe: Blue

### Queen

Coordinates: (70,15)
Width: 3
Height: 2
Hitpoints: 150

The queen's health is displayed by a health bar.

Movement:
The queen is controlled with W/A/S/D which correspond to Up/Left/Down?Right.

<SPACE> is used for normal attack. The queen attacks a distant AoE location which is a 5x5 area whose center is 8 tiles away from the queen’s location in the last-moved direction of the queen. 

'l' is used for eagle arrow attack. The queen launches a volley of arrows high into the air that reach the ground 1 second after being shot, dealing damage to all buildings in the AoE. The queen now attacks an AoE location which is a 9x9 area whose center is 16 tiles away from the queen’s location in the last-moved direction of the queen. 

Colour:
Normal: Magenta
Attack with sword: Red
Attack with eagle arrow: Blue

## Troops

- Ground Troops: Barbarians, Archers, King and Queen
- Air Troops: Balloons

### Barbarians

Number: 5
Width: 1
Height: 1
Colour: Red
Hitpoints: 30
Damage: 3

The barbarians can be spawned only at the specified spawning points. After they spwan, they move to the nearest non-wall building and attack it. If there is no non-wall building, they move to the nearest walled building, destroy the wall first and then attack the corresponding building.
The movement and attack is automated.
Time delay for action: 0.5 seconds

### Archers

Number: 5
Width: 1
Height: 1
Colour: Blue
Hitpoints: 15
Damage: 1.5

The archers can be spawned only at the specified spawning points. After they spwan, they move to the nearest non-wall building and attack it. If there is no non-wall building, they move to the nearest walled building and attack it. Archers can attack over walls. They can attack a single building at a time which falls within a radius of 12.
The movement and attack is automated.
Time delay for action: 0.25 seconds

### Balloons

Number: 3
Width: 1
Height: 1
Colour: LightBlue
Hitpoints: 30
Damage: 6

The balloons can be spawned only at the specified spawning points. After they spwan, they move to the nearest defense building and attack it. If there is no defense building, they move to the nearest non-defense building and attack it. Their movement is not restricted by walls and buildings.
The movement and attack is automated.
Time delay for action: 0.25 seconds


Once the troops are dead, they cannot move or attack and are displayed in light_black.

## Spells

1. Rage: 
   Number: 1
   Time: 5 seconds
   Increases the damage of all the troops by two.
   Increases the movement speed of the king by two.
   Decreases the time delay of action for barbarians to 0.1 seconds.
   The village base colour turns light_magenta when the rage spell is in effect.

2. Heal:
   Number: 1
   Time: 5 seconds
   Increases the health of all the troops to 150% of the current health.
   The village base colour turns yellow when the heal spell is in effect.

## Game Endings
Each game can end in either victory or defeat.
1. Victory: All buildings (excluding walls) have been destroyed.
2. Defeat: All troops and the King have died without destroying all buildings.
Once either of these conditions is satisfied, the game ends and appropriate message is displayed.

## Bonus Features:
1. King's leviathan axe feature has been implemented. The king uses 'l' to use his axe.
2. King's Iron Fist
   Time: 5 seconds
   The king's damage and speed doubles along with the spawning of four barbarians at the king's current location.
   The king's health increases to 150% of the current health.
3. Queen's Eagle Arrow feature has been implemented. The queen uses 'l' to use her eagle arrow.
