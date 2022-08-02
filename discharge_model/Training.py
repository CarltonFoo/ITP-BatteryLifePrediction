import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

import concurrent.futures

class Trainer:
    def __init__(self,
        model: keras.models.Model,
        train_x,
        train_y,
        validation_data=()):
        self.model = model
        self.history = None
        self.train_x = train_x
        self.train_y = train_y
        self.test_xy = validation_data
    def fit(self, epochs=1000):
        self.history = self.model.fit(
            self.train_x,
            self.train_y,
            epochs=epochs,
            validation_data=self.test_xy,
            verbose=0
        )
    def get_history(self):
        return self.history

class TrainThread:
    def __init__(self, create_model_callback, use_cpu="/cpu:0"):
        self.device = tf.device(use_cpu)
        self.create_model = create_model_callback
    def build_and_train(self, train_x, train_y, validation_data=(), epochs=1000):
        with self.device:
            model = self.create_model()
            keras.utils.set_random_seed(
                (hash(self.device) ^ hash(model)) & 0xFFFFFFFF
            )
            trainer = Trainer(
                model, train_x, train_y, validation_data
            )
            trainer.fit(epochs)
            return {
                'history': trainer.get_history(),
                'RMSE': model.evaluate(
                    validation_data[0],
                    validation_data[1],
                    verbose=0
                ) ** 0.5,
                'model': model
            }

def singlethread_train(train_x, train_y, test_x, test_y, create_model_callback, epochs=1000, device_name="/cpu:0"):
    thread = TrainThread(create_model_callback, device_name)
    print("Training on", device_name)
    return thread.build_and_train(
        train_x,
        train_y,
        (test_x, test_y),
        epochs
    )

def multithread_train(train_x, train_y, test_x, test_y, create_model_callback, device_list: list, epochs=1000, num_threads=1):
    with concurrent.futures.ThreadPoolExecutor(num_threads) as executor:
        train_one = lambda device_name: singlethread_train(
            train_x, train_y,
            test_x, test_y,
            create_model_callback,
            epochs,
            device_name
        )
        results = [x for x in executor.map(train_one, device_list)]
        return results
