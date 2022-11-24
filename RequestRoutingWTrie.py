
class RouteTrieNode:
    def __init__(self):
        self.pages = {}
        self.is_valid_path = False
        self.handler = "404 Not Found"

class RouteTrie:
    def __init__(self):
        self.root = RouteTrieNode()
        self.root.handler = "Root Handler"

    def cleanup_input(self, path):
        """
        Cleans up and breaks down input for easier insertion and lookup
        Does not rebuild, it would depend on method objectives

        Args:
            path(String): path to clean

        Returns:
            page_dir(Array): list of divided paths

        """

        # Removes first and last slashes if present
        if path[0] == '/':
            path = path[1:]

        if path[-1] == '/':
            path = path[:-1]

        # Separates the actual paths and saves to a list
        page_dirs = path.split('/')
        return page_dirs


    def insert(self, page, handler):
        """
        Adds RouteTrieNodes with a given page

        Args:
            page(String): page to add to RouteTrie
        """

        # Cleans up the input for easier insertion
        page_dirs = self.cleanup_input(page)

        current_node = self.root

        # Adds the web directories
        for page in page_dirs:

            # Rebuilds the path and add to pages if not already present
            page_path = "/" + page

            if page_path not in current_node.pages:
                current_node.pages[page_path] = RouteTrieNode()

            current_node = current_node.pages[page_path]

        current_node.is_valid_path = True
        current_node.handler = handler

    def find(self, path):
        """
        Given a path, it returns a handler for the page

        Args:
            path(String): Path to search down in
        Returns:
            handler(String): the handler for the page
        """

        # Handles invalid inputs
        if type(path) != str or path == "":
            return "400 Bad Request"

        page_to_find = self.cleanup_input(path)
        current_node = self.root

        # Iterate through the pages
        for page in page_to_find:

            # Recombine the page
            page_path = "/" + page

            # If page is not found, it will give an error
            if page_path not in current_node.pages.keys():
                return "404 Not Found"

            current_node = current_node.pages[page_path]

        return current_node.handler

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self):
        self.route_trie = RouteTrie()

    def add_handler(self, path, handler):
        self.route_trie.insert(path, handler)

    def lookup(self, path):

        # Handle case when searching for root page
        if path == "/":
            return self.route_trie.root.handler

        return self.route_trie.find(path)


# Create the router and add a route
router = Router()
router.add_handler("/home/about", "About Handler")
router.add_handler("/admin/login", "403 Forbidden")

# Test cases for lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print '404 Not Found'
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler'
print(router.lookup("/home/about/me")) # should print '404 Not Found'

# Other Test cases
print(router.lookup("/admin/login")) # should print '403 Forbidden'
print(router.lookup("admin/login/")) # should print '403 Forbidden'
print(router.lookup("/store")) # should print '404 Not Found'

# Test cases where inputs are unusual
print(router.lookup("")) # should print "400 Bad Request"
print(router.lookup(None)) # should print "400 Bad Request"
print(router.lookup(23)) # should print "400 Bad Request"
