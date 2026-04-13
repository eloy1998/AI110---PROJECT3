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

### High-Energy Pop Profile
Permission to Dance by BTS - Score: 4.67
Reasons: genre match (+2.0), mood match (+1.0), energy similarity (0.90), tempo similarity (0.78)

Good 4 U by Olivia Rodrigo - Score: 4.00
Reasons: genre match (+2.0), energy similarity (1.00), tempo similarity (1.00)

Montero (Call Me By Your Name) by Lil Nas X - Score: 3.85
Reasons: genre match (+2.0), energy similarity (0.90), tempo similarity (0.95)

Happy by Pharrell Williams - Score: 3.85
Reasons: genre match (+2.0), energy similarity (0.90), tempo similarity (0.95)

Blinding Lights by The Weeknd - Score: 3.79
Reasons: genre match (+2.0), energy similarity (0.80), tempo similarity (0.99)

### Chill Lofi Profile
Skinny Love by Bon Iver - Score: 3.88
Reasons: genre match (+2.0), energy similarity (0.90), tempo similarity (0.98)

What a Wonderful World by Louis Armstrong - Score: 2.96
Reasons: mood match (+1.0), energy similarity (1.00), tempo similarity (0.96)

Take Me Home Country Roads by John Denver - Score: 1.71
Reasons: energy similarity (0.80), tempo similarity (0.91)

Moonlight Sonata by Beethoven - Score: 1.70
Reasons: energy similarity (0.90), tempo similarity (0.80)

Drivers License by Olivia Rodrigo - Score: 1.68
Reasons: energy similarity (0.90), tempo similarity (0.78)

### Deep Intense Rock Profile
Bohemian Rhapsody by Queen - Score: 4.56
Reasons: genre match (+2.0), mood match (+1.0), energy similarity (0.90), tempo similarity (0.66)

Old Town Road by Lil Nas X - Score: 1.98
Reasons: energy similarity (1.00), tempo similarity (0.98)

Permission to Dance by BTS - Score: 1.93
Reasons: energy similarity (1.00), tempo similarity (0.93)

Happy by Pharrell Williams - Score: 1.90
Reasons: energy similarity (1.00), tempo similarity (0.90)

Butter by BTS - Score: 1.85
Reasons: energy similarity (1.00), tempo similarity (0.85)