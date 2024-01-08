import random

# disk_size = cylinder count
# head = starting cylinder
disk_size = 200
head = 50


# Function to perform C-LOOK on the request
# queue = list of requests
# head = position of disk head
def CLOOK(queue, head):
    max = 0
    movement_count = 0
    cur_track = 0
    request_size = len(queue)

    left = []
    right = []
    seek_sequence = []

    # Appending tracks to left and right arrays
    for i in range(request_size):
        if queue[i] < head:
            left.append(queue[i])
        if queue[i] > head:
            right.append(queue[i])

    # Sorting left and right requests
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
request_size = int(input("Enter number of requests: "))

# Creating a random request queue
queue = []

for i in range(request_size):
    queue.append(random.randint(0, disk_size - 1))

print("Initial Queue: ", queue)

CLOOK(queue, head)
