'''# Write a python program to find the square root of the given number'''
# using approximation method
# testcase 1
# input: 25
# output: 4.999999999999998
# testcase 2
# input: 49
# output: 6.999999999999991
def main():
    """Program starts here"""
    sq_ = int(input())
    epsilon_ = 0.01
    step_ = 0.1
    guess_ = 0.0
    while abs(guess_**2-sq_) >= epsilon_ and (guess_ <= sq_):
        guess_ = guess_+step_
    print(guess_)
if __name__ == "__main__":
    main()
