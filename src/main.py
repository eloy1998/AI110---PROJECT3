from recommender import load_songs, recommend_songs

def main():
    # Load songs
    songs = load_songs('/workspaces/AI110---PROJECT3/data/songs.csv')
    print(f"Loaded songs: {len(songs)}")

    # Default user profile
    user_prefs = {
        'favorite_genre': 'Pop',
        'favorite_mood': 'Happy',
        'target_energy': 0.8,
        'target_tempo': 160
    }

    # Get recommendations
    recommendations = recommend_songs(user_prefs, songs, k=5)

    # Print recommendations
    print("\nTop Recommendations:")
    for song, score, reasons in recommendations:
        print(f"{song['title']} by {song['artist']} - Score: {score:.2f}")
        print(f"Reasons: {', '.join(reasons)}")
        print()

if __name__ == "__main__":
    main()