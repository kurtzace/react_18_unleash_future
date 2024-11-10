### Diving into Reinforcement learning via AWS Deep Racer

Reinforcement learning (RL) is a type of machine learning where an agent learns to make decisions by performing actions and receiving rewards.

**Key Concepts:**
- **Agent**: The learner or decision maker (e.g., DeepRacer car).
- **Environment**: The world the agent interacts with (e.g., the race track).
- **State**: The current situation of the agent (e.g., position on track).
- **Action**: The decision taken by the agent (e.g., move forward, turn left).
- **Reward**: The feedback from the environment (e.g., staying on track).

@


**Equations:**
- **Policy**: \( \pi(a|s) \) - The strategy that the agent uses to determine the next action based on the current state.
- **Value Function**: \( V(s) = \mathbb{E}[R|s] \) - The expected reward for a state.
- **Q-Function**: \( Q(s, a) = \mathbb{E}[R|s, a] \) - The expected reward for a state-action pair.

![image](https://github.com/user-attachments/assets/3abddebb-62f8-4ac5-8917-7799e5af9f49)

^



### Reinforcement Learning Basics from Udemy

**State**: 
- Chess: location of pieces of board and remaining time.
- Position of object, rotating , time
- Avatar position of ghost, agent, time

**Action**:
- Modify rotation
- button we press

**Reward**:
- effectiveness of decision making, goal based. +ve or -ve reward. 
- eat yellow pill. feedback
@


**Agent**:
- Entity will participate in tasks (human being/ algo)

**Environment**: 
- Agent cant control 100, opponent. gravity, friction. 

Markov Decision Process (discrete finite time , stochastic (future is modified partially) control process - decision)

![image](https://github.com/user-attachments/assets/36eee823-0160-4a9e-9e71-14acf15e31d2)

^




### Finite Markov Decision Process

**Key Points**:
- Episodic (terminates) or Continuing
- Trajectory: elements generated when agent moves from state to another.
- Episode: Trajectories to final state
- Reward (maximize sum) vs Return (short term return may impact long -term reward)

![image](https://github.com/user-attachments/assets/18885f58-f9e7-4f54-b7d2-e664a8210d24)

^




### Tic-Tac-Toe Analogy

The agent interfaces with the game (via the API)

```python
game.start() 
while not game.is_over() 
  state = game.getstate() 
  ### do something intelligent 
  location = agent.pick_move(state) 
  ### make the move game.move(symbol, location) 
```
@


**Key Points**:
- Episode = game/round/match
- The agent will try to maximize its reward

![image](https://github.com/user-attachments/assets/275ea771-56c8-46b2-abb6-3c2a0996d700)

^




### Policy and Value Functions

**Policy**: Yield an action - given a current state

```python
def get_action(s): 
    if random() < epsilon: 
        a = sample from action space 
    else: 
        a = fixed policy[s]  
    return a
```
@


Policy parameter - W (shape is D x |A|)

```math
π(a|S) = softmax(W^T s)
```

![image](https://github.com/user-attachments/assets/8ea6bba0-0757-4e86-802d-aa6eb55a12f4)

^




### Bellman Equation

Bellman equation for state values:

![image](https://github.com/user-attachments/assets/dda5d110-619f-4d38-85e5-b5d6e4f3ef8a)

Bellman equation for Q-values:

![image](https://github.com/user-attachments/assets/28ec8159-2103-4c2c-934e-953e814a126e)

^




### Learning and Exploration

**Learning Process**:
- Calculate returns
- Update Q-values
- Improve policy

**Explore-Exploit Dilemma**:
- Explore: collect more data to determine best outcome
- Exploit: play with best policy to win
@


Monte Carlo: requires terminal state

![image](https://github.com/user-attachments/assets/5e073f59-1dbf-443f-ac60-6c6cc3b94368)

^




### AWS DeepRacer Experience

AWS DeepRacer is a 1/18th scale race car that gives you an exciting way to get started with reinforcement learning (RL).

![image](https://github.com/user-attachments/assets/b8068b79-b553-4474-b12f-f95b3a2ca71f)

@



**Car Features:**
- Intel Atom processor
- Intel distribution of OpenVINO toolkit
- Front-facing camera (4 megapixels)
- System memory: 4 GB RAM
- 802.11ac Wi-Fi
- Ubuntu 20.04 Focal Fos
- ROS 2 Foxy Fitzroy
- AWS DeepRacer Evo Expansion Pack
- Second front-facing camera (stereo cameras)
- 260-degree, 12-meter scanning radius Lidar sensor

^




### 3D Racing Simulator

AWS DeepRacer uses a 3D racing simulator to train models in a virtual environment.

![image](https://github.com/user-attachments/assets/2593ba5e-8ecb-4ee0-9e43-8579cbd73247)
@


**Key Concepts:**
- **Agent**: The DeepRacer car
- **Environment**: The race track
- **Action**: Decisions made by the car (e.g., speed, steering angle)
- **Reward**: Feedback based on the car's performance (e.g., staying on track)

**Episodes**: Training iterations from start to finish or until the car drives off the track.

^




### Reward Functions

Reward functions are critical in guiding the agent's learning process.

![image](https://github.com/user-attachments/assets/f3eff8a9-916e-462e-bd2e-7ae2a8169f86)
@


**Key Parameters:**
- **Position on Track**: (x, y) coordinates
- **Heading**: Orientation of the car
- **Waypoints**: Ordered list of milestones on the track
- **Track Width**: Width of the track
- **Distance from Center**: Distance of the car from the track centerline
- **All Wheels on Track**: Boolean indicating if all wheels are on the track
- **Speed**: Current speed of the car
- **Steering Angle**: Angle of the front wheels

^




### Example Reward Functions

**Follow Center Line**

This reward function incentivizes the car to stay close to the center of the track.

```python
def reward_function(params):
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']

    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3

    return float(reward)
```
@


**Prevent Zig-Zag**

This reward function penalizes excessive steering to prevent zig-zag behavior.

```python
def reward_function(params):
    distance_from_center = params['distance_from_center'],  track_width = params['track_width'], abs_steering = abs(params['steering_angle'])

    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    if distance_from_center <= marker_1:  reward = 1.0
    elif distance_from_center <= marker_2: reward = 0.5
    elif distance_from_center <= marker_3: reward = 0.1
    else:  reward = 1e-3
    ABS_STEERING_THRESHOLD = 15
    if abs_steering > ABS_STEERING_THRESHOLD: reward *= 0.8
    return float(reward)
```

^




### Setting Up Your Racer Profile

![image](https://github.com/user-attachments/assets/61cc3cca-5f6d-4afe-9e8d-2db46c692c20)
@


**Example Track:**
A to Z Speedway
- Length: 16.64 m (54.59')
- Width: 107 cm (42")
- Direction: Clockwise, Counterclockwise

^




### Clockwise Waypoints

Downloaded the track numpy file and plotted the waypoints for the clockwise track.

![image](https://github.com/user-attachments/assets/99a452e7-6794-475b-b72e-caff17218f4d)
@


```python
import matplotlib.pyplot as plt
import numpy as np
tracksPath = '~/Downloads/reInvent2019_wide_cw.npy'
track_name = "A to Z Speedway"
absolute_path = "."
waypoints = np.load(tracksPath)
print("Number of waypoints = " + str(waypoints.shape[0]))

for i, point in enumerate(waypoints):
    waypoint = (point[2], point[3])
    plt.scatter(waypoint[0], waypoint[1])
    plt.text(waypoint[0], waypoint[1], str(i), fontsize=9, ha='right')
    print("Waypoint " + str(i) + ": " + str(waypoint))

plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title(f'Waypoints for {track_name}')
plt.show()
```

^




### Clockwise Reward Function

The Clockwise Reward Function incentivizes the car to follow the correct speed and direction based on waypoints.

[Link to code snippet](code/clockwise_reward_function.py)

**Key Points:**
- Penalize for offtrack.
- Prevent zig-zag behavior.
- Reward for maintaining appropriate speed based on waypoints.
- Adjust rewards based on distance from center.
- Heading direction reward for maintaining the correct heading.

^




### Percentage Reward Function

The Percentage Reward Function adjusts rewards based on the car's progress along the track.

[Link to code snippet](code/percentage_reward_function.py)

**Key Points:**
- Penalize for offtrack or reversing.
- Prevent zig-zag behavior.
- Reward for maintaining appropriate speed based on progress percentage.
- Adjust rewards based on distance from center.
- Heading direction reward for maintaining the correct heading.

^




### Conclusion

AWS DeepRacer combines the excitement of racing with the challenge of machine learning, making it an excellent tool for both education and entertainment.

</section>
```
