# Model Card for VibeFinder 1.0

## Model Name
VibeFinder 1.0

## Goal / Task
Predicts and recommends songs that match a user's musical taste profile based on genre, mood, energy, and tempo preferences.

## Data Used
Dataset of 18 songs with features: title, artist, genre, mood, energy (0.0-1.0), tempo_bpm. Limited diversity in genres, mostly Pop.

## Algorithm Summary
Scores songs by adding points for genre match (+2.0), mood match (+1.0), and similarity scores for energy and tempo (1.0 - normalized difference). Ranks top songs by total score.

## Observed Behavior / Biases
The system over-prioritizes genre matches, leading to filter bubbles where users only get recommendations from their preferred genre, even if other songs match energy or mood better. With limited dataset, recommendations lack variety.

## Evaluation Process
Tested with three profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock. Ran experiments changing weights to see sensitivity. Compared outputs to musical intuition.

## Intended Use and Non-Intended Use
Intended for simple music discovery simulations. Not for production use or real recommendations without more data and advanced algorithms.

## Ideas for Improvement
Add more songs for diversity. Implement collaborative filtering. Use machine learning for better scoring. Add user feedback loop.

## Limitations and Bias
The dataset is small and biased towards Pop music (10/18 songs), causing Pop songs to dominate recommendations. Numerical features like energy are simplistic and may not capture complex musical vibes.

## Evaluation
For High-Energy Pop: Recommendations focused on high-energy Pop songs, accurate but limited by genre bias.
For Chill Lofi: Preferred low-energy songs, but genre match boosted Indie over better energy matches.
For Rock: Only one Rock song, so it always tops, showing dataset limitation.

## Personal Reflection
Biggest learning: Simple rules can simulate recommendations but reveal biases quickly.
AI tools helped generate code and ideas, but I verified logic manually.
Surprised by how genre weight dominated rankings.
Next: Add more features like danceability, integrate user ratings.