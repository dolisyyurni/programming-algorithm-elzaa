# Program KNN dengan scikit-learn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Memuat dataset Iris
iris = load_iris()
X, y = iris.data, iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model dan pelatihan
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train, y_train)

# Prediksi
y_prediksi = knn_model.predict(X_test)

# Akurasi
akurasi = accuracy_score(y_test, y_prediksi)
print(f"Akurasi KNN: {akurasi * 100:.2f}%")
