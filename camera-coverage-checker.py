def is_camera_set_sufficient(required_distance, required_light, cameras):

    min_distance, max_distance = required_distance
    min_light, max_light = required_light

    distance_boundaries = {min_distance, max_distance}
    light_boundaries = {min_light, max_light}

    for camera in cameras:
        distance_boundaries.update(camera["distance"])
        light_boundaries.update(camera["light"])

    distance_boundaries = sorted(distance_boundaries)
    light_boundaries = sorted(light_boundaries)

    for i in range(len(distance_boundaries) - 1):
        for j in range(len(light_boundaries) - 1):

            distance = (
                distance_boundaries[i]
                + distance_boundaries[i + 1]
            ) / 2

            light = (
                light_boundaries[j]
                + light_boundaries[j + 1]
            ) / 2

            if not (
                min_distance <= distance <= max_distance
                and
                min_light <= light <= max_light
            ):
                continue

            if not any(
                camera["distance"][0] <= distance <= camera["distance"][1]
                and
                camera["light"][0] <= light <= camera["light"][1]
                for camera in cameras
            ):
                return False

    return True


required_distance = (0, 100)         
required_light = (0,100)
cameras = [
    {'distance': (0, 50), 'light': (0, 100)},
    {'distance': (50, 100), 'light': (0, 100)},
]
print('Is camera set sufficient:', is_camera_set_sufficient(required_distance, required_light, cameras))
