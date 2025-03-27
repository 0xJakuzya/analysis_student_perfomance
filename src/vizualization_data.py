import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from parser_csv import ParserStudents

parser_data = ParserStudents('data/students_performance.csv')

df = pd.DataFrame(parser_data.data)

df['math score'] = df['math score'].astype(int)
df['reading score'] = df['reading score'].astype(int)
df['writing score'] = df['writing score'].astype(int)

df['total score'] = df['math score'] + df['reading score'] + df['writing score']

plt.subplot(1, 3, 1)
sns.histplot(df['math score'], bins=20, kde=True)
plt.title('Распределение оценок по математике')

plt.subplot(1, 3, 2)
sns.histplot(df['reading score'], bins=20, kde=True, color='green')
plt.title('Распределение оценок по чтению')

plt.subplot(1, 3, 3)
sns.histplot(df['writing score'], bins=20, kde=True, color='red')
plt.title('Распределение оценок по письму')

plt.tight_layout()
plt.show()