class HTMLNode:
    def __init__(self, tag: str | None = None, value: str | None = None, children: list["HTMLNode"] | None = None, props: dict[str, str] | None = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self) -> str:

        ret_str = ""

        if self.props == None:
            return ""

        for prop in self.props:
            ret_str += f' {prop}="{self.props[prop]}"'

        return ret_str

    def __repr__(self) -> str:
            return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str, props: dict[str, str] | None = None) -> None:
        super().__init__(tag, value, None, props)
        self.tag = tag
        self.value = value
        self.props = props         

    def to_html(self) -> str:
            if self.value is None:
                 raise ValueError("Invalid HTML - no Value is set")

            if self.tag is None:
                 return f'{self.value}'

            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
            return f"LeafNode({self.tag}, {self.value}, {self.props})"
    