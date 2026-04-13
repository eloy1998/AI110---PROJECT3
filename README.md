# AI110---PROJECT3

## How The System Works

Real-world recommendations work by analyzing user behavior and song attributes. Collaborative filtering uses patterns from similar users, while content-based filtering matches song features to user preferences. My version prioritizes content-based filtering using genre, mood, energy, and tempo.

Song objects will use: title, artist, genre, mood, energy, tempo_bpm.

UserProfile will use: favorite_genre, favorite_mood, target_energy, target_tempo.

Algorithm Recipe:
- +2.0 points for genre match
- +1.0 point for mood match
- Energy score: 1.0 - abs(song_energy - user_energy)
- Tempo score: 1.0 - abs(song_tempo - user_tempo) / 200 (normalize)

Potential biases: This system might over-prioritize genre, ignoring great songs that match the user's mood or energy.

## Terminal Output

Loaded songs: 18

Top Recommendations:
Happy by Pharrell Williams - Score: 5.00
Reasons: genre match (+2.0), mood match (+1.0), energy similarity (1.00), tempo similarity (1.00)

Butter by BTS - Score: 4.75
Reasons: genre match (+2.0), mood match (+1.0), energy similarity (1.00), tempo similarity (0.75)

Montero (Call Me By Your Name) by Lil Nas X - Score: 3.91
Reasons: genre match (+2.0), energy similarity (1.00), tempo similarity (0.91)

Good 4 U by Olivia Rodrigo - Score: 3.85
Reasons: genre match (+2.0), energy similarity (0.90), tempo similarity (0.95)

Blinding Lights by The Weeknd - Score: 3.84
Reasons: genre match (+2.0), energy similarity (0.90), tempo similarity (0.94)