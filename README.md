# alexa-top-1000
Scans the Alexa top 1000 sites and analyze them.

The analysis includes:
Per Site
• Word count of the fist page and rank across all the sites based off the word count
• Duration of the scan

Across All Sites
• AVG word count of the first page
• Top 20 HTTP headers and the percentage of sites they were seen in
• Duration of the entire scan

## Usage
```
$ python alexa-top-1000.py
```

The number of sites scanned and headers analyzed can be set with command line flags.
```
$ python alexa-top-1000.py -s 200 -H 30
```
