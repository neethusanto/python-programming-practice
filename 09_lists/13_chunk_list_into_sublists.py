"""
Q13: Split a list into evenly sized sublists/chunks of size K.
"""

def chunk_list(items, chunk_size):
    chunks = []
    current_chunk = []
    for item in items:
        current_chunk.append(item)
        if len(current_chunk) == chunk_size:
            chunks.append(current_chunk)
            current_chunk = []
    if current_chunk:
        chunks.append(current_chunk)
    return chunks

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Chunks of size 3:", chunk_list(arr, 3))
