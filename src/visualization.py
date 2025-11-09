"""
Visualization Module
Reusable plotting functions for EDA.
"""

import matplotlib.pyplot as plt
import seaborn as sns
from windrose import WindroseAxes

def lineplot_timeseries(df, cols, time_col="Timestamp"):
    fig, axes = plt.subplots(len(cols)//2, 2, figsize=(12, 8))
    axes = axes.flatten()
    for i, col in enumerate(cols):
        sns.lineplot(x=time_col, y=col, data=df, ax=axes[i])
        axes[i].set_title(col)
        axes[i].tick_params(axis='x', rotation=45)
    plt.tight_layout()
    plt.show()

def barplot_by_time(df, cols, time_feature, order=None):
    fig, axes = plt.subplots(len(cols)//2, 2, figsize=(12, 8))
    axes = axes.flatten()
    for i, col in enumerate(cols):
        sns.barplot(x=time_feature, y=col, data=df, ax=axes[i], order=order)
        axes[i].set_title(f"{col} by {time_feature}")
        axes[i].tick_params(axis='x', rotation=45)
    plt.tight_layout()
    plt.show()

def correlation_heatmap(df, cols):
    corr = df[cols].corr()
    plt.figure(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()
    return corr

def scatter_plots(df, x_y_pairs):
    n = len(x_y_pairs)
    fig, axes = plt.subplots(1, n, figsize=(5*n, 4))
    if n == 1:
        axes = [axes]
    for ax, (x, y) in zip(axes, x_y_pairs):
        sns.scatterplot(x=x, y=y, data=df, ax=ax)
        ax.set_title(f"{x} vs {y}")
    plt.tight_layout()
    plt.show()

def wind_rose(df, ws_col="WS", wd_col="WD"):
    ax = WindroseAxes.from_ax()
    ax.bar(df[wd_col], df[ws_col], normed=True, opening=0.8, edgecolor='white')
    ax.set_legend(title="Wind Speed (m/s)")
    plt.title("Wind Rose: Wind Speed & Direction")
    plt.show()

def bubble_chart(df, x, y, size_col, color_col):
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x], df[y], s=df[size_col]*2, c=df[color_col],
                cmap='coolwarm', alpha=0.6, edgecolor='k')
    plt.title(f"Bubble Chart: {y} vs {x} (Bubble size = {size_col})")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.colorbar(label=f"{color_col}")
    plt.grid(True)
    plt.show()
