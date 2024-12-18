import matplotlib.pyplot as plt


def create_pie(labels, data, title):
    sizes = [30, 20, 15, 10, 25]
    colours = ['#FF7F3E', '#219B9D', '#99ff99', '#80C4E9', '#86D293', '#ffcc99', '#c2c2f0']
    explode = (0.1, 0, 0, 0, 0)

    fig, ax = plt.subplots()  # Create a new figure and axis for each pie chart
    ax.pie(data, labels=labels, autopct='%1.1f%%', colors=colours, labeldistance=1.1)
    ax.set_title(title)
    ax.legend(labels, title="Categories", loc='center left', bbox_to_anchor=(1, 0.5))
    return fig  # Return the figure object to embed into Tkinter
