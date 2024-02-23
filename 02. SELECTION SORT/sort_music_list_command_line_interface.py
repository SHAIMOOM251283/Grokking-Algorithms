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

# Input from the user
def get_artists_play_counts_from_user():
    artists_play_counts = []
    num_artists = int(input("Enter the number of artists: "))

    for i in range(1, num_artists + 1):
        artist = input(f"Enter the name of Artist {i}: ")
        play_count = int(input(f"Enter the play count for {artist}: "))
        artists_play_counts.append((artist, play_count))

    return artists_play_counts

# Example usage:
if __name__ == "__main__":
    # Get input from the user
    artists_play_counts = get_artists_play_counts_from_user()

    # Use Bubble Sort to sort the list
    bubble_sort_artists_by_play_count(artists_play_counts)

    # Print the sorted list
    print_sorted_artists(artists_play_counts)
