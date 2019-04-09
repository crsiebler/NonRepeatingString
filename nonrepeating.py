from queue import Queue


def non_repeating(value, counts, q):
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
    counts = {}
    q = Queue()

    with open('stream.txt') as stream:
        [print(non_repeating(value.strip(), counts, q)) for value in stream.readlines()]


def main():
    process_stream()


if __name__ == '__main__':
    main()
