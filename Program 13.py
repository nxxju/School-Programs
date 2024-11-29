import matplotlib.pyplot as plt

x = ["Surya", "Sumedh", "Aaron", "Rayaansh", "Ishaan"]
y = [45, 70, 89, 50, 92]

plt.bar(x, y, color='skyblue')

plt.title("Comparison of Students' Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
