import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

    def test_eq2(self):
        node = TextNode("This is a link node", TextType.LINK, "www.boot.dev")
        node2 = TextNode("This is a link node", TextType.LINK, "www.boot.dev")
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        node2 = TextNode("This is a plain text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_noteq2(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        node2 = TextNode("This is a bold text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_noteq3(self):
        node = TextNode("This is a link node", TextType.LINK, "www.boot.dev")
        node2 = TextNode("This is a link node", TextType.LINK)
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()



