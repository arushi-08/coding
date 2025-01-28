# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
    
        host_name = startUrl.replace('http://', '').split('/')[0]
        next_links = [startUrl]
        ans = [startUrl]
        visited = set([startUrl])
        visited_lock = threading.Lock()
        
        with ThreadPoolExecutor(max_workers=100) as pool:
        
            while next_links :
                future_to_url = {pool.submit(htmlParser.getUrls, url):url for url in next_links}
                next_links = []

                for future in as_completed(future_to_url):
                    url = future_to_url[future]
                    new_links = future.result()
                        
                    for cand in new_links:
                        cand_host_name = cand.replace('http://', '').split('/')[0]
                        if cand_host_name == host_name:
                            with visited_lock:
                                if cand not in visited:
                                    next_links.append(cand)
                                    ans.append(cand)
                                    visited.add(cand)
                    
        return list(ans)


# assume we have 10k servers and 10^9 urls to crawl.
# we deploy the same code on each server
# the code can know about all the other servers.
# aim: minimize communication between machines and make sure each node does equal work
# how would design change?

# for equal load - equal num of urls crawled / server -> 10^9/10^4 = 100k urls/server
# 1 server - 100 threads - 1k urls/thread - best case 

# for minimizing communication between servers, 
# we can do bfs
# the urls can be distributed across servers based on the level of the bfs search + till the limit of the urls/server is reached.
# Start with server 1:
# Call {pool.submit(htmlParser.getUrls, url):url for url in next_links}
# Perform next steps i.e. as_completed
# If we reach the limit of urls crawled on current server, we send the next urls to next server
# this is done asynchronously, and we continue executing on current server.
# Finally we wait for all servers' results and combine them
# visited_lock is applied for each server.


"""
Hash-Based Partitioning Over BFS Levels
BFS-level distribution can lead to hotspots if certain levels have vastly more URLs. Instead, use a consistent hash function (e.g., hash(url) % 10,000) to assign URLs to servers. This ensures:
Each URL is processed by exactly one server, eliminating duplication.
Natural load balancing if the hash distributes URLs evenly.
Local Queues with Direct Routing
Each server maintains its own queue of URLs it’s responsible for. When a server discovers new URLs:
Hash them: If the hash matches the current server, add to its local queue.
Route directly: If not, send the URL to the hashed server once. This minimizes redundant communication.
No Global Coordination for Visited URLs
Since URLs are partitioned by hash, each server only tracks its own visited set. No global locks or cross-server checks are needed.
Revised Design:

Initial Distribution
Hash all seed URLs to assign them to servers. Each server starts with URLs that hash to its ID.
Crawling Process
Each server processes its local queue (BFS/DFS doesn’t matter here; focus on URL ownership).
For each extracted URL:
Compute server_id = hash(url) % 10,000.
If server_id == self, add to local queue if unvisited.
Else, send the URL to server_id via asynchronous message (e.g., message queue).
Load Balancing
With a good hash function (e.g., SHA-256), each server gets ~100k URLs naturally.
If some servers finish early, implement work-stealing (optional, adds some communication) or rely on hash uniformity.
Why This Works Better:

Minimized Communication: URLs are only sent once to their owner server. No chaining ("next server") or global coordination.
No Duplicates: Hash-based ownership ensures no two servers process the same URL.
Scalability: Adding/removing servers can be handled via consistent hashing (if dynamic scaling is needed).
"""


"""
What if one node fails or does not work?

1. Replicate URL Assignments

Mechanism:
Assign each URL to N nodes (e.g., primary + backup) using a modified hash (e.g., hash(url) % 10,000 for primary, (hash(url) + offset) % 10,000 for backups).
If the primary node fails, the backup node takes over.
Pros:
Minimal communication: Only backup nodes receive URLs (no global coordination).
Fast failover.
Cons:
Slightly increased storage/processing (each URL is stored on N nodes).
Requires a lightweight failure detector (e.g., heartbeat).

2. Heartbeat + Hash Ring Redistribution

Mechanism:
Nodes periodically send heartbeats to a lightweight coordinator (or via gossip protocol).
If a node fails, its hash range is redistributed to adjacent nodes in the consistent hash ring.
New owner nodes reprocess URLs in the failed range (requires tracking unprocessed URLs).
Pros:
No replication overhead.
Works with existing consistent hashing.
Cons:
Reprocessing may cause duplicates if URLs were partially crawled.
Requires tracking unprocessed URLs (e.g., using Bloom filters).

"""
