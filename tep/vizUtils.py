import pandas as pd
import matplotlib.pyplot as plt
from .utils import discretize

def plot_bars(data, classes, labels, title, normalize=True):
    """
    Plots a discretized distribution of the given data.

    Args:
        data: One-dimensional numpy array
        classes: Interval boundaries for discretization
        labels: Labels for displayed bars
    """
    data = discretize(data, classes)
    df = pd.DataFrame(data=data, columns=['tmp'])
    df = df['tmp'].astype('category')
    counts = df.value_counts(sort=False, normalize=normalize)
    axes = counts.plot(kind='bar', title=title, rot=0)
    axes.set_xticklabels(labels)
    plt.show(axes)
    return
