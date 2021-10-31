# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# https://generatedata.com/generator

# %%
name = "Abigail"
print(name)
print(len(name))
print(name[0:3])  # Slice
print(name[0:7])
print(name[2:6])
print(name[:3])
print(name[3:])


# %%
file1 = open("RandomData-10.csv", "r")
data = file1.readlines()
file1.close()


# %%
print(data)


# %%
print(data[0])
print(data[1])


# %%
for row in data:
    print(row)


# %%
for row in data:
    print(row[0 : len(row) - 1])


# %%
name = data[1].split(",")[0]
print(name)


# %%
name = data[1].split(",")[0]
grade = data[1].split(",")[1]
age = data[1].split(",")[2]
color = data[1].split(",")[3]

print(name)
print(grade)
print(age)
print(color)
