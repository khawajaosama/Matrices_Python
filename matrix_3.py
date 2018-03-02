#FINDING THE KEY CONNECTORS

friendships = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
               [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

def key_connectors(user):
    return [friend+1 for friend,num in enumerate(friendships[user-1])
            if num==1]

print(key_connectors(6))