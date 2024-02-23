def set_cover(states, stations):
    uncovered_states = set(states)
    chosen_stations = []

    while uncovered_states:
        best_station = None
        max_covered_states = set()

        for station, coverage in stations.items():
            covered_states = coverage & uncovered_states
            if len(covered_states) > len(max_covered_states):
                best_station = station
                max_covered_states = covered_states

        if best_station is None:
            break

        chosen_stations.append(best_station)
        uncovered_states -= max_covered_states

    return chosen_stations

# Example usage
if __name__ == "__main__":
    states = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
    stations = {
        "kone": {"id", "nv", "ut"},
        "ktwo": {"wa", "id", "mt"},
        "kthree": {"or", "nv", "ca"},
        "kfour": {"nv", "ut"},
        "kfive": {"ca", "az"}
    }

    chosen_stations = set_cover(states, stations)
    print("Chosen stations:", chosen_stations)
