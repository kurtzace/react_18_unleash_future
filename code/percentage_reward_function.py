def reward_function(params):
    '''
    Percentage-based reward function for AWS DeepRacer.
    '''
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering_angle = params['steering_angle']
    speed = params['speed']
    is_offtrack = params['is_offtrack']
    is_reversed = params['is_reversed']
    heading = params['heading']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    progress = params['progress']

    reward = 1.0

    if is_offtrack or is_reversed:
        return 1e-3

    if all_wheels_on_track:
        reward += 1.0

    ABS_STEERING_THRESHOLD = 15
    if abs(steering_angle) > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    if progress >= 75:
        target_speed = 4.0
    elif progress >= 60:
        target_speed = 1.5
    elif progress >= 40:
        target_speed = 3.0
    elif progress >= 25:
        target_speed = 1.5
    elif progress >= 10:
        target_speed = 3.0
    else:
        target_speed = 1.5

    speed_diff = abs(speed - target_speed)
    if speed_diff < 0.5:
        reward += 1.0
    elif speed_diff < 1.0:
        reward += 0.5
    else:
        reward += 0.1

    def calculate_heading(point1, point2):
        return math.degrees(math.atan2(point2[1] - point1[1], point2[0] - point1[0]))

    next_waypoint = waypoints[closest_waypoints[1]]
    prev_waypoint = waypoints[closest_waypoints[0]]
    track_heading = calculate_heading(prev_waypoint, next_waypoint)
    
    if progress >= 75:
        heading_diff = abs(track_heading - 180)
    elif progress >= 40:
        heading_diff = abs(track_heading + 55)
    elif progress >= 25:
        heading_diff = abs(track_heading - 0)
    elif progress >= 10:
        heading_diff = abs(track_heading - 103)
    else:
        heading_diff = abs(track_heading - 0)
    
    if heading_diff > 180:
        heading_diff = 360 - heading_diff

    reward += 1 - (heading_diff / 180)

    return float(reward)
