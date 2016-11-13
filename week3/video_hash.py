from Crypto.Hash import SHA256

# Calculate blocked hash of a video file using SHA256


def bytes_from_file(filename, chunksize):
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                yield chunk
            else:
                break


def calculate_hash(video_chunks):
    for i in range(len(video_chunks)-1, 0, -1):
        video_chunks[i-1] += SHA256.new(video_chunks[i]).digest()

    return SHA256.new(video_chunks[0]).hexdigest()


if __name__ == "__main__":
    print(calculate_hash(list(bytes_from_file('video.mp4', 1024))))

