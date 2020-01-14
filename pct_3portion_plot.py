def pct_3portion_plot(x, y1, y2, y3, xtext_rotation, fig_height, fig_width, data_label, plt_title, filename, plot_horizontal=False):
    """plot a three-portion percent stacked bar chart
    Keyword arguments:
    x -- array of values for x-axis
    y1 -- array of values for bottom portion
    y2 -- array of values for middle portion
    y3 -- array of values for top portion
    xtext_rotation -- degrees to rotate labels on x axis
    fig_height -- height of figure
    fig_width -- width of figure
    plt_title -- title to use for plot
    filename -- name of file to save plot
    plot_horizontal -- boolean for horizontal/vertical lines, default is vertical
    
    special thanks to https://pythonmatplotlibtips.blogspot.com/2018/11/normalized-stacked-barplot-number-percentage-python-matplotlib.html
    """
 
    # normalize
    snum = y1+y2+y3
    y1 = y1/snum*100.
    y2 = y2/snum*100.
    y3 = y3/snum*100.

    plt.figure(figsize=(fig_width,fig_height))
    plt.title(plt_title, size = text_size)
    plt.xticks(size = text_size, rotation=xtext_rotation)
    plt.yticks(size=text_size)

    if plot_horizontal:
        # create bars
        plt.barh(x, y1, label='Functional', color='green')
        plt.barh(x, y2, left=y1, label='Functional Needs Repaid', color='yellow')
        plt.barh(x, y3, left=y1+y2, label='Non Functional', color='red')

        #reverse xpos & ypos in text setting for horizontal plot
        for xpos, ypos, yval in zip(x, y1/2, y1):
            plt.text(ypos, xpos, "%.1f"%yval + "%", ha="center", va="center", 
                     size = text_size, color = 'white', weight = 'bold')

        ax.invert_yaxis()
        plt.xlabel('Percentage of Pumps', size=text_size)
        plt.ylabel(data_label, size=text_size)
    else:
        # create bars
        plt.bar(x, y1, label='Yes', color='red')
        plt.bar(x, y2, bottom=y1,label='No', color='green')
        plt.bar(x, y3, bottom=y1+y2,label='y3')
        
        # add text annotation corresponding to the percentage of each data.
        for xpos, ypos, yval in zip(x, y1/2, y1):
            plt.text(xpos, ypos, "%.1f"%yval, ha="center", va="center")
        for xpos, ypos, yval in zip(x, y1+y2/2, y2):
            plt.text(xpos, ypos, "%.1f"%yval, ha="center", va="center")
        for xpos, ypos, yval in zip(x, y1+y2+y3/2, y3):
            plt.text(xpos, ypos, "%.1f"%yval, ha="center", va="center")
        # add text annotation corresponding to the "total" value of each bar
        for xpos, ypos, yval in zip(x, y1+y2+y3, snum):
            plt.text(xpos, ypos, "N=%d"%yval, ha="center", va="bottom")

        plt.ylabel('Percentage of Pumps', size=text_size)
        plt.xlabel(data_label, size=text_size)

    plt.savefig(filename, bbox_inches='tight', pad_inches=0.02)
    plt.show()
    