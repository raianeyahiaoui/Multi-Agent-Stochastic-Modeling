from src.model import MoneyModel
from src.analysis import plot_heatmap

# Run a sample simulation
model = MoneyModel(N=50, width=10, height=10)
for i in range(100):
    model.step()

print(f"Simulation Complete. Final Gini Coefficient: {model.datacollector.get_model_vars_dataframe()['Gini'].iloc[-1]}")
plot_heatmap(model)
