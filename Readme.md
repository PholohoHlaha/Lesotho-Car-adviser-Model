Car Adviser AI Model
Overview

This AI model advises a buyer on the condition of a car based on several categorical features. It uses three types of Naive Bayes classifiers: CategoricalNB, GaussianNB, and MixedNB, to predict the state of the car. This project can be extended to include additional features, such as scanning an engine to determine its duration, making it useful for every Mosotho buying a vehicle from dealers.
Features

    CategoricalNB: Handles categorical features.
    GaussianNB: Handles continuous features.
    MixedNB: Handles a mix of categorical and continuous features.
    Interactive Input: Allows users to input car features and get a prediction on the car's condition.
    Accuracy Reporting: Provides accuracy of each classifier on test data.

Requirements

    Python 3.x
    pandas
    scikit-learn
    mixed-naive-bayes

Installation
Step-by-Step Installation
1. Clone the Repository

sh

git clone https://github.com/PholohoHlaha/Car-Modelling-.git
cd car-adviser-ai

2. Create a Virtual Environment

It's a good practice to create a virtual environment to manage dependencies.

sh

python -m venv venv
source venv/bin/activate    # On Windows use `venv\Scripts\activate`

3. Install Required Packages

sh

pip install pandas scikit-learn mixed-naive-bayes

4. The dataset is called car.data

Ensure you have the above dataset for training and testing the model.

5. Run the Model

Execute the Python script to train the classifiers and make predictions.

sh

python car_adviser.py

Installation on Specific Operating Systems
On Linux

    Install Python and Pip:

    sh

    sudo apt update
    sudo apt install python3 python3-pip

    Follow the general installation steps above from cloning the repository to running the model.

On Windows

    Install Python:
        Download and install Python from the official website.

    Follow the general installation steps above from cloning the repository to running the model.

On macOS

    Install Homebrew (if not already installed):

    sh

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Install Python:

sh

    brew install python

    Follow the general installation steps above from cloning the repository to running the model.

Usage

    Training and Testing: The script will split the data into training and testing sets, train each classifier, and print their accuracies.
    Interactive Prediction: After training, you can input car features interactively, and the model will predict the car's condition.

Example Input

When prompted, enter car features separated by commas:


Enter data separated by commas: vhigh,high,3,4,med,high

csharp

The car condition is VERY GOOD

Future Enhancements

    Engine Scanning Feature: Implement a feature to scan an engine and predict its duration.
    Improved Model: Explore additional machine learning models to improve prediction accuracy.
    User Interface: Develop a web or mobile interface for easier interaction.

License

This project is licensed under the MIT License.
Contact

For any inquiries or questions, please contact pholohohlaha@gmail.com

