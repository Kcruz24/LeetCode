from typing import List


class HtmlParser(object):
   def getUrls(self, url):
       """
       :type url: str
       :rtype List[str]
       """


class Solution:
    # O(N) Time | O(N) Space
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:

        def dfs(url: str) -> None:
            for next_url in htmlParser.getUrls(url):
                next_hostname = next_url.split('//')[1].split('/')[0]
                if hostname != next_hostname:
                    continue

                if next_url in visited:
                    continue

                all_urls.append(next_url)
                visited.add(next_url)
                dfs(next_url)

        hostname = startUrl.split('//')[1].split('/')[0]
        visited = set([startUrl])
        all_urls = [startUrl]

        dfs(startUrl)

        return all_urls


class Solution:
    # O(N) Time | O(N) Space
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:

        hostname = startUrl.split('//')[1].split('/')[0]
        visited = set([startUrl])
        all_urls = [startUrl]

        stack = [startUrl]
        while stack:
            url = stack.pop()

            for neighbor_url in htmlParser.getUrls(url):
                next_domain = neighbor_url.split('//')[1].split('/')[0]

                if hostname != next_domain:
                    continue

                if next_domain in visited:
                    continue

                visited.add(next_domain)
                all_urls.append(next_domain)
                stack.append(next_domain)

        return all_urls


'''

output:
[
 "http://psn.wlyby.edu/upkr",
 "http://psn.wlyby.edu/apgb",
 "http://psn.wlyby.edu/inmj",
 "http://psn.wlyby.edu/shez",
 "http://psn.wlyby.edu/ubmr",
 "http://psn.wlyby.edu/wvoz"]

Expected:
["http://psn.wlyby.edu/apgb",
 "http://psn.wlyby.edu/inmj",
 "http://psn.wlyby.edu/shez",
 "http://psn.wlyby.edu/ubmr",
 "http://psn.wlyby.edu/wvoz"]

'''
x = 'http://news.yahoo.com/news/topics/'
y = x.split('//')
x = y[1].split('/')
hostname = x[0]
print(hostname)
print(x)
