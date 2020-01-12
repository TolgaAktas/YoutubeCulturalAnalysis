countries = ['GB', 'US', 'CA', 'DE', 'MX', 'RU', 'FR', 'IN', 'JP', 'KR'] # looking at correlations between these countries
category_titles = ['Film & Animation', 'Autos & Vehicles', 'Music', 'Pets & Animals', 'Sports', 'Short Movies', 'Travel & Events',
                   'Gaming', 'Videoblogging', 'People & Blogs', 'Comedy', 'Entertainment', 'News & Politics', 'Howto & Style',
                   'Education', 'Science & Technology', 'Movies', 'Anime/Animation', 'Action/Adventure', 'Classics', 'Comedy',
                   'Documentary', 'Drama', 'Family', 'Foreign', 'Horror', 'Sci-Fi/Fantasy', 'Thriller', 'Shorts', 'Shows', 'Trailers']

import numpy as np
counts = np.array([
    [174, 12, 830, 39, 198, 0, 10, 157, 0, 233, 158, 746, 111, 185, 34, 38, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [303, 58, 764, 138, 402, 0, 57, 94, 0, 445, 495, 1461, 474, 581, 241, 365, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0],
    [945, 223, 1311, 205, 1339, 0, 188, 715, 0, 1613, 1670, 7050, 2146, 1253, 538, 590, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 115, 0],
    [1203, 574, 1110, 180, 1307, 0, 103, 956, 0, 2882, 1513, 8946, 1632, 1313, 521, 604, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 111, 1],
    [714, 199, 1739, 49, 1570, 0, 72, 611, 0, 3158, 998, 6926, 1665, 1984, 381, 349, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
    [1580, 1244, 1085, 447, 978, 0, 216, 721, 0, 5824, 1777, 3983, 3108, 1727, 431, 844, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 160, 0],
    [1122, 496, 1894, 166, 2104, 0, 74, 907, 0, 2179, 2157, 5983, 1854, 1772, 506, 478, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 101, 1],
    [404, 29, 1147, 1, 243, 0, 3, 19, 0, 771, 1044, 5572, 2076, 399, 609, 282, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 121, 0],
    [282, 161, 636, 679, 640, 0, 59, 433, 0, 774, 263, 2337, 354, 461, 45, 71, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [434, 26, 588, 231, 185, 0, 20, 494, 0, 1532, 639, 2448, 1934, 216, 136, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 69, 1],
])

import matplotlib.pyplot as plt
from matplotlib import cm

fig, ax = plt.subplots(figsize=(16, 7))
heatmap = ax.imshow(counts, interpolation='nearest', cmap=cm.OrRd)

# making the colorbar on the side
cbar_min = counts.min().min()
cbar_max = counts.max().max()
cbar = fig.colorbar(heatmap, ticks=[cbar_min, cbar_max])

# print labels
ax.set_yticks(np.arange(len(countries)))
ax.set_xticks(np.arange(len(category_titles)))
ax.set_yticklabels(countries, fontsize=15)
ax.set_xticklabels(category_titles, fontsize=15, rotation=90)
cbar.ax.tick_params(labelsize=15)
plt.savefig('figures/genre_counts.pdf')
