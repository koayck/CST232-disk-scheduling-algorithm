import random

# disk_size = cylinder count
# head = starting cylinder
disk_size = 200
head = 50


# Function to perform C-SCAN on the request
# queue = list of requests
# head = position of disk head
def CSCAN(queue, head):
    max = 0
    movement_count = 0
    cur_track = 0
    request_size = len(queue)
    left = []
    right = []
    seek_sequence = []

    for i in range(request_size):
        if queue[i] < head:
            left.append(queue[i])
        if queue[i] > head:
            right.append(queue[i])

    # Appending end values which has to be visited before reversing the direction
    left.append(0)
    right.append(disk_size - 1)

    # Sorting left and right requests queue
    left.sort()
    right.sort()

    # First service the requests on the right side of the head
    while right:
        cur_track = right.pop(0)

        # Appending current track seek sequence
        seek_sequence.append(cur_track)

        # Calculate absolute distance of track from head, then add to total track count
        movement_count += abs(cur_track - head)

        if max < movement_count:
            max = movement_count

        # Accessed track is now new head
        head = cur_track

    # Now service the requests on the left side of the head
    while left:
        cur_track = left.pop(0)

        # Appending current track to seek sequence
        seek_sequence.append(cur_track)

        # Calculate absolute distance of track from head, then add to total track count
        movement_count += abs(cur_track - head)

        if max < movement_count:
            max = movement_count

        # Accessed track is now the new head
        head = cur_track

    # Display the total number of head track
    print("Total number of head movement = ", movement_count)

    # Display the seek sequence
    print("Seek Sequence is", ", ".join(str(track) for track in seek_sequence))

    # Display the maximum head movement
    print("Maximum head movement (worst-case) = ", max)

# Display initial position of head
print("Initial position of head: ", head)

# input number of requests
# request_size = int(input("Enter number of requests: "))

# Creating a random request queue
queue = [
    147,
    182,
    143,
    158,
    137,
    143,
    11,
    112,
    21,
    187,
    62,
    135,
    136,
    56,
    117,
    150,
    25,
    108,
    57,
    57,
    181,
    157,
    153,
    175,
    48,
    56,
    98,
    52,
    178,
    91,
    3,
    24,
    98,
    146,
    6,
    94,
    8,
    124,
    156,
    82,
    130,
    185,
    1,
    57,
    2,
    96,
    50,
    167,
    171,
    175,
    7,
    196,
    17,
    18,
    72,
    82,
    58,
    68,
    35,
    188,
    128,
    110,
    0,
    170,
    65,
    188,
    182,
    55,
    194,
    88,
    73,
    111,
    4,
    147,
    112,
    23,
    114,
    184,
    140,
    11,
    42,
    61,
    51,
    124,
    77,
    187,
    39,
    169,
    40,
    39,
    175,
    10,
    14,
    0,
    188,
    49,
    91,
    91,
    68,
    72,
]

# for i in range(request_size):
#     queue.append(random.randint(0, disk_size - 1))

CSCAN(queue, head)
