def fileNaming(names):

    tracker = dict()

    for name in names:

        if name in tracker:
            new_fname = name + f'({tracker[name]})'

            if new_fname not in tracker:
                tracker[new_fname] = 1
                tracker[name] += 1

            else:

                counter = tracker[name] + 1

                while name + f'({counter})' in tracker:

                    counter += 1

                tracker[name + f'({counter})'] = 1

        else:

            tracker[name] = 1

    return list(tracker.keys())
