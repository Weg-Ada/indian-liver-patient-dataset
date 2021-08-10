# Indian Liver Patient Dataset

Code created in the Google Colab repository.

![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg) https://colab.research.google.com/drive/1s6ib0wg5ei7lIDUoAoVusRImUZhKJX10

## Description of the research problem 

Check how the quality of the classification (measured by the frequency of making a correct decision) depends on the number of features used. For artificial neural networks - unidirectional network with 1 hidden layer and for learning by back propagation method with parameter.

Steps taken:
* Data cleaning and preparation
* Rank the features in terms of their suitability for classification
* One hot encoding
* Prepare data for double cross-validation
* Neural network

  Consists of 3 layers:
  * from the input layer (number of input neurons = 106, number of output neurons = 106, activation function = 'relu'),
  * hidden layer (activation function = 'relu'),
  * output layer (number of output neurons = 8, activation function = 'softmax').
  
* Network learning
* Classification
* Creation of a confusion matrix

## Description of the dataset

Source of [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/ILPD+(Indian+Liver+Patient+Dataset))

### Abstract

This data set contains 10 variables that are age, gender, total Bilirubin, direct Bilirubin, total proteins, albumin, A/G ratio, SGPT, SGOT and Alkphos.

### Source

1. Bendi Venkata Ramana
ramana.bendi@gmail.com
Associate Professor,
Department of Information Technology,
Aditya Instutute of Technology and Management,
Tekkali - 532201, Andhra Pradesh, India.

2. Prof. M. Surendra Prasad Babu
drmsprasadbabu@yahoo.co.in
Deptartment of Computer Science & Systems Engineering,
Andhra University College of Engineering,
Visakhapatnam-530 003 Andhra Pradesh, India.

3. Prof. N. B. Venkateswarlu
venkat_ritch@yahoo.com
Department of Computer Science and Engineering,
Aditya Instutute of Technology and Management,
Tekkali - 532201, Andhra Pradesh, India.

### Data Set Information

This data set contains 416 liver patient records and 167 non liver patient records.The data set was collected from north east of Andhra Pradesh, India. Selector is a class label used to divide into groups (liver patient or not). This data set contains 441 male patient records and 142 female patient records.

Any patient whose age exceeded 89 is listed as being of age "90".

### Attribute Information

1. Age Age of the patient
2. Gender Gender of the patient
3. TB Total Bilirubin
4. DB Direct Bilirubin
5. Alkphos Alkaline Phosphotase
6. Sgpt Alamine Aminotransferase
7. Sgot Aspartate Aminotransferase
8. TP Total Protiens
9. ALB Albumin
10. A/G Ratio Albumin and Globulin Ratio
11. Selector field used to split the data into two sets (labeled by the experts)
