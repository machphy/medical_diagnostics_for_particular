
# X-ray Diagnosis Project

## Overview
This project aims to create a machine learning model for diagnosing X-ray images of chest conditions. It includes data preprocessing, model training using deep learning techniques, and a Flask-based web application for real-time diagnosis.

## Project Structure
The project is structured as follows:

- **`chest_xray/`**: Contains the dataset divided into `train/`, `val/`, and `test/` subdirectories.
- **`uploads/`**: Directory where user-uploaded X-ray images are stored for diagnosis.
- **`templates/`**: Contains HTML templates for the Flask web application.
  - `index.html`: Main page for uploading X-ray images.
  - `result.html`: Page for displaying diagnosis results.
  - `base.html`: Base template for layout and common elements.
- **`static/`**: Directory for static files (CSS, JavaScript).
  - `style.css`: Custom CSS for styling the application.
  - `script.js`: JavaScript for client-side functionality.
- **`app.py`**: Flask application file handling routes and interactions.
- **`data_preprocessing.py`**: Script for preprocessing X-ray images.
- **`train_model.py`**: Script for training the X-ray diagnosis model.
- **`xray_diagnosis_model.h5`**: Pre-trained model for diagnosing X-ray images.

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/machphy/medical_diagnostics_for_particular
   cd xray_diagnosis_project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open your web browser and go to `http://localhost:5000` to use the application.

## Usage
- Navigate to the main page (`/`) to upload an X-ray image.
- After uploading, the image will be processed, and the diagnosis result will be displayed on the `result` page.

## Technologies Used
- Python
- Flask
- OpenCV
- TensorFlow/Keras

## Contributing
Contributions are welcome. If you'd like to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/new-feature`).
6. Create a new Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
```
rajeebsharma@2024
