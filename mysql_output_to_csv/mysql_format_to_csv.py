input_file = open("input")
output_file = open("output.csv", "w")

while True:
    line = input_file.readline()
    if not line:
        break

    chunks = line.split("|")
    if len(chunks) >= 2:
        animal = chunks[1].strip()
        peso = chunks[2].strip()
        output_file.write("{},{}\n".format(animal, peso))

input_file.close()
output_file.close()
