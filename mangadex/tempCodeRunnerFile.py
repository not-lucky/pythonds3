iprocessing.Pool(processes=4)

    # Map the list of URLs to the download_song function using the multiprocessing Pool
    # This will run the download_song function with each URL in parallel, using up to 4 processes at a time
    pool.map(do_the_thing, [U * 4])

    # Close the multiprocessing Pool to free up resources
    pool.close()
    pool.join()