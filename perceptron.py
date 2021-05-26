
# threshold: value that determines whether to output True or False
# adjustment: adjustment factor 
# weights: list of numbers representing initial weights on the inputs
# examples: list of examples for training the perceptron, [boolean, [(list of 1s and 0s)]] 
# passes: number of passes perceptrons hould make through the list of examples 
def perceptron(threshold, adjustment, weights, examples, passes):
    print(f"Starting weights:  {str(weights)}")
    print(f"Threshold:  {threshold}     Adjustment:  {adjustment}")
    for x in range (1, passes+1):
        print(f"\nPass  {x}\n")

        for i in range (0, len(examples)):
            answer = examples[i][0]
            inputs = examples[i][1]
            prediction = makePrediction(threshold, weights, inputs)
        
            print(f"inputs:  {inputs}")
            print(f"prediction:  {prediction}     answer:  {answer}")
            adjust(adjustment, weights, inputs, prediction, answer)
            print("adjusted weights: " + str(weights))

# Makes prediction of whether or not input falls into desired classification
# threshold: value that determines whether to output True or False
# returns True if the sum of products is greater than threshold 
#         False if the sum of products is less than threshold
def makePrediction(threshold, weights, example):
    # Calculate the sum of products
    sum = 0
    for weight, bin in zip(weights, example):
        product = weight*float(bin)
        sum+=product
    # See if the sum is above or below the threshold
    if sum > threshold:
        return True
    else: 
        return False

# Adjusts weights if perceptron predicts incorrectly 
# adjustment: adjustment factor 
# weights: list of numbers representing weights on the inputs
# prediction: True or False 
# answer: whether the input ACTUALLY falls into desired classification 
def adjust(adjustment, weights, inputs, prediction, answer):
    if (prediction == False) and (answer == True):
        for i, (input, weight) in enumerate(zip(inputs, weights)):
            if input == 1:
                weights[i] = weights[i]+adjustment
    elif (prediction == True) and (answer == False):
        for i, (input, weight) in enumerate(zip(inputs, weights)):
            if input == 1:
                weights[i] = weights[i]-adjustment


# Test Cases
# perceptron(0.5, 0.1, [-0.5, 0, 0.5, 0, -0.5], [[True, [1,1,1,1,0]], [False, [1,1,1,1,1]], [False, [0,0,0,0,0]], [False, [0,0,1,1,0]], [False, [1,0,1,0,1]], [False, [1,0,1,0,0]], [False, [0,1,0,1,1]], [False, [0,1,0,1,0]], [False, [0,0,1,0,0]], [False, [0,0,0,1,0]]], 4)
# perceptron(0.4, 0.09,  [0.3, -0.6], [[True, [1,1]], [False, [0,0]],[True, [0,1]], [True, [1,0]]], 10)