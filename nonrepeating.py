from queue import Queue

"""Script to find the first non-repeating string in a stream.

This module reads a file called stream.txt to create a stream of strings.  As a string is received, return the first
non-repeating string in the stream.

Example:
    $ python nonrepeating.py
    
Todo:
    * Add input argument for file to parse as stream
    * Create separate main so this is separate module
"""


def non_repeating(value, counts, q):
    """Finds the first non-repeating string in a stream.

    Args:
        value (str): Latest string received in the string
        counts (dict): Dictionary of strings containing the counts to determine if string is repeated
        q (Queue): Container for all strings in stream that have yet determined as being repeated

    Return:
        str: First non-repeating string. None if all strings are repeated.
    """
    q.put(value)

    if value in counts:
        counts[value] += 1
    else:
        counts[value] = 1

    while not q.empty():
        if counts[q.queue[0]] > 1:
            q.get()
        else:
            return q.queue[0]

    if q.empty():
        return None


def process_stream():
    """Processes the input file as a stream.
    """
    counts = {}
    q = Queue()

    with open('stream.txt') as stream:
        [print(non_repeating(value.strip(), counts, q)) for value in stream.readlines()]


def main():
    """Driver method.
    """
    process_stream()


if __name__ == '__main__':
    main()
