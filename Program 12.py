import statistics as stats

x = list(map(int, input("Enter numbers separated by space [Eg:- 1 2 3]: ").split()))

mean = sum(x) / len(x)
median = stats.median(x)
try:
    mode = stats.mode(x)
except stats.StatisticsError:
    mode = "No unique mode"
std = stats.stdev(x)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Standard Deviation:", std)
