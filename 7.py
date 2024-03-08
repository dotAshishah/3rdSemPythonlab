# 7. CUSTOMIZING SEABORN PLOTS WITH AESTHETIC

import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
sns.set(style="whitegrid")
sns.scatterplot(x="total_bill", y="tip", style="time", size="size", data=tips)
sns.despine()
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.title("Scatter Plot of Total Bill vs Tip")
plt.show()