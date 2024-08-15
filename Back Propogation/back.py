import numpy as np

# Input data
X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)

# Normalize input data
X = X / np.amax(X, axis=0)  # Maximum of X array longitudinally
y = y / 100

# Sigmoid Function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of Sigmoid Function
def derivatives_sigmoid(x):
    return x * (1 - x)

# Variable initialization
epoch = 5  # Setting training iterations
lr = 0.1  # Setting learning rate
inputlayer_neurons = 2  # Number of features in data set
hiddenlayer_neurons = 3  # Number of hidden layers neurons
output_neurons = 1  # Number of neurons at output layer

# Weight and bias initialization
wh = np.random.uniform(size=(inputlayer_neurons, hiddenlayer_neurons))
bh = np.random.uniform(size=(1, hiddenlayer_neurons))
wout = np.random.uniform(size=(hiddenlayer_neurons, output_neurons))
bout = np.random.uniform(size=(1, output_neurons))

# Training process
for i in range(epoch):
    # Forward Propagation
    hinp1 = np.dot(X, wh)
    hinp = hinp1 + bh
    hlayer_act = sigmoid(hinp)
    outinp1 = np.dot(hlayer_act, wout)
    outinp = outinp1 + bout
    output = sigmoid(outinp)

    # Backpropagation
    EO = y - output  # Error at Output layer
    outgrad = derivatives_sigmoid(output)
    d_output = EO * outgrad
    EH = d_output.dot(wout.T)  # Error at Hidden layer
    hiddengrad = derivatives_sigmoid(hlayer_act)  # How much hidden layer weights contributed to the error
    d_hiddenlayer = EH * hiddengrad

    # Updating Weights and Biases
    wout += hlayer_act.T.dot(d_output) * lr
    wh += X.T.dot(d_hiddenlayer) * lr
    bout += np.sum(d_output, axis=0, keepdims=True) * lr
    bh += np.sum(d_hiddenlayer, axis=0, keepdims=True) * lr

    # Print the outputs
    print("----------- Epoch", i + 1, "Starts -----------")
    print("Input: \n" + str(X))
    print("Actual Output: \n" + str(y))
    print("Predicted Output: \n", output)
    print("----------- Epoch", i + 1, "Ends -----------\n")
