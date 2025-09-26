"""
Part 2, Lecture 1

Implement and test argmax() function that returns the location of a maximum.
"""


def argmax(values):
    """
    Return the location and value of the maximum contained in a given sequence.

    Parameters
    ----------
    values : Sequence of numbers

    Returns
    -------
    imax : int
        Location of the maximum
    """

    N = len(values)

    # Check that the sequence is not empty
    if N == 0:
        raise ValueError('attempt to get argmax of an empty sequence')

    # Initialise the maximum location and value
    imax = 0
    vmax = values[0]

    # Loop through the sequence to find the maximum
    for i in range(1, N):
        v = values[i]
        # If the current value is greater than the maximum found so far,
        # update the maximum location and value
        if v > vmax:
            imax = i
            vmax = v

    return imax


def main():
    """
    Main function to test argmax().
    """

    # Create list of values to test argmax()
    values = [2, 3, -1, 7, 4]

    # Use argmax() to locate the maximum
    imax = argmax(values)
    # Print the maximum value and its index
    vmax = values[imax]
    print(f'Max. value is {vmax} located at index {imax}')

    # Check that function raises an error for empty sequences
    imax = argmax([])


if __name__ == '__main__':
    # Run the main function if this script is executed
    main()