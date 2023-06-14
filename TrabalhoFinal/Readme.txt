[TRABALHO] Adicionar a explicação 
    1º layer
    linha: model.add(Conv2D(28, kernel_size=(3,3), input_shape = input_shape)): Adds a convolutional layer with 28 filters and a kernel size of (3, 3). The input_shape parameter defines the shape of the input data.
    Referência "An example of convolution operation to detect vertical edges:" https://github.com/amanchadha/coursera-deep-learning-specialization/tree/master/C4%20-%20Convolutional%20Neural%20Networks/Notes

model.summary() 

Model: "sequential_2"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_2 (Conv2D)            (None, 26, 26, 28)        280       
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 13, 13, 28)        0         
_________________________________________________________________
flatten_2 (Flatten)          (None, 4732)              0         
_________________________________________________________________
dense_6 (Dense)              (None, 128)               605824    
_________________________________________________________________
dropout_4 (Dropout)          (None, 128)               0         
_________________________________________________________________
dense_7 (Dense)              (None, 70)                9030      
_________________________________________________________________
dropout_5 (Dropout)          (None, 70)                0         
_________________________________________________________________
dense_8 (Dense)              (None, 10)                710       
=================================================================
Total params: 615,844
Trainable params: 615,844
Non-trainable params: 0
_________________________________________________________________

https://colab.research.google.com/drive/1W8fCTLZAO9YKcNRQzYfFf__9CROQLOcZ#scrollTo=oZQBaIHv7q1Y