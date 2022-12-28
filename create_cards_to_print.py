import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

paths_mots_courts_facile = 'data/Devine Mots courts - Niv.1 - Facile.csv'
mots_courts_facile = pd.read_csv(paths_mots_courts_facile, sep=';')

# print(mots_courts_facile.head())

for i, word in enumerate(mots_courts_facile['lemme']):
    if i > 100:  # si on veut les 100 premiers mots
        break

    # if word != 'fille':  # si on veut tester un mot unique
    #     continue

    # Découpage de la définition pour qu'elle ne déborde pas de la figure
    def_1 = mots_courts_facile['def_1'].iloc[i]
    line = ''
    def_to_print = ''
    count = 0
    last_num_car = 0
    nb_words_per_line = 7
    # print("Def_1 avant : ", def_1)
    for num_car, car in enumerate(def_1):
        if car == ' ':
            count += 1
            # print(f"Count : {count} - Car : {car} - Num_car Cond1 :  {num_car}")

        if count == nb_words_per_line and car == ' ':
            # print(f"Count : {count} - Car : {car} - Num_car Cond2 :  {num_car}")
            count = 0
            line = def_1[last_num_car:num_car]
            line = line + '\n'
            def_to_print = def_to_print + line
            last_num_car = num_car
            # print("Last_num_car Cond2 : ", last_num_car)
            # print("Line : ", line)
            # print("def_to_print : ", def_to_print)
        if num_car == len(def_1) - 1 and count < nb_words_per_line:
            line = def_1[last_num_car:len(def_1)]
            def_to_print = def_to_print + line
            # print("Line : ", line)
            # print("def_to_print : ", def_to_print)
    # print("Def_1 après : ", def_to_print)

    fig = plt.figure(figsize=(24, 4))
    gs = matplotlib.gridspec.GridSpec(1, 5,
                                      height_ratios=[1], width_ratios=[1, 1, 1, 3, 3],
                                      left=0, right=1, bottom=0, top=1,
                                      hspace=0, wspace=0)

    ax1 = plt.subplot(gs[0], facecolor='tomato')
    ax2 = plt.subplot(gs[1], facecolor='darkorange')
    ax3 = plt.subplot(gs[2], facecolor='orange')
    ax4 = plt.subplot(gs[3], facecolor='gold')
    ax5 = plt.subplot(gs[4], facecolor='yellow')

    ax1.text(1, 1, word, fontsize=20, color='black', family='serif',
             verticalalignment='center', horizontalalignment='center',
             bbox={'boxstyle': 'round',
                   'facecolor': (1, 0.2, 0),
                   'pad': 0.5}
             )
    ax2.text(1, 1, mots_courts_facile['anagramme'].iloc[i], fontsize=20, color='black', family='serif',
             verticalalignment='center', horizontalalignment='center',
             bbox={'boxstyle': 'round',
                   'facecolor': (1, 0.4, 0),
                   'pad': 0.5}
             )
    ax3.text(1, 1.2, mots_courts_facile['nb_lettres'].iloc[i], fontsize=20, color='black', family='serif',
             verticalalignment='center', horizontalalignment='center',
             bbox={'boxstyle': 'round',
                   'facecolor': (1, 0.6, 0),
                   'pad': 0.5}
             )
    ax3.text(1, 0.8, mots_courts_facile['nb_lettres2'].iloc[i], fontsize=20, color='black', family='serif',
             verticalalignment='center', horizontalalignment='center',
             bbox={'boxstyle': 'round',
                   'facecolor': (1, 0.6, 0),
                   'pad': 0.5}
             )
    ax4.text(0.7, 1, mots_courts_facile['syn_1'].iloc[i], fontsize=20, color='black', family='serif',
             verticalalignment='center', horizontalalignment='center',
             bbox={'boxstyle': 'round',
                   'facecolor': (1, 0.8, 0),
                   'pad': 0.5}
             )
    ax4.text(2, 1, mots_courts_facile['syn_2'].iloc[i], fontsize=20, color='black', family='serif',
             verticalalignment='center', horizontalalignment='center',
             bbox={'boxstyle': 'round',
                   'facecolor': (1, 0.8, 0),
                   'pad': 0.5}
             )
    ax4.text(3.3, 1, mots_courts_facile['syn_3'].iloc[i], fontsize=20, color='black', family='serif',
             verticalalignment='center', horizontalalignment='center',
             bbox={'boxstyle': 'round',
                   'facecolor': (1, 0.8, 0),
                   'pad': 0.5}
             )
    ax4.text(2, 1.5, mots_courts_facile['syn_4'].iloc[i], fontsize=20, color='black', family='serif',
             verticalalignment='center', horizontalalignment='center',
             bbox={'boxstyle': 'round',
                   'facecolor': (1, 0.8, 0),
                   'pad': 0.5}
             )
    ax4.text(2, 0.5, mots_courts_facile['syn_5'].iloc[i], fontsize=20, color='black',  family='serif',
             verticalalignment='center', horizontalalignment='center',
             bbox={'boxstyle': 'round',
                   'facecolor': (1, 0.8, 0),
                   'pad': 0.5}
             )
    ax5.text(1, 1, def_to_print, fontsize=20, color='black', family='serif', wrap=True,
             verticalalignment='center', horizontalalignment='center',
             bbox={'boxstyle': 'round',
                   'facecolor': (1, 0.9, 0.5),
                   'pad': 0.5}
             )
    ax1.set_xlim(0, 2)
    ax1.set_ylim(0, 2)
    ax2.set_xlim(0, 2)
    ax2.set_ylim(0, 2)
    ax3.set_xlim(0, 2)
    ax3.set_ylim(0, 2)
    ax4.set_xlim(0, 4)
    ax4.set_ylim(0, 2)
    ax5.set_xlim(0, 2)
    ax5.set_ylim(0, 2)
    ax1.axis('off')
    ax2.axis('off')
    ax3.axis('off')
    ax4.axis('off')
    ax5.axis('off')

    file_name = f"data/cartes/{word}_carte.png"
    print(file_name)
    print("#######################################################################################################")
    plt.savefig(file_name)
    plt.close(fig)

