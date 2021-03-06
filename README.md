# python-exercises

1.    [ctypes] Get the process name from a process ID (CreateToolhelp32Snapshot, TH32CS_SNAPPROCESS, szExeFile).

2.    [net] Write a client / server pair of sources in which the client requests random numbers of a specific number of digits from the server.

3.    [re] Extract all ASCII strings of length >= 4 from a file (e.g. executable).

4.    [re] Find all URLs and / or email addresses in a text file.

5.    [sound] Play the first 9 notes of Beethoven's "Fur Elise" (E D# E D# E B D C A) - check with https://onlinesequencer.net/ (modules: winsound / pygame.midi).

6.    [images] Render & save the Julia fractal as a PNG.
7.    [lang] Create functions which:
        a. Compute the factorial of an integer.
        b. Check if a number is prime.
        c. Compute the greatest common divisor of two numbers.
        d. Convert a string to uppercase.
        e. Caesar-encrypt (ROT3) a string.
        f. Multiply a matrix (given as a list of rows) by a scalar value. e.g.: matrix of 3 rows, 2 columns: A = [[1, 2], [3, 4], [5, 6]] multiplied by 2 => [[2, 4], [6, 8], [10, 12]]
        g. Print the name and type of each global symbol with the following format:
            one entry per line
            name padded to the right to 10 with blanks, at most 10 characters
            colon (:)
            type (as returned by the type() function), truncated at 15 characters

        e.g.:

        a         :<type 'int'>
        __builtins:<type 'module'>
        __name__  :<type 'str'>
        __package_:<type 'NoneType
        [...]

8.    [net] Write a client-server application in which the client calls on the server to perform the operations in problem

9.    [encoding] Using the function randint(low, high) from the random module (find out what it does online), create a (global) dictionary mapping each lowercase letter of the alphabet to a unique 4-digit number (converted to string); print a multiline string encoded using this method. e.g.:

    s = '''a
        ab'''
    ENCODING = {'a':'1023', 'b':'7310', [...]}

    =>

    1023
    10237310

    Bonus poins: create a function which decodes such an encoded string. Can you use the same dictionary?

10.    [lang] Print all primes between 100000000000 and 100000010000 (inclusive) separated by semicolons (;).

11.    [lang] Find two coprime integers in the range 1e50..1e51.

12.    [lang] Multiply a matrix of M rows & N columns by a matrix of N rows & M columns.

13.    [re] Extract all user agents from an Apache log file (e.g. http://redlug.com/logs/access.log); count the number of appearances for each distinct version of each user agent. e.g. from this:

    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36"

    the actual user agent is Chrome version 41.0.2272.101, but for the sake of simplicity we can assume that the first thing that looks like a user agent + version may be used ("Mozilla 5.0" in this case).

14.    [parsing] Print the number of sections of a PE executable whose filename is given as a parameter to the script (module: struct).

15.    [lang] Create a generator function which returns the numbers from the Fibonacci sequence.

16.    [web] Write a minimal web server which accepts POST file uploads from an HTML form and saves the uploaded files XOR-encoded into a local folder (module: bottle). Expose the list of encoded files & allow downloading the original, unencoded files.

       Bonus points: include the file type (as returned by the file command) when listing stored files.

17.    [image] Render the Koch curve (fractal) in under 15 lines of code (module: turtle).

18.    [net] Write a script which takes as arguments an IP, a user and a password, connects to that IP as an FTP server and (recursively) copies all remote files to the current folder (module: ftplib).

19.    [net] Retrieve the definition (and, if available, the main image) from the Wikipedia page of a given item.

20.    [net] Download a video from a video sharing site (Dailymotion, Vimeo, YouTube etc.).

21.    [net] Given any show name (e.g. "The Simpsons") and a season / episode number, print the episode name and a brief description (use an online database, e.g. imdb.com or epguides.com).

22.    [os] Find duplicate files in a given folder + subfolders and automatically append the extension .dup (if not already present) to all but the first appearance (modules: os, hashlib).
