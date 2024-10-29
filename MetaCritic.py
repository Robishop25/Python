# Metacritic Top 100 games of all time



#in command prompt, use 'py mpt.py' to run this

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


from tabulate import tabulate


#create variables

title = 'Title'
score = 'Metascore'
year = 'Release Year'
platform = 'Platform'
genre = 'Genre'
rank = 'Rank'
rated = 'Rated'
e = 'E'
e10 = 'E10+'
t = 'T'
m = 'M'
nintendo = 'Nintendo'
xbox = 'Xbox'
playstation = 'Playstation'


metacritic_ratings = [
  {rank: 1, title: 'The Legend of Zelda: Ocarina of Time', score: 99, platform: nintendo, year: 1998, rated: e},
  {rank: 2, title: 'SoulCalibur', score: 98, platform: xbox, year: 1999, rated: t},
  {rank: 3, title: 'Grand Theft Auto IV', score: 98, platform: playstation, year: 2008, rated: m},
  {rank: 4, title: 'Super Mario Galaxy', score: 97, platform: nintendo, year: 2007, rated: e},
  {rank: 5, title: 'Super Mario Galaxy 2', score: 97, platform: nintendo, year: 2010, rated: e},
  {rank: 6, title: 'The Legend of Zelda: Breath of the Wild', score: 97, platform: nintendo, year: 2017, rated: e10},
  {rank: 7, title: "Tony Hawk's Pro Skater 3", score: 97, platform: playstation, year: 2001, rated: t},
  {rank: 8, title: "Red Dead Redemption 2", score: 97, platform: xbox, year: 2018, rated: m},
  {rank: 9, title: "Grand Theft Auto V", score: 97, platform: xbox, year: 2014, rated: m},
  {rank: 10, title: "Metroid Prime", score: 97, platform: nintendo, year: 2002, rated: t},
  {rank: 11, title: "Grand Theft Auto III", score: 97, platform: playstation, year: 2001, rated: m},
  {rank: 12, title: "Super Mario Odyssey", score: 97, platform: nintendo, year: 2017, rated: e10},
  {rank: 13, title: "Halo: Combat Evolved", score: 97, platform: xbox, year: 2001, rated: m},
  {rank: 14, title: "NFL 2K1", score: 97, platform: playstation, year: 2000, rated: e},
  {rank: 15, title: "Half-Life 2", score: 96, platform: xbox, year: 2004, rated: m},
  {rank: 16, title: "BioShock", score: 96, platform: xbox, year: 2007, rated: m},
  {rank: 17, title: "GoldenEye 007", score: 96, platform: nintendo, year: 1997, rated: t},
  {rank: 18, title: "Uncharted 2: Among Theives", score: 96, platform: playstation, year: 2009, rated: t},
  {rank: 19, title: "Resident Evil 4", score: 96, platform: nintendo, year: 2005, rated: m},
  {rank: 20, title: "Baldur's Gate 3", score: 96, platform: playstation, year: 2023, rated: m},
  {rank: 21, title: "The Orange Box", score: 96, platform: xbox, year: 2007, rated: m},
  {rank: 22, title: "Tekken 3", score: 96, platform: xbox, year: 1998, rated: t},
  {rank: 23, title: "Mass Effect 2", score: 96, platform: xbox, year: 2010, rated: m},
  {rank: 24, title: "The House in Fata Morgana - Dreams of the Revenants Edition", score: 96, platform: nintendo, year: 2021, rated: m},
  {rank: 25, title: "Elden Ring", score: 96, platform: playstation, year: 2022, rated: m},
  {rank: 26, title: "The Elder Scrolls V: Skyrim", score: 96, platform: xbox, year: 2011, rated: m},
  {rank: 27, title: "Half-Life", score: 96, platform: xbox, year: 1998, rated: m},
  {rank: 28, title: "The Legend of Zelda: Tears of the Kingdom", score: 96, platform: nintendo, year: 2023, rated: e10},
  {rank: 29, title: "The Legend of Zelda: Windwaker", score: 96, platform: nintendo, year: 2003, rated: e},
  {rank: 30, title: "Gran Turismo", score: 96, platform: playstation, year: 1998, rated: e},
  {rank: 31, title: "Metal Gear Solid 2: Sons of Liberty", score: 96, platform: playstation, year: 2001, rated: m},
  {rank: 32, title: "Grand Theft Auto Double Pack", score: 96, platform: playstation, year: 2003, rated: m},
  {rank: 33, title: "Portal: Companion Collection", score: 95, platform: nintendo, year: 2022, rated: e},
  {rank: 34, title: "Baldur's Gate II", score: 95, platform: "pc", year: 2000, rated: t},
  {rank: 35, title: "Grand Theft Auto San Andreas", score: 95, platform: playstation, year: 2004, rated: m},
  {rank: 36, title: "Grand Theft Auto Vice City", score: 95, platform: playstation, year: 2002, rated: m},
  {rank: 37, title: "LittleBigPlanet", score: 95, platform: playstation, year: 2008, rated: e},
  {rank: 38, title: "The Legend of Zelda: Collectors Edition", score: 95, platform: nintendo, year: 2003, rated: e},
  {rank: 39, title: "Gran Turismo 3", score: 95, platform: playstation, year: 2001, rated: e},
  {rank: 40, title: "Halo 2", score: 95, platform: xbox, year: 2004, rated: m},
  {rank: 41, title: "The Legend of Zelda: Majora's Mask", score: 95, platform: nintendo, year: 2000, rated: e},
  {rank: 42, title: "The Legend of Zelda: A Link to the Past/Four Swords", score: 95, platform: nintendo, year: 2002, rated: e},
  {rank: 43, title: "The Last of Us", score: 95, platform: nintendo, year: 2013, rated: m},
  {rank: 44, title: "The Legend of Zelda: Twilight Princess", score: 95, platform: nintendo, year: 2006, rated: t},
  {rank: 45, title: "Madden NFL 2003", score: 95, platform: playstation, year: 2003, rated: e},
  {rank: 46, title: "Persona 5 Royal", score: 95, platform: playstation, year: 2020, rated: m},
  {rank: 47, title: "The Las of Us Remastered", score: 95, platform: playstation, year: 2014, rated: m},
  {rank: 48, title: "Red Dead Redemption", score: 95, platform: playstation, year: 2010, rated: m},
  {rank: 49, title: "Portal 2", score: 95, platform: xbox, year: 2011, rated: e10},
  {rank: 50, title: "Final Fantasy IX", score: 94, platform: playstation, year: 2000, rated: t},
  {rank: 51, title: "God of War", score: 94, platform: playstation, year: 2018, rated: m},
  {rank: 52, title: "Tony Hawk's Pro Skater 4", score: 94, platform: playstation, year: 2002, rated: t},
  {rank: 53, title: "Devil May Cry", score: 94, platform: playstation, year: 2001, rated: m},
  {rank: 54, title: "Madden NFL 2002", score: 94, platform: playstation, year: 2002, rated: e},
  {rank: 55, title: "Batmans: Arkham City", score: 94, platform: xbox, year: 2011, rated: t},
  {rank: 56, title: "Metroid Prime", score: 94, platform: nintendo, year: 2023, rated: t},
  {rank: 57, title: "The Legend of Zelda: Ocarina of Time 3D", score: 94, platform: nintendo, year: 2011, rated: t},
  {rank: 58, title: "Chrono Cross", score: 94, platform: playstation, year: 2000, rated: t},
  {rank: 59, title: "Madden NFL 2004", score: 94, platform: playstation, year: 2004, rated: e},
  {rank: 60, title: "Gears of War", score: 94, platform: xbox, year: 2006, rated: m},
  {rank: 61, title: "The Elder Scrolls IV: Oblivion", score: 94, platform: xbox, year: 2006, rated: m},
  {rank: 62, title: "Sid Meiers: Civilization II", score: 94, platform: 'pc', year: 1996, rated: e},
  {rank: 63, title: "Quake", score: 94, platform: 'pc', year: 1996, rated: m},
  {rank: 64, title: "Call of Duty 4: Modern Warfare", score: 94, platform: xbox, year: 2007, rated: m},
  {rank: 65, title: "BioShock Infinite", score: 94, platform: 'pc', year: 2013, rated: m},
  {rank: 66, title: "Halo 3", score: 94, platform: xbox, year: 2007, rated: m},
  {rank: 67, title: "Ninja Gaiden 5", score: 94, platform: xbox, year: 2005, rated: m},
  {rank: 68, title: "Metal Gear Solid", score: 94, platform: playstation, year: 1998, rated: m},
  {rank: 69, title: "Super Mario Bros 3", score: 94, platform: nintendo, year: 2003, rated: e},
  {rank: 70, title: "Grim Fandango", score: 94, platform: 'pc', year: 1998, rated: t},
  {rank: 71, title: "Tom Clancy's Splinter Cell: Chaos Theory", score: 94, platform: xbox, year: 2005, rated: m},
  {rank: 72, title: "God of War: Ragnarok", score: 94, platform: playstation, year: 2022, rated: m},
  {rank: 73, title: "Resident Evil Code: Veronica", score: 94, platform: 'pc', year: 2000, rated: m},
  {rank: 74, title: "Burnout 3", score: 94, platform: xbox, year: 2004, rated: t},
  {rank: 75, title: "Diablo", score: 94, platform: 'pc', year: 1996, rated: m},
  {rank: 76, title: "Metal Gear Solid 3: Substinence", score: 94, platform: playstation, year: 2006, rated: m},
  {rank: 77, title: "Call of Duty: Modern Warfare 2", score: 94, platform: xbox, year: 2009, rated: m},
  {rank: 78, title: "Metal Gear Solid 4: Guns of the Patriots", score: 94, platform: playstation, year: 2008, rated: m},
  {rank: 79, title: "God of War", score: 94, platform: playstation, year: 2005, rated: m},
  {rank: 80, title: "Star Wars: Knights of the Old Republic", score: 94, platform: xbox, year: 2003, rated: t},
  {rank: 81, title: "Side Meier's Civilization IV", score: 94, platform: 'pc', year: 2005, rated: e},
  {rank: 82, title: "Virtua Fighter 4", score: 94, platform: playstation, year: 2002, rated: t},
  {rank: 83, title: "Super Smash Bros Brawl", score: 93, platform: nintendo, year: 2008, rated: t},
  {rank: 84, title: "Company of Heroes", score: 93, platform: 'pc', year: 2006, rated: m},
  {rank: 85, title: "Gran Turismo 2", score: 93, platform: playstation, year: 1999, rated: e},
  {rank: 86, title: "The Last of Us Part II", score: 93, platform: playstation, year: 2020, rated: m},
  {rank: 87, title: "Tom Clancy's Splinter Cell: Pandora Tomorrow", score: 93, platform: xbox, year: 2004, rated: m},
  {rank: 88, title: "Grand Theft Auto: Chinatown Wars", score: 93, platform: nintendo, year: 2009, rated: m},
  {rank: 89, title: "Pac-Man Championship Edition DX", score: 93, platform: xbox, year: 2010, rated: e},
  {rank: 90, title: "Dwarf Fortress", score: 93, platform: 'pc', year: 2006, rated: e},
  {rank: 91, title: "Half-Life: Alyx", score: 93, platform: 'pc', year: 2020, rated: m},
  {rank: 92, title: "Divinity: Original Sin 2", score: 93, platform: 'pc', year: 2017, rated: m},
  {rank: 93, title: "Unreal Tournament 2004", score: 93, platform: 'pc', year:2004, rated: m},
  {rank: 94, title: "Braid", score: 93, platform: xbox, year: 2008, rated: e10},
  {rank: 95, title: "God of War II", score: 93, platform: playstation, year: 2007, rated: m},
  {rank: 96, title: "Super Mario 3D World", score: 93, platform: nintendo, year: 2013, rated: e},
  {rank: 97, title: "Starcraft II: Wings of Liberty", score: 93, platform: 'pc', year: 2010, rated: t},
  {rank: 98, title: "SSX 2000", score: 93, platform: playstation, year: 2000, rated: e},
  {rank: 99, title: "Street Fighter IV", score: 93, platform: xbox, year: 2009, rated: t},
  {rank: 100, title: "Persona 4 Golden", score: 93, platform: playstation, year: 2012, rated: m}
]



# make datafram for all titles
metacritic_ratings_df = pd.DataFrame(metacritic_ratings)
count_all_games = sum(1 for game in metacritic_ratings)
print('')
print('Top', count_all_games, 'best games of all time')
print(metacritic_ratings_df)


# count how many nintendo games
count_nintendo_games = sum(1 for game in metacritic_ratings if game[platform] == nintendo)
print('')
print('Number of Nintendo Games:', count_nintendo_games)
# combine all nintendo scores
sum_nintendo_scores = sum(game[score] for game in metacritic_ratings if game[platform] == nintendo)
# calculate average nintendo score
avg_nintendo_score = round(sum_nintendo_scores/count_nintendo_games, 1)
print('Average Nintendo Score:', avg_nintendo_score)
# make a dataframe of the top 5 nintendo games
# create a list of all nintendo games
all_nintendo_games = [game for game in metacritic_ratings if game[platform] == nintendo]
#filter the list for the top 5 games
top_five_nintendo = all_nintendo_games[:5]
# make dataframe
top_five_nintendo_df = pd.DataFrame(top_five_nintendo)
'''print('')
print('Top Five Nintendo Games of all time')
print(top_five_nintendo_df)'''
# calculate top 5 rank (lower is better)
top_five_nintendo_rank = sum(game[rank] for game in top_five_nintendo)
print('Top 5 Nintendo Games Combined Rank:', top_five_nintendo_rank)


# count how many xbox games
count_xbox_games = sum(1 for game in metacritic_ratings if game[platform] == xbox)
print('')
print('Number of Xbox Games:', count_xbox_games)
# combine all xbox scores
sum_xbox_scores = sum(game[score] for game in metacritic_ratings if game[platform] == xbox)
# calculate average xbox score
avg_xbox_score = round(sum_xbox_scores/count_xbox_games, 1)
print('Average Xbox Score:', avg_xbox_score)
# calculate rank (lower is better)
sum_xbox_rank = sum(game[rank] for game in metacritic_ratings if game[platform] == xbox)
# make a dataframe of the top 5 xbox games
# create a list of all xbox games
all_xbox_games = [game for game in metacritic_ratings if game[platform] == xbox]
#filter the list for the top 5 games
top_five_xbox = all_xbox_games[:5]
# make dataframe
top_five_xbox_df = pd.DataFrame(top_five_xbox)
'''print('')
print('Top Five Xbox Games of all time')
print(top_five_xbox_df)'''
# calculate top 5 rank (lower is better)
top_five_xbox_rank = sum(game[rank] for game in top_five_xbox)
print('Top 5 Xbox Games Combined Rank:', top_five_xbox_rank)



# count how many playstation games
count_ps_games = sum(1 for game in metacritic_ratings if game[platform] == playstation)
print('')
print('Number of Playstation Games:', count_ps_games)
# combine all playstation scores
sum_playstation_scores = sum(game[score] for game in metacritic_ratings if game[platform] == playstation)
# calculate average playstation score
avg_playstation_score = round(sum_playstation_scores/count_ps_games, 1)
print('Average Playstation Score:', avg_playstation_score)
# calculate rank
sum_playstation_rank = sum(game[rank] for game in metacritic_ratings if game[platform] == playstation)
# make a dataframe of the top 5 xbox games
# create a list of all xbox games
all_playstation_games = [game for game in metacritic_ratings if game[platform] == playstation]
#filter the list for the top 5 games
top_five_playstation = all_playstation_games[:5]
# make dataframe
top_five_playstation_df = pd.DataFrame(top_five_playstation)
'''print('')
print('Top Five Playstation Games of all time')
print(top_five_playstation_df)'''
# calculate top 5 rank (lower is better)
top_five_playstation_rank = sum(game[rank] for game in top_five_playstation)
print('Top 5 Playstation Games Combined Rank:', top_five_playstation_rank)





'''
# scatter plot
# Extract scores and platforms from the dataset
scores = [game['Metascore'] for game in metacritic_ratings]
platforms = [game['Platform'] for game in metacritic_ratings]

# Create a scatter plot
plt.figure(figsize=(10, 6)) # Adjust figure size if needed
plt.scatter(platforms, scores, alpha=0.5) # alpha controls the transparency of points

# Add labels and title
plt.xlabel('Platform')
plt.ylabel('Metascore')
plt.title('Metascore by Platform')

# Rotate x-axis labels for better readability if needed
plt.xticks(rotation=45)

# Show plot
plt.grid(True) # Add grid for better visualization
plt.tight_layout() # Adjust layout to prevent clipping of labels
#plt.show()

'''


# another attempt to make scatter plot based on chatgpt suggested code
# DECENTLY SUCCESSFUL SCATTER PLOT BELOW IN PARENTHESES

'''
# Extract scores, ranks, and platforms from the dataset
scores = [game['Metascore'] for game in metacritic_ratings]
ranks = [game['Rank'] for game in metacritic_ratings]
platforms = [game['Platform'] for game in metacritic_ratings]

# Separate scores, ranks, and platforms for each platform
nintendo_scores = [scores[i] for i in range(len(scores)) if platforms[i] == 'Nintendo']
nintendo_ranks = [ranks[i] for i in range(len(ranks)) if platforms[i] == 'Nintendo']
xbox_scores = [scores[i] for i in range(len(scores)) if platforms[i] == 'Xbox']
xbox_ranks = [ranks[i] for i in range(len(ranks)) if platforms[i] == 'Xbox']
playstation_scores = [scores[i] for i in range(len(scores)) if platforms[i] == 'Playstation']
playstation_ranks = [ranks[i] for i in range(len(ranks)) if platforms[i] == 'Playstation']

# Add some jitter to the ranks to make the points less aligned
jittered_nintendo = np.random.uniform(-0.1, 0.1, len(nintendo_ranks))
jittered_xbox = np.random.uniform(-0.1, 0.1, len(xbox_ranks))
jittered_playstation = np.random.uniform(-0.1, 0.1, len(playstation_ranks))

# Create a scatter plot with different colors for each platform
plt.figure(figsize=(10, 6))
plt.scatter(nintendo_ranks, nintendo_scores, color='red', label='Nintendo', alpha=0.5)
plt.scatter(xbox_ranks, xbox_scores, color='green', label='Xbox', alpha=0.5)
plt.scatter(playstation_ranks, playstation_scores, color='blue', label='Playstation', alpha=0.5)

# Add labels and title
plt.xlabel('Rank (Lower is Better)')
plt.ylabel('Metascore')
plt.title('Metascore by Rank and Platform')

# Add legend
plt.legend()

# Show plot
plt.grid(True)
plt.tight_layout()
plt.show()
'''

# CHATGPT ATTEMPT AT LINE CHART
# MEH
'''
# Separate scores, ranks, and platforms for each platform
nintendo_scores = [game['Metascore'] for game in metacritic_ratings if game['Platform'] == 'Nintendo']
nintendo_ranks = [game['Rank'] for game in metacritic_ratings if game['Platform'] == 'Nintendo']
xbox_scores = [game['Metascore'] for game in metacritic_ratings if game['Platform'] == 'Xbox']
xbox_ranks = [game['Rank'] for game in metacritic_ratings if game['Platform'] == 'Xbox']
playstation_scores = [game['Metascore'] for game in metacritic_ratings if game['Platform'] == 'Playstation']
playstation_ranks = [game['Rank'] for game in metacritic_ratings if game['Platform'] == 'Playstation']

# Sort the data by rank for each platform
nintendo_sorted = sorted(zip(nintendo_ranks, nintendo_scores))
xbox_sorted = sorted(zip(xbox_ranks, xbox_scores))
playstation_sorted = sorted(zip(playstation_ranks, playstation_scores))

# Unzip the sorted data
nintendo_ranks_sorted, nintendo_scores_sorted = zip(*nintendo_sorted)
xbox_ranks_sorted, xbox_scores_sorted = zip(*xbox_sorted)
playstation_ranks_sorted, playstation_scores_sorted = zip(*playstation_sorted)

# Create a line chart for each platform
plt.figure(figsize=(10, 6))
plt.plot(nintendo_ranks_sorted, nintendo_scores_sorted, label='Nintendo', color='red')
plt.plot(xbox_ranks_sorted, xbox_scores_sorted, label='Xbox', color='green')
plt.plot(playstation_ranks_sorted, playstation_scores_sorted, label='Playstation', color='blue')

# Add labels and title
plt.xlabel('Rank (Lower is Better)')
plt.ylabel('Metascore')
plt.title('Metascore by Rank and Platform')

# Add legend
plt.legend()

# Show plot
plt.grid(True)
plt.tight_layout()
plt.show()
'''


# Chat gpt bar graph

# EXCELLENT!!!

# Sort the metacritic_ratings by score in descending order
metacritic_ratings_sorted = sorted(metacritic_ratings, key=lambda x: x['Metascore'], reverse=True)

# Separate scores for each platform
nintendo_scores = [game['Metascore'] for game in metacritic_ratings_sorted if game['Platform'] == 'Nintendo']
xbox_scores = [game['Metascore'] for game in metacritic_ratings_sorted if game['Platform'] == 'Xbox']
playstation_scores = [game['Metascore'] for game in metacritic_ratings_sorted if game['Platform'] == 'Playstation']

# Count the number of titles with each score for each platform
nintendo_score_count = {score: nintendo_scores.count(score) for score in nintendo_scores}
xbox_score_count = {score: xbox_scores.count(score) for score in xbox_scores}
playstation_score_count = {score: playstation_scores.count(score) for score in playstation_scores}

# Get unique scores
all_scores = sorted(set(nintendo_scores + xbox_scores + playstation_scores), reverse=True)

# Get counts for each platform for each score
nintendo_counts = [nintendo_score_count.get(score, 0) for score in all_scores]
xbox_counts = [xbox_score_count.get(score, 0) for score in all_scores]
playstation_counts = [playstation_score_count.get(score, 0) for score in all_scores]

# Set the width of the bars
bar_width = 0.25

# Set the positions of the bars on the x-axis
r1 = range(len(all_scores))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(r1, nintendo_counts, color='red', width=bar_width, edgecolor='grey', label='Nintendo')
plt.bar(r2, xbox_counts, color='green', width=bar_width, edgecolor='grey', label='Xbox')
plt.bar(r3, playstation_counts, color='blue', width=bar_width, edgecolor='grey', label='Playstation')

# Add xticks with scores in descending order
plt.xlabel('Score', fontweight='bold')
plt.ylabel('Number of Titles', fontweight='bold')
plt.xticks([r + bar_width for r in range(len(all_scores))], all_scores)

# Add a legend
plt.legend()

# Show plot
plt.title('Number of Titles with Each Score by Platform')
plt.tight_layout()
plt.show()




# print all scores within dataset


# count number of games that have a score of 99
score_99_count = sum(1 for game in metacritic_ratings if game[score] == 99)
#print('') #comment out if printing consoles with score of 99
#print('Total Games with Score of 99:', score_99_count)

# count number of nintendo games that have a score of 99
score_99_count_nintendo = sum(1 for game in metacritic_ratings if game[score] == 99 and game[platform] == nintendo)
print('')
print('Total Games with Score of 99:', score_99_count, 'Nintendo:', score_99_count_nintendo)



# count number of games that have a score of 98
score_98_count = sum(1 for game in metacritic_ratings if game[score] == 98)
#print('')
#print('Total Games with Score of 98:', score_98_count)

# count number of nintendo games that have a score of 98
score_98_count_nintendo = sum(1 for game in metacritic_ratings if game[score] == 98 and game[platform] == nintendo)

# count number of xbox games that have a score of 98
score_98_count_xbox = sum(1 for game in metacritic_ratings if game[score] == 98 and game[platform] == xbox)

# count number of playstation games that have a score of 98
score_98_count_playstation = sum(1 for game in metacritic_ratings if game[score] == 98 and game[platform] == playstation)

print('')
print('Total Games with Score of 98:', score_98_count, 
  'Nintendo:', score_98_count_nintendo,
  'Xbox:', score_98_count_xbox,
  'Playstation:', score_98_count_playstation)


# count nmber of games that have a score of 97
score_97_count = sum(1 for game in metacritic_ratings if game[score] == 97)

# count number of nintendo games that have a score of 97
score_97_count_nintendo = sum(1 for game in metacritic_ratings if game[score] == 97 and game[platform] == nintendo)

# count number of xbox games that have a score of 97
score_97_count_xbox = sum(1 for game in metacritic_ratings if game[score] == 97 and game[platform] == xbox)

# count number of playstation games that have a score of 97
score_97_count_playstation = sum(1 for game in metacritic_ratings if game[score] == 97 and game[platform] == playstation)

print('')
print('Total Games with Score of 97:', score_97_count, 
  'Nintendo:', score_97_count_nintendo,
  'Xbox:', score_97_count_xbox,
  'Playstation:', score_97_count_playstation)




# count nmber of games that have a score of 96
score_96_count = sum(1 for game in metacritic_ratings if game[score] == 96)

# count number of nintendo games that have a score of 96
score_96_count_nintendo = sum(1 for game in metacritic_ratings if game[score] == 96 and game[platform] == nintendo)

# count number of xbox games that have a score of 96
score_96_count_xbox = sum(1 for game in metacritic_ratings if game[score] == 96 and game[platform] == xbox)

# count number of playstation games that have a score of 96
score_96_count_playstation = sum(1 for game in metacritic_ratings if game[score] == 96 and game[platform] == playstation)

print('')
print('Total Games with Score of 96:', score_96_count, 
  'Nintendo:', score_96_count_nintendo,
  'Xbox:', score_96_count_xbox,
  'Playstation:', score_96_count_playstation)



# count nmber of games that have a score of 95
score_95_count = sum(1 for game in metacritic_ratings if game[score] == 95)

# count number of nintendo games that have a score of 95
score_95_count_nintendo = sum(1 for game in metacritic_ratings if game[score] == 95 and game[platform] == nintendo)

# count number of xbox games that have a score of 95
score_95_count_xbox = sum(1 for game in metacritic_ratings if game[score] == 95 and game[platform] == xbox)

# count number of playstation games that have a score of 95
score_95_count_playstation = sum(1 for game in metacritic_ratings if game[score] == 95 and game[platform] == playstation)

print('')
print('Total Games with Score of 95:', score_95_count, 
  'Nintendo:', score_95_count_nintendo,
  'Xbox:', score_95_count_xbox,
  'Playstation:', score_95_count_playstation)



# count nmber of games that have a score of 94
score_94_count = sum(1 for game in metacritic_ratings if game[score] == 94)

# count number of nintendo games that have a score of 94
score_94_count_nintendo = sum(1 for game in metacritic_ratings if game[score] == 94 and game[platform] == nintendo)

# count number of xbox games that have a score of 94
score_94_count_xbox = sum(1 for game in metacritic_ratings if game[score] == 94 and game[platform] == xbox)

# count number of playstation games that have a score of 94
score_94_count_playstation = sum(1 for game in metacritic_ratings if game[score] == 94 and game[platform] == playstation)

print('')
print('Total Games with Score of 94:', score_94_count, 
  'Nintendo:', score_94_count_nintendo,
  'Xbox:', score_94_count_xbox,
  'Playstation:', score_94_count_playstation)

print(tabulate(metacritic_ratings, headers = "keys", tablefmt = "grid"))