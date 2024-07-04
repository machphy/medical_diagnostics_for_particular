from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint

# Import data generators from data_preprocessing.py
from data_preprocessing import train_generator, val_generator, test_generator

# Define CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')  # Output layer for binary classification
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.summary()  # Print model architecture

# Train the model
model.fit(
    train_generator,
    epochs=10,
    validation_data=val_generator
)

# Evaluate on test set
test_loss, test_acc = model.evaluate(test_generator)
print('Test accuracy:', test_acc)

# Save the model
model.save('xray_diagnosis_model')
