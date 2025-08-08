from sklearn.preprocessing import LabelEncoder
data = [1,3,4,5,67, 78, 89, 89, 89, 56, 67, 67, 1]
le = LabelEncoder()
le.fit(data)
print(le.classes_)
data = ["Ferrari", "Ferrari", "Redbull", "Mercedes", "Ferrari"]
le.fit(data)
print(le.classes_)
print(le.transform(data))