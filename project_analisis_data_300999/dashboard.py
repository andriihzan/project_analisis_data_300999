import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Memuat dataset
df = pd.read_csv("data/day.csv")

# Judul Dashboard
st.title("Bike Sharing Dashboard")

# Line Chart: Tren Penggunaan Sepeda dari Waktu ke Waktu
st.subheader("Trend of Bike Rentals Over Time")
fig, ax = plt.subplots()
ax.plot(df["dteday"], df["cnt"], label="Total Rentals")
ax.set_xlabel("Date")
ax.set_ylabel("Total Rentals")
ax.set_title("Trend of Bike Rentals Over Time")
st.pyplot(fig)

# Bar Chart: Penggunaan Sepeda Berdasarkan Hari Kerja
df["is_weekend"] = df["weekday"].apply(lambda x: 1 if x >= 5 else 0)
st.subheader("Total Bike Rentals on Weekdays vs Weekends")
fig, ax = plt.subplots()
df.groupby("is_weekend")["cnt"].sum().plot(kind="bar", ax=ax)
ax.set_xlabel("Is Weekend")
ax.set_ylabel("Total Rentals")
ax.set_title("Total Bike Rentals on Weekdays vs Weekends")
st.pyplot(fig)

# Box Plot: Distribusi Pengguna Sepeda Berdasarkan Musim
st.subheader("Bike Rentals by Season")
fig, ax = plt.subplots()
sns.boxplot(x="season", y="cnt", data=df, ax=ax)
ax.set_xlabel("Season")
ax.set_ylabel("Total Rentals")
ax.set_title("Bike Rentals by Season")
st.pyplot(fig)

# Heatmap: Korelasi Antar Fitur
st.subheader("Correlation Matrix")
correlation_matrix = df[
    ["temp", "atemp", "hum", "windspeed", "casual", "registered", "cnt"]
].corr()
fig, ax = plt.subplots()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", ax=ax)
ax.set_title("Correlation Matrix")
st.pyplot(fig)

# Histogram: Distribusi Pengguna Sepeda
st.subheader("Distribution of Total Bike Rentals")
fig, ax = plt.subplots()
df["cnt"].hist(bins=30, ax=ax)
ax.set_xlabel("Total Rentals")
ax.set_ylabel("Frequency")
ax.set_title("Distribution of Total Bike Rentals")
st.pyplot(fig)

# Scatter Plot: Hubungan Antara Suhu dan Pengguna Sepeda
st.subheader("Relationship Between Temperature and Bike Rentals")
fig, ax = plt.subplots()
sns.scatterplot(x="temp", y="cnt", data=df, ax=ax)
ax.set_xlabel("Temperature")
ax.set_ylabel("Total Rentals")
ax.set_title("Relationship Between Temperature and Bike Rentals")
st.pyplot(fig)

# Pie Chart: Proporsi Pengguna Sepeda Berdasarkan Situasi Cuaca
st.subheader("Proportion of Bike Rentals by Weather Situation")
weather_counts = df["weathersit"].value_counts()
fig, ax = plt.subplots()
ax.pie(
    weather_counts,
    labels=["Clear", "Mist", "Light Snow/Rain"],
    autopct="%1.1f%%",
    startangle=140,
)
ax.set_title("Proportion of Bike Rentals by Weather Situation")
st.pyplot(fig)
