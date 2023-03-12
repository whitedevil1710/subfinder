import argparse
import requests
from termcolor import colored

print(colored("""

░██████╗██╗░░░██╗██████╗░███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
██╔════╝██║░░░██║██╔══██╗██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
╚█████╗░██║░░░██║██████╦╝█████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
░╚═══██╗██║░░░██║██╔══██╗██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
██████╔╝╚██████╔╝██████╦╝██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
╚═════╝░░╚═════╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝
--------------c̶o̶d̶e̶d̶ b̶y̶:̶ w̶h̶i̶t̶e̶d̶e̶v̶i̶l̶----------------------------------
""", "blue"))
try:
	def find_subdirs(url, subdomains, extensions, depth, user_agent=None, proxy=None, auth=None):
	    session = requests.Session()
	    if user_agent:
	        session.headers.update({"User-Agent": user_agent})

	    if proxy:
	        session.proxies = {"http": proxy, "https": proxy}

	    if auth:
	        session.auth = auth

	    try:
	        response = session.get(url)
	        response.raise_for_status()
	    except requests.exceptions.RequestException as e:
	        print(colored("Error: Unable to connect to URL", "red"))
	        return

	    base_url = response.url

	    for subdomain in subdomains:
	        subdir = f"{subdomain}/"
	        for i in range(depth):
	            for ext in extensions:
	                subdir_url = f"{base_url}{subdir}{ext}"
	                try:
	                    response = session.get(subdir_url)
	                    if response.status_code == 200:
	                        print(colored(f"Found: {subdir_url}", "green"))
	                    else:
	                        print(colored(f"Not found: {subdir_url}", "yellow"))
	                except requests.exceptions.RequestException:
	                    print(colored(f"Error: Unable to connect to {subdir_url}", "red"))
	            subdir += subdir + f"{subdomain}/"
	
	if __name__ == "__main__":
	    parser = argparse.ArgumentParser(description="Find subdirectories of a website")
	    parser.add_argument("url", help="The URL of the website to search")
	    parser.add_argument("subdomains_file", help="The file containing subdomains to search for")
	    parser.add_argument(
	        "-e", "--extensions", nargs="+", default=[""], help="The extensions to try"
	    )
	    parser.add_argument(
	        "-d",
	        "--depth",
	        type=int,
	        default=3,
	        help="The maximum depth to search",
	    )
	    parser.add_argument(
	        "-u",
	        "--user-agent",
	        help="The user agent string to use for HTTP requests",
	    )
	    parser.add_argument(
	        "-p",
	        "--proxy",
	        help="The HTTP proxy server to use for HTTP requests",
	    )
	    parser.add_argument(
	        "-a",
	        "--auth",
	        nargs=2,
	        metavar=("USERNAME", "PASSWORD"),
	        help="The HTTP authentication credentials to use for HTTP requests",
	    )
	    args = parser.parse_args()
	
	    auth = None
	    if args.auth:
	        auth = tuple(args.auth)
	
	    with open(args.subdomains_file) as f:
	        subdomains = [line.strip() for line in f]
	
	    find_subdirs(
	        args.url,
	        subdomains,
	        args.extensions,
	        args.depth,
	        user_agent=args.user_agent,
	        proxy=args.proxy,
	        auth=auth,
	    )
except KeyboardInterrupt:
	print("Exit")
