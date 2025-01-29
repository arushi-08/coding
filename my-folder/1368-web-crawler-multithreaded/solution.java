/**
 * // This is the HtmlParser's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface HtmlParser {
 *     public List<String> getUrls(String url) {}
 * }
 */
class Solution {
    private Set<String> visited;
    private String hostName;
    private HtmlParser htmlParser;

    public List<String> crawl(String startUrl, HtmlParser htmlParser) {
        visited = ConcurrentHashMap.newKeySet(); // new
        hostName = startUrl.replace("http://", "").split("/")[0];
        this.htmlParser = htmlParser;
        crawlR(startUrl);
        return new ArrayList<>(visited);
    }
    private void crawlR(String startUrl){
        String currentHost = startUrl.replace("http://", "").split("/")[0];
        if (visited.contains(startUrl) || !hostName.equals(currentHost)) return;
        visited.add(startUrl);
        this.htmlParser.getUrls(startUrl).parallelStream().forEach(this::crawlR); // new
    }
}
