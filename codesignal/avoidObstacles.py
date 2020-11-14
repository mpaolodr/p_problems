def avoidObstacles(inputArray):

    obs_set = set(inputArray)
    min_obs = min(inputArray)
    max_obs = max(inputArray) + 1

    minimum = None

    for j in range(1, max_obs + 1):

        clear = True

        for num in range(0, max_obs + 1, j):

            if num in obs_set:

                clear = False
                break

        if clear:

            if minimum is None:

                minimum = j

            else:

                if minimum > j:

                    minimum = j

    return minimum
