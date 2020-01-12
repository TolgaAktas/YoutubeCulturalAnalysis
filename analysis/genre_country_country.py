import numpy as np

genre_CA_vector = np.load('obj_genre_CA.npy').flatten()
genre_US_vector = np.load('obj_genre_US.npy').flatten()
genre_DE_vector = np.load('obj_genre_DE.npy').flatten()
genre_FR_vector = np.load('obj_genre_FR.npy').flatten()
genre_JP_vector = np.load('obj_genre_JP.npy').flatten()
genre_KR_vector = np.load('obj_genre_KR.npy').flatten()
genre_MX_vector = np.load('obj_genre_MX.npy').flatten()
genre_RU_vector = np.load('obj_genre_RU.npy').flatten()
genre_IN_vector = np.load('obj_genre_IN.npy').flatten()
genre_GB_vector = np.load('obj_genre_GB.npy').flatten()

vectors = [genre_GB_vector, genre_US_vector, genre_CA_vector, genre_DE_vector, genre_MX_vector,
           genre_RU_vector, genre_FR_vector, genre_IN_vector, genre_JP_vector, genre_KR_vector]

cos = np.zeros((10,10))
for i, vec1 in enumerate(vectors):
    for j, vec2 in enumerate(vectors):
        dot = np.dot(vec1, vec2)
        norma = np.linalg.norm(vec1)
        normb = np.linalg.norm(vec2)
        cos[i,j] = dot / (norma * normb)

countries = ['GB', 'US', 'CA', 'DE', 'MX', 'RU', 'FR', 'IN', 'JP', 'KR'] # looking at correlations between these countries
import matplotlib.pyplot as plt
from matplotlib import cm
fig, ax = plt.subplots(figsize=(15,15))
# fig.suptitle('Cosine Similarity of Genre between Countries', fontsize=20).set_y(0.85)
heatmap = ax.imshow(cos, interpolation='nearest', cmap=cm.OrRd)

# making the colorbar on the side
cbar_min = cos.min().min()
cbar_max = cos.max().max()
cbar = fig.colorbar(heatmap, ticks=[cbar_min, cbar_max])

#print labels
ax.set_yticks(np.arange(len(countries)))
ax.set_xticks(np.arange(len(countries)))
ax.set_yticklabels(countries, fontsize=20)
ax.set_xticklabels(countries, fontsize=20)
cbar.ax.tick_params(labelsize=20)
plt.savefig('figures/genre_similarity.pdf')
np.save('genre_country_country_dist', cos)