import pylab as pl
import numpy as np
from data import load_responses

songs, responses = load_responses()

# Print table of median values
mean_vectors = dict([(s, np.median(r, axis=0)) for s, r in responses.items()])
for s, v in mean_vectors.items():
    print "%s\t%s" % (s.split('/')[2].split('.')[0], '\t'.join(str(val) for val in v))

# Plot mean values
fig1 = pl.figure(1)

track = mean_vectors['wav/mix-short/wham-mix.wav']

plot1 = fig1.add_subplot(121)
plot1.bar(range(0,5), track, 0.2)
plot1.ylabel = ('Procent %')
labels = ('Pop', 'Rock', 'Reggae', 'Jazz', 'Klassiskt')
pl.xticks(range(0,5), labels, rotation=20)
pl.ylim([0,100])
pl.xlim([-.5,5])
pl.title('Wham - Medel')

# Plot boxplot and whiskers
track = responses['wav/mix-short/wham-mix.wav']
pop = [r[0] for r in track]
rock = [r[1] for r in track]
reggae = [r[2] for r in track]
jazz = [r[3] for r in track]
classical = [r[4] for r in track]
plot_data = [pop, rock, reggae, jazz, classical]

plot2 = fig1.add_subplot(122)
plot2.boxplot(plot_data)
pl.ylabel = ('Procent %')
labels = ('Pop', 'Rock', 'Reggae', 'Jazz', 'Klassiskt')
pl.xticks(range(1,6), labels, rotation=20)
pl.title('Wham - Boxplot')

# Show plots
pl.show()
