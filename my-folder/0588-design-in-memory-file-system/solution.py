class Data:
    def __init__(self):
        self.children = {}
        self.content = ''
        self.is_file = False

class FileSystem:

    def __init__(self):
        self.root = Data()

    def _traverse(self, path):
        path_list = [p for p in path.split('/') if p]
        node = self.root

        for p in path_list:
            if p not in node.children:
                node.children[p] = Data()
            
            node = node.children[p]
        
        return node, path_list[-1] if path_list else ''

    def ls(self, path: str) -> List[str]:
        node, node_data = self._traverse(path)
        if node.is_file:
            return [node_data]
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self._traverse(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node, _ = self._traverse(filePath)
        node.is_file = True
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node, _ = self._traverse(filePath)
        return node.content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
