import seaborn as sns
import matplotlib.pyplot as plt
data=[27,45,36,18,72,81,108,19,91]
df=pd.DataFrame(data,columns=["Values"])
sns.histplot(df["Values"],kde=True)
plt.title("Data Distribution")
plt.show()