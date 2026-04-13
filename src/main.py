from recommender import load_songs, recommend_songs

def main():
    # Load songs
    songs = load_songs('/workspaces/AI110---PROJECT3/data/songs.csv')
    print(f"Loaded songs: {len(songs)}")

    # Define profiles
    profiles = {
        "High-Energy Pop": {
            'favorite_genre': 'Pop',
            'favorite_mood': 'Energetic',
            'target_energy': 0.9,
            'target_tempo': 170
        },
        "Chill Lofi": {
            'favorite_genre': 'Indie',
            'favorite_mood': 'Calm',
            'target_energy': 0.3,
            'target_tempo': 100
        },
        "Deep Intense Rock": {
            'favorite_genre': 'Rock',
            'favorite_mood': 'Dramatic',
            'target_energy': 0.8,
            'target_tempo': 140
        }
    }

    for profile_name, user_prefs in profiles.items():
        print(f"\n--- {profile_name} Profile ---")
        # Get recommendations
        recommendations = recommend_songs(user_prefs, songs, k=5)

        # Print recommendations
        for song, score, reasons in recommendations:
            print(f"{song['title']} by {song['artist']} - Score: {score:.2f}")
            print(f"Reasons: {', '.join(reasons)}")

if __name__ == "__main__":
    main()