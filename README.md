# Flappy Bird for Gymnasium (Modified Version)

![Python versions](https://img.shields.io/pypi/pyversions/flappy-bird-gymnasium)
[![PyPI](https://img.shields.io/pypi/v/flappy-bird-gymnasium)](https://pypi.org/project/flappy-bird-gymnasium/)
[![License](https://img.shields.io/github/license/markub3327/flappy-bird-gymnasium)](https://github.com/markub3327/flappy-bird-gymnasium/blob/master/LICENSE)

This is a forked version of the original [flappy-bird-gymnasium](https://github.com/markub3327/flappy-bird-gymnasium) with added features for runtime constant configuration.

This repository contains the implementation of Gymnasium environment for
the Flappy Bird game. The implementation of the game's logic and graphics was
based on the [flappy-bird-gym](https://github.com/Talendar/flappy-bird-gym) project, by
[@Talendar](https://github.com/Talendar). 

## State space

The "FlappyBird-v0" environment, yields simple numerical information about the game's state as
observations representing the game's screen.

### `FlappyBird-v0`
There exist two options for the observations:  
1. option
* The LIDAR sensor 180 readings (Paper: [Playing Flappy Bird Based on Motion Recognition Using a Transformer Model and LIDAR Sensor](https://www.mdpi.com/1424-8220/24/6/1905))

2. option
* the last pipe's horizontal position
* the last top pipe's vertical position
* the last bottom pipe's vertical position
* the next pipe's horizontal position
* the next top pipe's vertical position
* the next bottom pipe's vertical position
* the next next pipe's horizontal position
* the next next top pipe's vertical position
* the next next bottom pipe's vertical position
* player's vertical position
* player's vertical velocity
* player's rotation

## Action space

* 0 - **do nothing**
* 1 - **flap**

## Rewards

* +0.1 - **every frame it stays alive**
* +1.0 - **successfully passing a pipe**
* -1.0 - **dying**
* −0.5 - **touch the top of the screen**

<br>

<p align="center">
  <img align="center" 
       src="https://github.com/markub3327/flappy-bird-gymnasium/blob/main/imgs/dqn.gif?raw=true" 
       width="200"/>
</p>

## Installation

To install this modified version, use:

```bash
pip install git+https://github.com/dtungpka/flappy-bird-gymnasium.git
```

## Basic Usage

```python
import gymnasium
import flappy_bird_gymnasium

# Create environment
env = gymnasium.make("FlappyBird-v0", render_mode="human")

# Basic usage remains the same as original
obs, info = env.reset()
while True:
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        break
```

## Runtime Constants Configuration

One of the main features of this fork is the ability to modify game constants during runtime using `update_constants()`. Here are the available constants:

### Speed and Acceleration
- `PIPE_VEL_X`: Pipe movement speed (default: -4)
- `PLAYER_MAX_VEL_Y`: Maximum descent speed (default: 10)
- `PLAYER_MIN_VEL_Y`: Maximum ascent speed (default: -8)
- `PLAYER_ACC_Y`: Downward acceleration (default: 1)
- `PLAYER_VEL_ROT`: Angular rotation speed (default: 3)
- `PLAYER_FLAP_ACC`: Upward acceleration when flapping (default: -9)

### Dimensions
- `PLAYER_WIDTH`: Width of player sprite (default: 34)
- `PLAYER_HEIGHT`: Height of player sprite (default: 24)
- `PLAYER_PRIVATE_ZONE`: Safe zone around player (default: calculated)
- `PIPE_WIDTH`: Width of pipes (default: 52)
- `PIPE_HEIGHT`: Height of pipes (default: 320)

Example of updating constants during runtime:

```python
# Create environment
env = gymnasium.make("FlappyBird-v0", render_mode="human")

# Update specific constants
env.update_constants(
    PLAYER_FLAP_ACC=-8,    # Weaker flap
    PLAYER_MAX_VEL_Y=12,   # Faster falling
    PIPE_WIDTH=80          # Wider pipes
)

# Continue using environment with new settings
obs, info = env.reset()
```

## Difficulty Presets

Here's how you can create and use difficulty presets:

```python
class FlappyBirdPresets:
    @staticmethod
    def easy():
        return {
            'PIPE_VEL_X': -3,           # Slower pipes
            'PLAYER_MAX_VEL_Y': 8,      # Slower falling
            'PLAYER_FLAP_ACC': -7,      # Gentler flapping
            'PLAYER_ACC_Y': 0.8,        # Slower gravity
            'PIPE_WIDTH': 60            # Wider pipes
        }
    
    @staticmethod
    def normal():
        return {
            'PIPE_VEL_X': -4,          # Default values
            'PLAYER_MAX_VEL_Y': 10,
            'PLAYER_FLAP_ACC': -9,
            'PLAYER_ACC_Y': 1,
            'PIPE_WIDTH': 52
        }
    
    @staticmethod
    def hard():
        return {
            'PIPE_VEL_X': -5,          # Faster pipes
            'PLAYER_MAX_VEL_Y': 12,    # Faster falling
            'PLAYER_FLAP_ACC': -10,    # Stronger flapping
            'PLAYER_ACC_Y': 1.2,       # Stronger gravity
            'PIPE_WIDTH': 45           # Narrower pipes
        }

# Usage example:
env = gymnasium.make("FlappyBird-v0", render_mode="human")

# Set difficulty to easy
env.update_constants(**FlappyBirdPresets.easy())

# Play game...
obs, info = env.reset()

# Later, change to hard mode
env.update_constants(**FlappyBirdPresets.hard())
```

### Creating Custom Difficulty Presets

You can create your own difficulty presets by adjusting the constants to match your desired gameplay:

```python
class MyCustomPresets:
    @staticmethod
    def super_easy():
        return {
            'PIPE_VEL_X': -2,           # Very slow pipes
            'PLAYER_MAX_VEL_Y': 6,      # Very slow falling
            'PLAYER_FLAP_ACC': -6,      # Very gentle flapping
            'PLAYER_ACC_Y': 0.6,        # Very low gravity
            'PIPE_WIDTH': 70            # Very wide pipes
        }
    
    @staticmethod
    def impossible():
        return {
            'PIPE_VEL_X': -7,           # Very fast pipes
            'PLAYER_MAX_VEL_Y': 15,     # Very fast falling
            'PLAYER_FLAP_ACC': -12,     # Very strong flapping
            'PLAYER_ACC_Y': 1.5,        # High gravity
            'PIPE_WIDTH': 40            # Very narrow pipes
        }

# Usage
env.update_constants(**MyCustomPresets.impossible())
```

## Tips for Creating Balanced Difficulty Presets

1. **Pipe Speed** (`PIPE_VEL_X`): 
   - Easier: -2 to -3
   - Normal: -4
   - Harder: -5 to -7

2. **Falling Speed** (`PLAYER_MAX_VEL_Y`):
   - Easier: 6 to 8
   - Normal: 10
   - Harder: 12 to 15

3. **Flap Strength** (`PLAYER_FLAP_ACC`):
   - Easier: -6 to -7
   - Normal: -9
   - Harder: -10 to -12

4. **Gravity** (`PLAYER_ACC_Y`):
   - Easier: 0.6 to 0.8
   - Normal: 1.0
   - Harder: 1.2 to 1.5

5. **Pipe Width** (`PIPE_WIDTH`):
   - Easier: 60 to 70
   - Normal: 52
   - Harder: 40 to 45


## Playing

To play the game (human mode), run the following command:

    $ flappy_bird_gymnasium
    
To see a random agent playing, add an argument to the command:

    $ flappy_bird_gymnasium --mode random

To see a Deep Q Network agent playing, add an argument to the command:

    $ flappy_bird_gymnasium --mode dqn
