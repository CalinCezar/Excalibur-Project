import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




st.markdown("### **Data Analysis Insights**")
st.markdown("### Based on the dataset we had:")


df = pd.read_csv("student_data/preprocessed_students.csv")
palette = sns.color_palette("pastel")
data = df['gender'].value_counts(normalize=True) * 100

fig, ax = plt.subplots(figsize=(7, 5))
ax.pie(data, labels=data.index, startangle=90, counterclock=False, autopct='%1.1f%%', colors=palette)
ax.set_title('Gender Distribution', fontsize=16)

st.title("Gender Distribution Visualization")
st.pyplot(fig)

data = df[df['hs_type'].isin(['Private', 'State'])].groupby('hs_type')['grade'].mean()

fig, ax = plt.subplots(figsize=(7, 5))
sns.barplot(x=data.index, y=data, ax=ax, palette='pastel')

ax.set_ylabel('Average Grade')
ax.set_title('Average Grade by High School Type')

st.title("Education Statistics")
st.pyplot(fig)

order = list(df['mother_job'].unique())
if 'Other' in order:
    order.remove('Other')

data_pie = df['mother_job'].value_counts(normalize=True) * 100
data_pie = data_pie.loc[order]

data_bar = df.groupby('mother_job')['grade'].mean().sort_values(ascending=False)
data_bar = data_bar.loc[order]

fig = plt.figure(figsize=(14, 5), constrained_layout=True)

plt.subplot(121)
plt.pie(data_pie, labels=data_pie.index, startangle=90, counterclock=False, autopct='%1.1f%%')

plt.subplot(122)
plt.bar(data_bar.index, data_bar, color='skyblue')
plt.xlabel('Mother\'s Occupation')
plt.ylabel('Average Grade')
plt.xticks(rotation=20)

st.title('Mother\'s Occupation and Average Grade')
st.pyplot(fig)

order = sorted(df['study_hrs'].dropna().unique())

data_pie = df['study_hrs'].value_counts(normalize=True) * 100
data_pie = data_pie.loc[order]

data_bar = df.groupby('study_hrs')['grade'].mean().sort_values(ascending=False)
data_bar = data_bar.loc[order]

fig = plt.figure(figsize=(14, 5), constrained_layout=True)

plt.subplot(121)
plt.pie(data_pie, labels=data_pie.index, startangle=90, counterclock=False, autopct='%1.1f%%')

plt.subplot(122)
sns.barplot(x=data_bar.index, y=data_bar, order=order, color='skyblue')
plt.xlabel('')
plt.ylabel('Average Grade')
plt.yticks([])
plt.box(False)

st.title('Weekly Study Hours and Average Grade')
st.pyplot(fig)

st.title('Reading Frequency')

order = list(df['read_freq'].dropna().unique())
data = df['read_freq'].value_counts(normalize=True) * 100
data = data.loc[order]

fig = plt.figure(figsize=(14, 5), constrained_layout=True)

plt.subplot(121)
plt.pie(data, labels=data.index, startangle=90, counterclock=False, autopct='%1.1f%%')

data_bar = df.groupby('read_freq')['grade'].mean().sort_values(ascending=False)
plt.subplot(122)
sns.barplot(x=data_bar.index, y=data_bar, order=order)
plt.xlabel('')
plt.ylabel('Average Grade')
plt.yticks([])
plt.box(False)

fig.suptitle('(non-scientific books/journals)', fontsize=18)
st.pyplot(fig)

order = list(df['read_freq_sci'].dropna().unique())
data = df['read_freq_sci'].value_counts(normalize=True) * 100
data = data.loc[order]

fig = plt.figure(figsize=(14, 5), constrained_layout=True)

plt.subplot(121)
plt.pie(data, labels=data.index, startangle=90, counterclock=False, autopct='%1.1f%%')

data_bar = df.groupby('read_freq_sci')['grade'].mean().sort_values(ascending=False)
plt.subplot(122)
sns.barplot(x=data_bar.index, y=data_bar, order=order)
plt.xlabel('')
plt.ylabel('Average Grade')
plt.yticks([])
plt.box(False)

fig.suptitle('(scientific books/journals)', fontsize=18)
st.pyplot(fig)

data = df.groupby('classroom')['grade'].mean().sort_values(ascending=False)

fig = plt.figure(figsize=(10, 5))

sns.barplot(x=data.index, y=data, order=data.index)
plt.xlabel('')
plt.ylabel('Average Grade')
plt.yticks([])
plt.box(False)

st.title("Flip-classroom ")
st.pyplot(fig)


order_mother_edu = ['Primary school', 'High school', 'Secondary school', 'University', 'MSc.', 'Ph.D.']  
order_father_edu = order_mother_edu[::-1] 

data = df.groupby(['mother_edu', 'father_edu']).size().reset_index(name='counts')

data_pivot = data.pivot(index='mother_edu', columns='father_edu', values='counts').fillna(0)

data_pivot = data_pivot.loc[order_mother_edu]
data_pivot = data_pivot[order_father_edu] 

fig, ax = plt.subplots(figsize=(10, 7), constrained_layout=True)
sns.heatmap(data_pivot.T.astype(int), annot=True, fmt='d', cmap='mako', linewidths=0.5, linecolor='gray', ax=ax)
ax.set_xlabel('Mother\'s Education')
ax.set_ylabel('Father\'s Education')

st.title("Parent's Education")
st.pyplot(fig)



