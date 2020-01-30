import unittest
from matching_helper import get_matching_patterns

# run tests by running <python test_pattern_matching_paths.py> in the terminal
class TestPatternMatchingPaths(unittest.TestCase):

    def test_base_case(self):
        patterns = ["*,b,*","a,*,*", "*,*,c", "foo,bar,baz", "w,x,*,*", "*,x,y,z"]
        paths = ["/w/x/y/z/", "a/b/c", "foo/", "foo/bar/", "foo/bar/baz/"]
        self.assertEqual(get_matching_patterns(patterns, paths), ["*,x,y,z", "a,*,*", "NO MATCH", "NO MATCH", "foo,bar,baz"], "Should be ['*,x,y,z', 'a,*,*', 'NO MATCH', 'NO MATCH', 'foo,bar,baz']")

    def test_one_match(self):
        patterns = ["a,b,c,e", "a,b,e,c" , "a,b,d,e"]
        paths = ["a/b/c/e"]
        self.assertEqual(get_matching_patterns(patterns, paths), ["a,b,c,e"], "Should be ['a,b,c,e'] ")

    def test_no_matches(self):
        patterns = ["a,*,z,e", "*,f,e,c" , "a,q,d,*"]
        paths = ["/h/i/j/k/"]
        self.assertEqual(get_matching_patterns(patterns, paths), ["NO MATCH"], "Should be ['NO MATCH'] ")

    def test_min_wildcards(self):
        patterns = ["w,x,*,*", "*,x,y,z"]
        paths = ["/w/x/y/z/"]
        self.assertEqual(get_matching_patterns(patterns, paths), ["*,x,y,z"], "Should be ['*,x,y,z'] ")

    def test_leftmost_wildcard(self):
        patterns = ["*,b,*", "*,*,c"]
        paths = ["a/b/c"]
        self.assertEqual(get_matching_patterns(patterns, paths), ["*,b,*"], "Should be ['*,b,*'] ")

    def test_no_patterns(self):
        patterns = []
        paths = ["/w/x/y/z/", "a/b/c", "foo/", "foo/bar/", "foo/bar/baz/"]
        self.assertEqual(get_matching_patterns(patterns, paths), ["NO MATCH"], "Should be ['NO MATCH']")

    def test_no_paths(self):
        patterns = ["*,b,*","a,*,*", "*,*,c", "foo,bar,baz", "w,x,*,*", "*,x,y,z"]
        paths = []
        self.assertEqual(get_matching_patterns(patterns, paths), ["NO MATCH"], "Should be ['NO MATCH']")

    def test_no_patterns_or_paths(self):
        patterns = []
        paths = []
        self.assertEqual(get_matching_patterns(patterns, paths), ["NO MATCH"], "Should be ['NO MATCH']")


if __name__ == "__main__":
    unittest.main()
    print("Everything passed")