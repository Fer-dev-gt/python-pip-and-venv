import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['Python', 'C++', 'Ruby', 'Java']
    values = [90, 80, 75, 95]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()