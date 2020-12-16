# my solution


def can_two_movies_fill_flight(movie_lengths, flight_length):

    # Determine if two movie runtimes add up to the flight length

    m_dict = dict()

    for i in range(len(movie_lengths)):

        if movie_lengths[i] not in m_dict:

            m_dict[movie_lengths[i]] = list()

        m_dict[movie_lengths[i]].append(i)

    for key in m_dict:

        target = max(flight_length, key) - min(flight_length, key)

        if target in m_dict:

            if target == key:

                if len(m_dict[target]) > 1:

                    return True

            else:

                return True

    return False
