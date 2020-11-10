import codecademylib3_seaborn
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Bar Graph: Featured Games

games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]

viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

plt.bar(range(len(games)), viewers, color='red')
plt.title("Viewers on Twitch for Each Game")
plt.legend(["Twitch"])
plt.xlabel("Game")
plt.ylabel("Viewer Count")
ax_bar = plt.subplot()
ax_bar.set_xticks(range(len(games)))
ax_bar.set_xticklabels(games, rotation=30)
plt.show()

# Pie Chart: League of Legends Viewers' Whereabouts
plt.close("all")

labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]

countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]

colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']

explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

plt.pie(countries, explode=explode, colors=colors, shadow=True, startangle=345, autopct='%1.0f%%', pctdistance=1.15)
plt.title("League of Legends Viewers' Whereabouts")
plt.legend(labels, loc="right")
plt.show()

# Line Graph: Time Series Analysis
plt.close("all")

hour = range(24)

viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

plt.plot(hour, viewers_hour)
plt.title("US Viewers for Each Hour")
plt.xlabel("Hour")
plt.ylabel("View Count")
plt.legend(["2015-01-01"])
ax_line = plt.subplot()
ax_line.set_xticks(hour)

y_upper = [y * 1.15 for y in viewers_hour]
y_lower = [y * 0.85 for y in viewers_hour]
plt.fill_between(hour, y_lower, y_upper, alpha=0.2)

plt.show()