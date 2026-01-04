import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def compute_gini(model):
    """Mathematical implementation of the Gini Coefficient for inequality analysis."""
    agent_wealths = [agent.wealth for agent in model.schedule.agents]
    x = sorted(agent_wealths)
    N = model.num_agents
    total = sum(x)
    if N == 0 or total == 0:
        return 0.0
    # Gini Formula: 1 + (1/N) - 2*B
    B = sum((i + 1) * xi for i, xi in enumerate(x)) / (N * total)
    return 1 + (1 / N) - 2 * B

def plot_heatmap(model):
    """Visualizes agent density across the grid."""
    agent_counts = np.zeros((model.grid.width, model.grid.height))
    for cell_content, x, y in model.grid.coord_iter():
        agent_counts[x][y] = len(cell_content)
    
    plt.figure(figsize=(6,6))
    sns.heatmap(agent_counts, cmap="viridis", annot=True, cbar=False, square=True)
    plt.title("Spatial Distribution of Agents")
    plt.show()
