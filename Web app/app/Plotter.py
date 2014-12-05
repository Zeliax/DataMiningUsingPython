# -*- coding: utf-8 -*-
"""Modules used to plot pie chart and histogram regarding sentiment."""
import matplotlib.pylab as plt
import matplotlib
import mpld3


def pie_chart(sentiment_list, rating_list, unknown_nr):
    """Plotting two piecharts of input.

    Keyword arguments:
    fractions_list -> list of two components; positive and negative counts.
    rating_list -> list of two components; likes and dislikes.
    unknown_nr -> comment amount that have not been given a sentiment score.
    """
    #Calculate differences in sentiment and likes/dislikes
    sent_pos_amount = sentiment_list[0]
    sent_neg_amount = sentiment_list[1]
    total_sent = sent_neg_amount + sent_pos_amount + unknown_nr
    rate_pos_amount = rating_list[0]
    rate_neg_amount = rating_list[1]
    total_rate = rate_neg_amount + rate_pos_amount

    labels = ['Positive', 'Negative']
    colors = ['#4CAF50', '#F44336']

    matplotlib.rcParams['text.color'] = '#263238'
    matplotlib.rcParams['lines.linewidth'] = 2
    matplotlib.rcParams['patch.edgecolor'] = 'white'
    matplotlib.rcParams['font.style'] = 'oblique'
    matplotlib.rcParams['font.size'] = 13

    fig = plt.figure(figsize=[6, 6])

    ax1 = fig.add_subplot(1, 2, 1)
    if sentiment_list == [0, 0]:
        ax1.text(0.1, 0.5,
                 'There is no plot to display',
                 fontsize=16,
                 color='#263238')
    else:
        nr_of_unknown_string = str(unknown_nr) + ' unknown comments'
        total_sent_string = str(total_sent) + ' total comments'
        _, texts, _ = ax1.pie(sentiment_list,
                              labels=labels,
                              autopct='%1.1f%%',
                              colors=colors)
        ax1.axis('equal')
        texts[0].set_fontsize(0)
        texts[1].set_fontsize(0)
        ax1.set_title('Sentiment Score')
        ax1.set_axis_off()
        ax1.legend()
        ax1.text(-0.8, -1.8,
                 nr_of_unknown_string,
                 fontsize=14,
                 color='#263238')
        ax1.text(-0.8, -2.0,
                 total_sent_string,
                 fontsize=14,
                 color='#263238')

    ax2 = fig.add_subplot(1, 2, 2)
    if rating_list == [0, 0]:
        ax2.text(0.1, 0.5,
                 'There is no plot to display',
                 fontsize=16,
                 color='#263238')
    else:
        _, texts, _ = ax2.pie(rating_list,
                              labels=labels,
                              autopct='%1.1f%%',
                              colors=colors)
        total_rate_string = str(total_rate) + ' total ratings'
        ax2.axis('equal')
        texts[0].set_fontsize(0)
        texts[1].set_fontsize(0)
        ax2.set_title('Likes/Dislikes')
        ax2.set_axis_off()
        ax2.legend()
        ax2.text(-0.8, -2.0,
                 total_rate_string,
                 fontsize=14,
                 color='#263238')

    fig.tight_layout()

    return fig


def hist_graph(sentiment_list, bins, unknown_nr):
    """Method for plotting a historgraph of input.

    Keyword arguments:
    sentiment_list -> list of sentiment scores; scores.
    bins -> bins to fit the sentiment scores in
    unknown_nr -> comment amount that have not been given a sentiment score.
    """
    unknown_list = [(number + 12) for number in unknown_nr]
    sentiment_list.extend(unknown_list)

    matplotlib.rcParams['text.color'] = '#263238'
    matplotlib.rcParams['lines.linewidth'] = 2
    matplotlib.rcParams['patch.edgecolor'] = 'white'
    matplotlib.rcParams['font.style'] = 'oblique'
    matplotlib.rcParams['font.size'] = 13

    fig = plt.figure(figsize=[6, 6])

    subfig = fig.add_subplot(1, 1, 1)
    subfig.set_title('Histogram displaying Sentiment Bins')
    subfig.set_xlabel('Bins')
    subfig.set_ylabel('Comment Count')
    subfig.set_xticks(bins[:-1])

    if sentiment_list == []:
        subfig.text(3, 0.5,
                    'There is no plot to display',
                    fontsize=20,
                    color='#263238')
    else:
        _, bins, patches = subfig.hist(sentiment_list,
                                       bins=bins,
                                       normed=1,
                                       histtype='bar',
                                       rwidth=0.6,
                                       stacked=True,
                                       align='left')

        for bin_, patch in zip(bins, patches):
            if bin_ > 5 and bin_ < 11:
                patch.set_facecolor('#4CAF50')
                patch.set_label('Positive')
            elif bin_ < 5:
                patch.set_facecolor('#F44336')
                patch.set_label('Negative')
            elif bin_ >= 5 and bin_ < 6:
                patch.set_facecolor('#FFC107')
                patch.set_label('Neutral')
            elif bin_ == 11:
                patch.set_facecolor('#9E9E9E')
                patch.set_label('Unknown')

    fig.tight_layout()

    return fig


def generate_pie_plots(sentiment_list, rating_list, unknown_list):
    """Given list of sentiments and a list of ratings, generate pie charts.

    sentiment_list -> list of amount positive/negative comments.
    rating_list -> list of amount likes/dislikes.
    unknown_list -> list of number of un-analysed comments.
    """
    plot_list = []
    for sentiment, rating, unknown in zip(sentiment_list, rating_list,
                                          unknown_list):
        fig = pie_chart(sentiment, rating, unknown)
        plot_list.append(mpld3.fig_to_html(fig))
    return plot_list


def genereate_hist_plots(sentiment_list, bins, unknown_list):
    """Given a sentiment list, bin and unknown count list, generate plots.

    sentiment_list -> list of amount positive/negative comments
    bins -> bins to fit the sentiment scores in
    unknown_list -> list of amount that have not been given a sentiment score.
    """
    plot_list = []
    for sentiment, unknown in zip(sentiment_list, unknown_list):
        fig = hist_graph(sentiment, bins, unknown)
        plot_list.append(mpld3.fig_to_html(fig))
    return plot_list


def list_divider(nested_list, unknown_list):
    """The inputs are mapped based on sub-functions."""
    def unknown_list_counter(unknown_list):
        """Count the amount of unknown sentiment scores."""
        return len([unknown for unknown in unknown_list])

    def pos_neg_counter(sentiment_list):
        """Count the positive/negative comments in a list."""
        positive = len([sent for sent in sentiment_list if sent > 5])
        negative = len([sent for sent in sentiment_list if sent <= 5])
        return [positive, negative]

    pos_neg_count = map(pos_neg_counter, nested_list)
    unknown_count = map(unknown_list_counter, unknown_list)
    return pos_neg_count, unknown_count
