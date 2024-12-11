import joblib
import matplotlib.pyplot as PLT
import numpy as NP
import pandas as PD
import seaborn as SNS

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

"""
    function read_data(filename: str) -> PD.DataFrame
    - this function takes in a filename as a string and returns a Pandas DataFrame.
    - the file is a .csv file with a | delimiter/separator.
    - we drop the 'location' feature but keep the 'city' feature.
"""
def read_data(filename: str) -> PD.DataFrame:
    print(f'\nread_data({filename}) called -->')
    print(f'\tReading data from <{filename}>...')
    data = PD.read_csv(filepath_or_buffer = filename, sep = '|')
    data = data.drop(['location'], axis = 1)
    print('\tSuccesfully read data.')
    return data

"""
    function print_data_info(data: PD.DataFrame) -> None
    - this function takes in a Pandas DataFrame and prints its info.
"""
def print_data_info(data: PD.DataFrame) -> None:
    print('\nprint_data_info() called -->')
    print('\tData Info:')
    print('\t', data.info())

"""
    function feature_engineering(data: PD.DataFrame) -> PD.DataFrame:
    - this function takes in a Pandas DataFrame and performs feature engineering.
    - creates a new feature 'price_per_sqft', 'total_rooms', and 'luxury_index'.
    - drops any null valued rows
    - returns the modified DataFrame.
"""    
def feature_engineering(data: PD.DataFrame) -> PD.DataFrame:
    print('\nfeature_engineering() called -->')
    print('\tPerforming feature engineering...')
    
    feature_engineered_data = data
    # feature_engineered_data['price'] = feature_engineered_data['price'] * 0.0036
    # feature_engineered_data['bedrooms'] = feature_engineered_data['bedrooms']
    # feature_engineered_data['baths'] = feature_engineered_data['baths']
    # feature_engineered_data['size'] = feature_engineered_data['size']
    feature_engineered_data['bed_bath_ratio'] = feature_engineered_data['bedrooms'] / (feature_engineered_data['baths'] + 1e-9)
    feature_engineered_data['price_per_sqft'] = feature_engineered_data['price'] / (feature_engineered_data['size'] + 1e-9)
    feature_engineered_data['total_rooms'] = feature_engineered_data['bedrooms'] + (feature_engineered_data['baths'] + 1e-9)
    feature_engineered_data['luxury_index'] = feature_engineered_data['size'] + (feature_engineered_data['bedrooms'] * 0.5) + (feature_engineered_data['baths'] * 0.3)
    
    feature_engineered_data = feature_engineered_data.dropna()
    
    print('\tFeature engineering completed.')
    
    print_data_info(data = feature_engineered_data)
    
    return feature_engineered_data

"""
    function categorical_encoding(data: PD.DataFrame) -> PD.DataFrame:
    - this function takes in a Pandas DataFrame and performs categorical encoding on the city feature.
"""
def categorical_encoding(data: PD.DataFrame) -> PD.DataFrame:
    print('\ncategorical_encoding() called -->')
    print('\tCategorical encoding...')
    
    categorical_data = data.copy()
    
    categorical_data = categorical_data.join(PD.get_dummies(categorical_data.city))
    
    categorical_data = categorical_data.drop(columns = ['city'], axis = 1)
    
    print('\tCategorical encoding completed.')
    
    print_data_info(data = categorical_data)
    
    return categorical_data

"""
    function scale_data(data: PD.DataFrame) -> PD.DataFrame:
    - this function scales the dataset using StandardScaler from sklearn.preprocessing.
"""
def scale_data(data: PD.DataFrame) -> PD.DataFrame:
    print('\nscale_data() called -->')
    print('\tScaling data...')
    
    scaled_data = data.copy()
    
    scaled_data['price'] = NP.log(scaled_data['price'] + 1)
    scaled_data['price_per_sqft'] = NP.log(scaled_data['price_per_sqft'] + 1)
    scaled_data['bed_bath_ratio'] = NP.log(scaled_data['bed_bath_ratio'] + 1)
    scaled_data['size'] = NP.log(scaled_data['size'] + 1)
    scaled_data['luxury_index'] = NP.log(scaled_data['luxury_index'] + 1)
    
    print('\tScaling completed.')
    
    return scaled_data

"""
    function linear_regression(x_train: PD.Series, X_test: PD.Series, y_train: PD.Series, Y_test: PD.Series) -> None:
    - this function performs linear regression using the training data and evaluates the model on both the training and test data.
"""
def linear_regression(x_train: PD.Series, X_test: PD.Series, y_train: PD.Series, Y_test: PD.Series) -> None:
    print('\nlinear_regression() called -->')
    print('\tTraining Linear Regression model...')
    
    model = LinearRegression()
    
    model.fit(X = x_train, y = y_train)
    print('\tLinear Regression model trained.')
    
    train_predictions = model.predict(x_train)
    train_mse = mean_squared_error(y_train, train_predictions)
    train_r2 = r2_score(y_train, train_predictions)
    print(f'\tTraining Mean Squared Error: {train_mse:.4f}')
    print(f'\tTraining R^2 Score: {train_r2:.4f}')
    
    print("\n\tEvaluating model on test data...")
    test_predictions = model.predict(X_test)
    test_mse = mean_squared_error(Y_test, test_predictions)
    test_r2 = r2_score(Y_test, test_predictions)
    print(f"\tTest Mean Squared Error: {test_mse:.4f}")
    print(f"\tTest R^2 Score: {test_r2:.4f}")

"""
    function multiple_linear_regression(x_train: PD.Series, X_test: PD.Series, y_train: PD.Series, Y_test: PD.Series) -> None:
    - this function performs multiple linear regression using the training data and evaluates the model on both the training and test data.
"""
def multiple_linear_regression(x_train: PD.Series, X_test: PD.Series, y_train: PD.Series, Y_test: PD.Series) -> None:
    print('\nmultiple_linear_regression() called -->')
    print('\tTraining Multiple Linear Regression model...')
    
    model = LinearRegression()
    
    model.fit(X = x_train, y = y_train)
    print('\tMultiple Linear Regression model trained.')
    
    train_predictions = model.predict(x_train)
    train_mse = mean_squared_error(y_train, train_predictions)
    train_r2 = r2_score(y_train, train_predictions)
    print(f'\tTraining Mean Squared Error: {train_mse:.4f}')
    print(f'\tTraining R^2 Score: {train_r2:.4f}')
    
    print("\n\tEvaluating model on test data...")
    test_predictions = model.predict(X_test)
    test_mse = mean_squared_error(Y_test, test_predictions)
    test_r2 = r2_score(Y_test, test_predictions)
    print(f"\tTest Mean Squared Error: {test_mse:.4f}")
    print(f"\tTest R^2 Score: {test_r2:.4f}")
    
    print('\n\tModel Coefficients (weights):')
    for feature, coeficient in zip(x_train.columns, model.coef_):
        print(f'\t - {feature}: {coeficient:.4f}')
    print(f'\tModel Intercept: {model.intercept_:.4f}')

"""
    function random_forest_regression(x_train: PD.Series, X_test: PD.Series, y_train: PD.Series, Y_test: PD.Series, n_estimators = 100, random_state = 42) -> None:
    - this function performs random forest regression using the training data and evaluates the model on both the training and test data.
"""
def random_forest_regression(x_train: PD.Series, X_test: PD.Series, y_train: PD.Series, Y_test: PD.Series, n_estimators = 100, random_state = 42) -> None:
    print('\nrandom_forest_regression() called -->')
    print('\tTraining Random Forest Regression model...')
    
    RF_MODEL = RandomForestRegressor(n_estimators = n_estimators, random_state = random_state)
    
    RF_MODEL.fit(X = x_train, y = y_train)
    print('\tRandom Forest Regression model trained.')
    
    Y_PRED_RF = RF_MODEL.predict(X = x_train)
    mae_rf = mean_absolute_error(y_train, Y_PRED_RF)
    mse_rf = mean_squared_error(y_train, Y_PRED_RF)
    r2_rf = r2_score(y_train, Y_PRED_RF)
    print(f"\nRandom Forest - Mean Absolute Error (MAE): {mae_rf:.4f}")
    print(f"Random Forest - Mean Squared Error (MSE): {mse_rf:.4f}")
    print(f"Random Forest - R² Score: {r2_rf:.4f}")
    
    print("\n\tEvaluating model on test data...")
    Y_TEST_RF = RF_MODEL.predict(X = X_test)
    mae_rf = mean_absolute_error(Y_test, Y_TEST_RF)
    mse_rf = mean_squared_error(Y_test, Y_TEST_RF)
    r2_rf = r2_score(Y_test, Y_TEST_RF)
    print(f"Random Forest - Mean Absolute Error (MAE): {mae_rf:.4f}")
    print(f"Random Forest - Mean Squared Error (MSE): {mse_rf:.4f}")
    print(f"Random Forest - R² Score: {r2_rf:.4f}")

"""
    function display_data_histogram(data: PD.DataFrame) -> None:
    - this function displays histograms of all the feautures in the dataset.
"""
def display_data_histogram(data: PD.DataFrame) -> None:
    print('\ndisplay_train_data_histograms() called -->')
    print('\t<train_data> histogram:')
    data.hist(bins = 10, figsize = (15, 8))
    PLT.show()

"""
    function display_correlation_heatmap(data: PD.DataFrame) -> None:
    - this function displays a correlation heatmap of all the features in the dataset.
"""
def display_correlation_heatmap(data: PD.DataFrame):
    print('\ndisplay_correlation_heatmap() called -->')
    print('\t<data> correlation heatmap:')
    
    print('data -->')
    print(data)
    
    PLT.figure(figsize = (15, 8))
    SNS.heatmap(data.corr(), annot = True, cmap = 'YlGnBu')
    PLT.show()

def main() -> None:
    DATA_FILENAME = 'data.csv'
    
    DATA = read_data(filename = DATA_FILENAME)
    print_data_info(data = DATA)
    # display_data_histogram(data = DATA)
    
    FEATURE_ENGINEERED_DATA = feature_engineering(data = DATA)
    # display_data_histogram(data = FEATURE_ENGINEERED_DATA)
    
    CATEGORICAL_ENCODED_DATA = categorical_encoding(data = FEATURE_ENGINEERED_DATA)
    # display_data_histogram(data = CATEGORICAL_ENCODED_DATA)
    
    SCALED_DATA = scale_data(data = CATEGORICAL_ENCODED_DATA)
    # display_data_histogram(data = SCALED_DATA)
    # display_correlation_heatmap(data = SCALED_DATA)
    
    TRAIN_DATA = SCALED_DATA
    x = SCALED_DATA.drop(['price'], axis = 1)
    y = SCALED_DATA['price']
    x_train, X_test, y_train, Y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)
    
    linear_regression(x_train = x_train, X_test = X_test, y_train = y_train, Y_test = Y_test)
    
    multiple_linear_regression(x_train = x_train, X_test = X_test, y_train = y_train, Y_test = Y_test)
    
    random_forest_regression(x_train = x_train, X_test = X_test, y_train = y_train, Y_test = Y_test, n_estimators = 100, random_state = 42)
    
if __name__ == '__main__':
    main()