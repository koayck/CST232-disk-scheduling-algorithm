# CST232-disk-scheduling-algorithm

## Team Members
| Name | Email | Github Username |
| --- | --- | --- |
| Koay Chun Keat | koayck@student.usm.my | koayck |
| Lai Yicheng | laiyiching@student.usm.my | Jisi-A |
| Ang De Jie | dejieang168@gmail.com | Dejie1 |
| Anson Kiu Yi Kai | ansonkiu0212@gmail.com | NsonQ |

## Description

This project aims to optimize the performance of a disk drive with 200 cylinders and a current head position at cylinder 50 by comparing the SCAN, C-SCAN, and C-LOOK disk scheduling algorithms for a set of requests. These algorithms are implemented using Python programming language and their performance are analysed to determine the optimal scheduling strategy. Each algorithm is run with a set of 10, 20, 50, and 100 random requests.

## Introduction

Disk scheduling algorithms are used to reduce the seek time of a disk drive. The seek time is the time taken by the disk arm to move the heads to the cylinder containing the desired sector. The disk scheduling algorithm works by selecting the next request from the queue and then moving the disk arm to the cylinder containing the request. The performance of the disk scheduling algorithm is measured by the total seek time. The total seek time is the sum of the difference between the head position and the next request position. The lower the total seek time, the better the performance of the disk scheduling algorithm.

## Methodology

### SCAN Algorithm

The SCAN algorithm works by moving the disk arm from one end of the disk to the other, servicing requests along the way. When the head reaches the other end, it immediately returns to the beginning of the disk without servicing any requests on the return trip. The SCAN algorithm is also known as the elevator algorithm because the disk arm behaves like an elevator. The SCAN algorithm is implemented using the following steps:

1. Sort the requests in ascending order.

2. Find the first request in the sorted list that is greater than the current head position.

3. Move the disk arm in the direction of the first request.

4. Service the requests along the way.

5. If there are no more requests in the direction of the first request, move the disk arm in the opposite direction.

6. Service the requests along the way.

7. Repeat steps 5 and 6 until all requests have been serviced.

### C-SCAN Algorithm

The C-SCAN algorithm works by moving the disk arm from one end of the disk to the other, servicing requests along the way. When the head reaches the other end, it immediately returns to the beginning of the disk and continues servicing requests in the same direction. The C-SCAN algorithm is implemented using the following steps:

1. Sort the requests in ascending order.

2. Find the first request in the sorted list that is greater than the current head position.

3. Move the disk arm in the direction of the first request.

4. Service the requests along the way.

5. If there are no more requests in the direction of the first request, move the disk arm to the other end of the disk.

6. Service the requests along the way.

7. Repeat steps 5 and 6 until all requests have been serviced.

### C-LOOK Algorithm

The C-LOOK algorithm works by moving the disk arm from one end of the disk to the other, servicing requests along the way. When the head reaches the other end, it immediately returns to the beginning of the disk and continues servicing requests in the same direction. The C-LOOK algorithm is implemented using the following steps:

1. Sort the requests in ascending order.

2. Find the first request in the sorted list that is greater than the current head position.

3. Move the disk arm in the direction of the first request.

4. Service the requests along the way.

5. If there are no more requests in the direction of the first request, move the disk arm to the other end of the disk.

6. Service the requests along the way.

7. Repeat steps 5 and 6 until all requests have been serviced.



