def reward_function(params):
    '''
    Simple reward function for AWS DeepRacer.
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

    if 0.3 <= speed <= 3.0:
        reward += 0.5
    
    if distance_from_center < 0.15 * track_width:
        if speed >= 3.0:
            reward += 1.0
    elif distance_from_center < 0.30 * track_width:
        if speed >= 2.0:
            reward += 0.5
    elif distance_from_center < 0.50 * track_width:
        if speed >= 1.0:
            reward += 0.2
    else:
        reward += 0.1

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
