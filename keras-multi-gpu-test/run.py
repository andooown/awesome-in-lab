# -*- coding: utf-8 -*-

import os
import subprocess

# 利用可能な GPU の数を取得
res = subprocess.run(['nvidia-smi', '--query-gpu=index', '--format=csv,noheader'], stdout=subprocess.PIPE)
GPU_COUNT = len(res.stdout.splitlines())

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['CUDA_VISIBLE_DEVICES'] = ','.join(map(str, range(GPU_COUNT)))

from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Conv2D, Dense, Activation, MaxPooling2D, BatchNormalization, Dropout, Flatten
from keras.optimizers import Adam
from keras.utils import multi_gpu_model, to_categorical
import tensorflow as tf
import time

NUM_CLASSES = 10
EPOCHS = 10
BATCHSIZE = 32


def load_data(num_classes):
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()

    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0

    y_train = to_categorical(y_train, num_classes)
    y_test = to_categorical(y_test, num_classes)

    return (x_train, y_train), (x_test, y_test)


def create_model(input_shape, num_classes):
    model = Sequential()

    model.add(Conv2D(32, (3, 3), padding='same', input_shape=input_shape))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(Conv2D(32, (3, 3)))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3, 3), padding='same'))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(Conv2D(64, (3, 3)))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes))
    model.add(Activation('softmax'))

    return model


def build_model(input_shape, num_classes, gpus):
    if gpus > 1:
        with tf.device("/cpu:0"):
            model = create_model(input_shape, num_classes)
        model = multi_gpu_model(model, gpus=gpus)
    else:
        model = create_model(input_shape, num_classes)

    opt = Adam()
    model.compile(
        optimizer=opt,
        loss='categorical_crossentropy',
        metrics=['accuracy'])

    return model


def main():
    print('Load cifar10 dataset.....', end='')
    (x_train, y_train), (x_test, y_test) = load_data(NUM_CLASSES)
    print('Done.')

    for gpu in range(1, GPU_COUNT + 1):
        print('Use {0} gpu{1}.'.format(gpu, 's' if gpu > 1 else ''))

        print('Build model.....', end='')
        model = build_model(x_train.shape[1:], NUM_CLASSES, gpu)
        print('Done.')

        print('Train model.....', end='')
        start_time = time.time()
        history = model.fit(
            x_train, y_train,
            batch_size=BATCHSIZE * gpu,
            epochs=EPOCHS,
            validation_data=(x_test, y_test),
            shuffle=True,
            verbose=0)
        elapsed_time = time.time() - start_time
        print('Done.')

        print('Validation accuracy: {:.2%}'.format(history.history['val_acc'][-1]))
        print('Average time / epochs: {}sec'.format(elapsed_time / EPOCHS))


if __name__ == '__main__':
    main()
