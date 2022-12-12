with open("day6.txt", "r") as f:
    data = f.read()

start = 0
end = 14
sliding_window = True

while sliding_window:
    chunk = data[start:end]
    chunk_set = list(set(chunk))

    if len(chunk) == len(chunk_set):
        print(f"Marker: {end}")
        sliding_window = False
    
    start += 1
    end += 1

    if start >= len(data):
        sliding_window = False


