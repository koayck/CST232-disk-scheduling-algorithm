import random

# disk_size = cylinder count
# head = starting cylinder
disk_size = 200
head = 50

# Function to perform SCAN on the request
# queue = list of requests
# head = position of disk head
def SCAN(queue, head, direction):
    max = 0
    movement_count = 0
    cur_movement_count = 0
    cur_track = 0
    request_size = len(queue)
    left = []
    right = []
    seek_sequence = []

    for i in range(request_size):
        if queue[i] < head:
            left.append(queue[i])
        if queue[i] >= head:
            right.append(queue[i])

    # Appending end values which has to be visited before reversing the direction
    if direction == "left":
        left.append(0)
    if direction == "right":
        right.append(disk_size - 1)

    # Sorting left and right requests queue
    left.sort()
    right.sort()

    # Run the while loop two times, once for scanning right and another for left of the head
    run = 2
    while run != 0:
        if direction == "left":
            while left:
                cur_track = left.pop(-1)
                print(cur_track)

                # Appending current track to seek sequence
                seek_sequence.append(cur_track)

                # Calculate absolute distance of track from head
                cur_movement_count = abs(cur_track - head)

                # Add to total track count
                movement_count += cur_movement_count

                # Update maximum head movement
                if max < cur_movement_count:
                    max = cur_movement_count

                # Accessed track is now the new head
                head = cur_track

            # Reversing the direction
            direction = "right"

        elif direction == "right":
            while right:
                cur_track = right.pop(0)

                # Appending current track seek sequence
                seek_sequence.append(cur_track)

                # Calculate absolute distance of track from head
                cur_movement_count= abs(cur_track - head)

                # Add to total track count
                movement_count += cur_movement_count

                if max < cur_movement_count:
                    max = cur_movement_count
                    print(max)

                # Accessed track is now new head
                head = cur_track

            # Reversing the direction
            direction = "left"

        run -= 1

    # Display the total number of head track
    print("Total number of head movement = ", movement_count)

    # Display the seek sequence
    print("Seek Sequence is", ", ".join(str(track) for track in seek_sequence))

    # Display the maximum head movement
    print("Average Seek Time = ", (movement_count/len(seek_sequence)).__round__(2))

    # Display the maximum head movement
    print("Worst-case Seek Time = ", max)

# Display initial position of head
print("Initial position of head: ", head)

# input number of requests
request_size = int(input("Enter number of requests: "))

# input direction
direction = input("Enter direction (left/right): ")

# Creating a random request queue
queue = []

for i in range(request_size):
    queue.append(random.randint(0, disk_size - 1))

SCAN(queue, head, direction)