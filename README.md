# **Subdirectory Finder**

This is a Python script for finding subdirectories on a website. It takes a list of subdomains, tries various file extensions, and recursively searches for subdirectories up to a specified depth.

# **Usage**
```python
python subdirectory_finder.py <url> <subdomains_file> [-h] [-e EXTENSIONS [EXTENSIONS ...]][-d DEPTH] [-u USER_AGENT] [-p PROXY] [-a USERNAME PASSWORD] 
```
The script takes the following arguments:

- url - The URL of the website to search
- subdomains\_file - The path to a file containing a list of subdomains to search for
- -e, --extensions - Optional. The extensions to try (default is "", meaning no extension)
- -d, --depth - Optional. The maximum depth to search (default is 3)
- -u, --user-agent - Optional. The user agent string to use for HTTP requests
- -p, --proxy - Optional. The HTTP proxy server to use for HTTP requests
- -a, --auth - Optional. The HTTP authentication credentials to use for HTTP requests (format: USERNAME PASSWORD)
# **Installation**
```
git clone
pip3 install -r requirements.txt
cd subfinder
```
# **Examples**
```python
python subdirectory_finder.py https://example.com subdomains.txt -e php -d 5 -u Mozilla/5.0 -p http://127.0.0.1:8080 -a admin password
```
