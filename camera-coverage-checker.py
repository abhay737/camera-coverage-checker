def is_camera_set_sufficient(required_distance, required_light, cameras):
    min_distance, max_distance = required_distance
    min_light, max_light = required_light

    distance_points = [min_distance, max_distance]
    light_points = [min_light, max_light]

    for camera in cameras:
        distance_points.extend(camera['distance'])
        light_points.extend(camera['light'])

    distance_points = sorted(set(distance_points))
    light_points = sorted(set(light_points))

    for i in range(len(distance_points) - 1):
        for j in range(len(light_points) - 1):
            
            test_distance = (distance_points[i] + distance_points[i + 1]) / 2
            test_light = (light_points[j] + light_points[j + 1]) / 2

            if not(min_distance <= test_distance <= max_distance and min_light <= test_light <= max_light):
                continue
            
            covered = False

            for camera in cameras:
                if(camera['distance'][0] <= test_distance <= camera['distance'][1] and camera['light'][0] <= test_light <= camera['light'][1]):
                    covered = True
                    break
            
            if not covered:
                return False

    return True
    
required_distance = (0, 100)         
required_light = (0,100)
cameras = [
    {'distance': (0, 50), 'light': (0, 100)},
    {'distance': (50, 100), 'light': (0, 100)},
]
print('Is camera set sufficient:', is_camera_set_sufficient(required_distance, required_light, cameras))