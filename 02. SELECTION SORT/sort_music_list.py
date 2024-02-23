def bubble_sort_artists_by_play_count(artists):
    n = len(artists)

    for i in range(n):
        for j in range(0, n-i-1):
            # Compare adjacent play counts and swap if needed
            if artists[j][1] < artists[j+1][1]:
                artists[j], artists[j+1] = artists[j+1], artists[j]

def print_sorted_artists(artists):
    print("Rank\tArtist\t\tPlay Count")
    print("-" * 30)
    for rank, (artist, play_count) in enumerate(artists, start=1):
        print(f"{rank}\t{artist}\t\t{play_count}")

# Example usage:
if __name__ == "__main__":
    artists_play_counts = [
        ("Artist1", 150),
        ("Artist2", 300),
        ("Artist3", 200),
        ("Artist4", 100),
    ]

    # Use Bubble Sort to sort the list
    bubble_sort_artists_by_play_count(artists_play_counts)

    # Print the sorted list
    print_sorted_artists(artists_play_counts)
