import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np

# Step 1: Generate synthetic dataset with 3 clusters
def generate_data(n_samples=300, centers=3, cluster_std=0.60, random_state=0):
    """
    Generate a synthetic 2D dataset using make_blobs.
    """
    X, y_true = make_blobs(n_samples=n_samples, centers=centers,
                           cluster_std=cluster_std, random_state=random_state)
    return X, y_true

# Step 2: Apply KMeans clustering
def apply_kmeans(X, n_clusters=3, random_state=0):
    """
    Fit KMeans to the data and return the model and predicted labels.
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    kmeans.fit(X)
    return kmeans, kmeans.labels_

# Step 3: Evaluate clustering performance
def evaluate_clustering(X, labels, kmeans_model):
    """
    Calculate and print inertia and silhouette score.
    """
    inertia = kmeans_model.inertia_
    silhouette = silhouette_score(X, labels)

    print("=== Clustering Evaluation Metrics ===")
    print(f"Inertia (within-cluster sum of squares): {inertia:.2f}")
    print(f"Silhouette Score (higher is better): {silhouette:.4f}")

    return inertia, silhouette

# Step 4: Visualize the clustered data
def visualize_clusters(X, labels, kmeans_model):
    """
    Plot the clustered data points and cluster centers.
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis', alpha=0.6, edgecolors='k')

    # Plot cluster centers
    centers = kmeans_model.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, marker='X', label='Centroids')

    plt.title("KMeans Clustering Results (k=3)")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.legend()
    plt.grid(True)
    plt.show()

# Main function to run the entire process
def main():
    # Generate data
    X, y_true = generate_data()

    # Apply KMeans
    kmeans_model, labels = apply_kmeans(X, n_clusters=3)

    # Evaluate performance
    evaluate_clustering(X, labels, kmeans_model)

    # Visualize clusters
    visualize_clusters(X, labels, kmeans_model)

# Execute the main function
if __name__ == "__main__":
    main()