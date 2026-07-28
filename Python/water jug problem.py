jug1 = 0   # 4 L Jug
jug2 = 0   # 3 L Jug

print("Initial State:", (jug1, jug2))

# Step 1: Fill Jug 2 (3 L)
jug2 = 3
print("Fill Jug2:", (jug1, jug2))

# Step 2: Pour Jug2 into Jug1
jug1 = jug2
jug2 = 0
print("Pour Jug2 -> Jug1:", (jug1, jug2))

# Step 3: Fill Jug2 again
jug2 = 3
print("Fill Jug2:", (jug1, jug2))

# Step 4: Pour Jug2 into Jug1 until Jug1 is full
space = 4 - jug1
jug1 = 4
jug2 = jug2 - space
print("Pour Jug2 -> Jug1:", (jug1, jug2))

# Goal achieved
print("Target Achieved:", jug2, "Litres in Jug2")
