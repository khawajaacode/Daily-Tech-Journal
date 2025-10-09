### **1\. Supervised Learning**

**Definition:**\
Supervised learning is a type of machine learning where the model is trained using a labeled dataset. This means each input data point is paired with a correct output (target), allowing the algorithm to learn a mapping from inputs to outputs.

**Goal:**\
To predict the output for new, unseen data based on what it learned from the labeled training data.

**How It Works:**

1.  The model is fed input-output pairs.

2.  It learns the relationship or pattern between them.

3.  When given new input data, it predicts the output.

4.  Performance is evaluated using metrics like accuracy, precision, recall, etc.

**Examples:**

-   Predicting house prices (Regression)

-   Classifying emails as spam or not spam (Classification)

-   Handwriting recognition

-   Credit card fraud detection

**Types of Supervised Learning:**

-   **Regression:** Predicting continuous values (e.g., price, temperature).

-   **Classification:** Predicting discrete categories (e.g., spam/not spam).

**Common Algorithms:**

-   Linear Regression

-   Logistic Regression

-   Decision Trees

-   Random Forest

-   Support Vector Machines (SVM)

-   Neural Networks

* * * * *

### **2\. Unsupervised Learning**

**Definition:**\
Unsupervised learning uses **unlabeled data**, meaning there are no output labels provided. The algorithm tries to identify patterns, groupings, or structures hidden within the data.

**Goal:**\
To explore data structure and discover hidden patterns without human supervision.

**How It Works:**

1.  The model takes raw data without predefined labels.

2.  It identifies relationships, similarities, or groupings.

3.  It helps in understanding the underlying structure of the data.

**Examples:**

-   Customer segmentation

-   Market basket analysis

-   Anomaly detection

-   Dimensionality reduction for visualization

**Types of Unsupervised Learning:**

-   **Clustering:** Grouping similar data points together (e.g., K-Means, Hierarchical Clustering).

-   **Association:** Discovering rules that describe large portions of data (e.g., Apriori algorithm).

-   **Dimensionality Reduction:** Reducing the number of variables (e.g., PCA).

**Common Algorithms:**

-   K-Means Clustering

-   Hierarchical Clustering

-   DBSCAN

-   Principal Component Analysis (PCA)

-   Autoencoders

* * * * *

### **3\. Key Differences Between Supervised and Unsupervised Learning**

| Feature | Supervised Learning | Unsupervised Learning |
| --- | --- | --- |
| **Data Type** | Labeled data | Unlabeled data |
| **Goal** | Predict outcomes | Find hidden patterns |
| **Human Involvement** | Requires labeled examples | No labeling required |
| **Output** | Known (target variable) | Unknown or hidden structure |
| **Examples** | Regression, Classification | Clustering, Association |
| **Accuracy** | Measured using metrics (accuracy, RMSE) | Difficult to measure directly |
| **Complexity** | Often more complex | Relatively simpler but abstract |