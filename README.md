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

