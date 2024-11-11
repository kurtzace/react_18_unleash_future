def reward_function(params):
    '''
    Reward function for a clockwise AWS DeepRacer track.
    '''
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering_angle = params['steering_angle']
    speed = params['speed']
    is_offtrack = params['is_offtrack']
    heading = params['heading']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']

    reward = 1.0

    if is_offtrack:
        return 1e-3

    if not all_wheels_on_track:
        return 1e-3

    ABS_STEERING_THRESHOLD = 22
    if abs(steering_angle) > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    waypoint_index = closest_waypoints[1]
    if 2 <= waypoint_index <= 7:
        target_speed = 1.5
    elif 7 <= waypoint_index <= 12:
        target_speed = 3.0
    elif 12 <= waypoint_index <= 24:
        target_speed = 1.5
    elif 25 <= waypoint_index <= 35:
        target_speed = 2.5
    elif 36 <= waypoint_index <= 45:
        target_speed = 1.5
    elif 45 <= waypoint_index <= 55:
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

    if target_speed == 3.0 and distance_from_center < 0.1 * track_width:
        reward += 1.0
    elif target_speed == 1.5 and distance_from_center < 0.5 * track_width:
        reward += 0.5

    if 2 <= waypoint_index <= 7 or 35 <= waypoint_index <= 45:
        if distance_from_center < 0.5 * track_width and params['is_left_of_center'] == False:
            reward += 0.5
    elif 26 <= waypoint_index <= 32:
        if distance_from_center < 0.5 * track_width and params['is_left_of_center']:
            reward += 0.5
    elif 28 <= waypoint_index <= 32:
        if distance_from_center < 0.5 * track_width and params['is_left_of_center']:
            reward += 0.5
    else:
        if distance_from_center < 0.1 * track_width:
            reward += 1.0

    def calculate_heading(point1, point2):
        return math.degrees(math.atan2(point2[1] - point1[1], point2[0] - point1[0]))

    next_waypoint = waypoints[closest_waypoints[1]]
    prev_waypoint = waypoints[closest_waypoints[0]]
    track_heading = calculate_heading(prev_waypoint, next_waypoint)
    heading_diff = abs(track_heading - heading)
    
    if heading_diff > 180:
        heading_diff = 360 - heading_diff

    reward += 1 - (heading_diff / 180)

    return float(reward)
