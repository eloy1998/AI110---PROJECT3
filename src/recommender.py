import csv

def load_songs(file_path):
    """Load songs from a CSV file and return a list of dictionaries."""
    songs = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert numerical values
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = int(row['tempo_bpm'])
            songs.append(row)
    return songs

def score_song(user_prefs, song):
    """Score a song based on user preferences and return score with reasons."""
    score = 0.0
    reasons = []

    # Genre match
    if song['genre'] == user_prefs['favorite_genre']:
        score += 2.0
        reasons.append("genre match (+2.0)")

    # Mood match
    if song['mood'] == user_prefs['favorite_mood']:
        score += 1.0
        reasons.append("mood match (+1.0)")

    # Energy similarity
    energy_diff = abs(song['energy'] - user_prefs['target_energy'])
    energy_score = 1.0 - energy_diff
    score += energy_score
    reasons.append(f"energy similarity ({energy_score:.2f})")

    # Tempo similarity
    tempo_diff = abs(song['tempo_bpm'] - user_prefs['target_tempo'])
    tempo_score = 1.0 - (tempo_diff / 200.0)  # Normalize, assuming max diff 200
    score += tempo_score
    reasons.append(f"tempo similarity ({tempo_score:.2f})")

    return score, reasons

def recommend_songs(user_prefs, songs, k=5):
    """Recommend top k songs based on user preferences."""
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored_songs.append((song, score, reasons))

    # Sort by score descending
    scored_songs.sort(key=lambda x: x[1], reverse=True)

    return scored_songs[:k]