# Technical Task

## Prerequisites
This solution has been tested using Python 2.7 on Mac OSX 10.12 and Python 2.7 running within an Alpine Docker container.  
**Requirements**: Python 2.x or Docker

## Part 1 - Postcode validation
### Running Postcode Validator 
Using Python
`python part1_simpleValidator.py` (Tested on Python 2.7)  
OR  
If you do not have Python installed, you can run the script using a Python container in Docker: `docker run -v $(PWD):/tmp/ -w /tmp python:2.7-alpine time python /tmp/part1_simpleValidator.py`

### Analysis of Regex
In order to use the supplied Regular expression, the comments of whitespacing was removed.  

The test data supplied did not check all cases of postcodes accepted within the UK. There are additional postcode combinations that do not match the regex, but are genuine UK postcodes.   
The regex does not match against:  
1. some *Overseas* UK territories, such as the Falklands, however it does match against Gibraltar.   
2. any *BFPO* (British Forces Post Office) postcodes.   
3. some *Special* / *semi-mnemonic* postcodes - such as `W1N 4DJ` for **BBC Broadcast House**.

Testing of these cases can be found by running `python part1_specialPostcodeTesting.py`

## Part 2 - Bulk import
This script outputs a file called `failed_validation.csv`.
The script expects a file called `input_data.csv.gz` to be a gzip compressed csv, containing lines with two comma separated columns (`row_id` and `postcode`) to be in the same folder.  
*Note: Uncompressed CSV files can also be used.*

### Running Postcode Validator - Failed Postcodes
First, download the [input_data.csv.gz](https://drive.google.com/file/d/0BwxZ38NLOGvoTFE4X19VVGJ5NEk/view?usp=sharing) if it does not already exist in the root folder.  
Using Python
`python part2_bulkImport.py ` (Tested on Python 2.7)  
OR  
If you do not have Python installed, you can run the script using a Python container in Docker: `docker run -v $(PWD):/tmp/ -w /tmp python:2.7-alpine python /tmp/part2_bulkImport.py`

## Part 3 - Performance engineering

Performance testing was carried out on a single Laptop (Macbook 2.5Ghz i5, 16GB RAM, SSD Storage). To keep results accurate, all unused programs were closed.  
Testing was carried out 3 times in each scenario, to reduce outliers and to identify any sporadic results.  
The testing was done using [ test data from google drive](https://drive.google.com/file/d/0BwxZ38NLOGvoTFE4X19VVGJ5NEk/view?usp=sharing), which contains over 2 million postcodes.

### Running Postcode Validator - Passed/Failed Sorted Output:
First, download the [input_data.csv.gz](https://drive.google.com/file/d/0BwxZ38NLOGvoTFE4X19VVGJ5NEk/view?usp=sharing) file, if not already downloaded.  
Execute using: `time python part3_outputValidated.py` - This gives the running duration in seconds which have been recorded in the table below between each change. A brief change description and commit hash is included for each change. Changes can be re-tested by checking out the specific commit. 
Testing was verified by checking the contents of the two output files **passed_validation.csv** and **failed_validation.csv**

### Test results:


| Commit | Description of change | Timings |
|--------|-----------------------|---------|
| bc2d9f0fb3fe8cfb57b84ee234531ef52354381b | *Start Point* | 28.23s 28.48s 29.03s |
| c0ab8c33a41fede5b65c2b16c1dd12411dfbd258 | Debugging output to Stdout removed | 24.69s 25.21s 24.81s |
| c6d350991fedda88fcf373274b5a087a88303232 | Replace Regex with the alternative regex found on the UK Postcode Wiki page (different results given - Test failed) | 25.32s **[VOID - Failed]** |
| 558f1881f6b69fa89880a8434ccda0a25ef9e9fb | Read in a CSV file that isnt GZip compressed | 25.16s 25.21s 25.07s |
| ca7867f683c893678598b261b0174710b7a9f4d0 | Rearrange Regex so that checking for `GIR 0AA` is at the end of the Regex | 24.93s 25.01s 24.74s
| 2fb3a6cd06f184d84cdd8989b2b0f1678702af61 | Change to the sorting key definition for natural sorting of output files. Remove regex on key extraction and replace with split. | 13.15s 13.36s 13.30s |
| f8ca5375025c180a3f32fff3430ce656cad3772f | Write array of lines to file, rather than iterating over the lines | 12.66s 12.48s 12.52s

### Testing/Performance Analysis
During the initial testing, the execution time was 28.58 seconds on average. After a number of changes the execution time was significantly reduced to 12.55 seconds, less than half the original time.  
Changes were made incrementally to ensure that even small changes could be captured, allowing fine tuning to give the optimum running time.
The first change was to turn off the stdout logging, which reduced the time by approximately 4 seconds, however the biggest reduction was made by changing the sorting functionality to reduce its use of regex. 

### Future Enhancements
1. **User-defined input/output files** - Allow users to specify an input and/or output files when executing the postcode validation script. Input files could be remote or relative to the script location, and GZip compression can be automatically detected (without user specifying)
2. **Multithreaded processing** - The current script processes over 2 million entries in less than 13 seconds. If this was regularly used for larger datasets then loading the data as chunks and processing them in parallel through the regular expression functions to detect their validity would speed up the process, where required. 
3. **Logging** - Additional logging to file could later be used to generate statistics on average runtime, failed/successful matches and average execution time. This data cab be used to highlight problems with incoming data or issues in the process.

### Unit Testing
Unit testing can be executed by running `python testing.py -b`  
These tests execute using PyUnit and cover the functionality in the two custom imports (File handling and validation matching imports).  
Two small additional files (test_data.csv and test_data.csv.gz) are including in the repo for the purposes of unit testing.

