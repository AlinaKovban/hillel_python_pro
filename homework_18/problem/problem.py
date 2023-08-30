# All comments below is what I done in half on hour

# altitude = [1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 7, 5, 5, 8, 8, 2]

# hollow = [None, None, None, 1, None, 1, None, 1, None, 0, 1, 5, None, None, None, None, None]

# def max_hollow(altitude, hollow):
#     hollow_size = []
#     for i in altitude:
#         for j in hollow:
#             if j != None:
#                 size = i - j
#             else:
#                 size = 0
#     return hollow_size.append(size)
    
# print (max_hollow(altitude, hollow))


# All below is my solution what I done in 1,5 hours

def max_hollow(altitude, hollow):
    hollow_size = []
    for i in range(len(altitude)):
        if hollow[i] is not None:
            if isinstance(hollow[i], list):
                size = altitude[i]
                for element in hollow[i]:
                    new_size = size - element
                    hollow_size.append(new_size)
            else:
                size = altitude[i] - hollow[i]
                hollow_size.append(size)
        else:
            size = 0
            hollow_size.append(size)
    return max(hollow_size)


altitude = [1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 7, 5, 5, 8, 8, 2]

hollow = [None, None, None, [1, 0], None, 1, None, [1, 0], None, 0, [1, 0], 5, None, None, None, None, None]

print (max_hollow(altitude, hollow))
