import multiprocessing

# Function to be applied to each element of the list
def square_list(chunk):
    return [x * x for x in chunk]

if __name__ == "__main__":
    # Input list
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Number of processes to spawn
    num_processes = multiprocessing.cpu_count()

    # Split the input list into chunks for each process
    chunk_size = len(input_list) // num_processes
    chunks = [input_list[i:i+chunk_size] for i in range(0, len(input_list), chunk_size)]

    # Create a multiprocessing pool
    pool = multiprocessing.Pool(processes=num_processes)

    # Apply the function to each chunk in parallel using map function
    result_chunks = pool.map(square_list, chunks)

    # Flatten the result_chunks list
    results = [item for sublist in result_chunks for item in sublist]

    # Close the pool
    pool.close()
    pool.join()

    # Print the results
    print("Input list:", input_list)
    print("Squared list:", results)
