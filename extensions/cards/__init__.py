from docutils import nodes
from sphinx.locale import get_translation
from sphinx.util.docutils import SphinxDirective


class Cards(SphinxDirective):
    """ Implement a `cards` directive as a Bootstrap `row`. """
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = True

    def run(self):
        """ Process the content of the directive.

        We use custom node classes to represent HTML elements (e.g., 'div') rather than the
        corresponding sphinx.nodes.* class (e.g., sphinx.nodes.container) to prevent automatically
        setting the name of the node as class (e.g., "container") on the element.
        """
        self.assert_has_content()

        div_row = Div(classes=['row'])

        self.state.nested_parse(self.content, self.content_offset, div_row)

        return [div_row]


class Card(SphinxDirective):
    """ Implement a `card` directive with Bootstrap's card component. """
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = True

    def run(self):
        """ Process the content of the directive.

        We use custom node classes to represent HTML elements (e.g., 'div') rather than the
        corresponding sphinx.nodes.* class (e.g., sphinx.nodes.container) to prevent automatically
        setting the name of the node as class (e.g., "container") on the element.
        """
        _ = get_translation('cards')
        self.assert_has_content()

        div_col = Div(classes=['col'])

        self.state.nested_parse(self.content, self.content_offset, div_col)

        return [div_col]


        # # Create the accordion item container.
        # accordion_item_container = Container(classes=['accordion-item'])
        # accordion_container.append(accordion_item_container)
        #
        # # Create the header.
        # header = Header(ids=[heading_id], classes=['accordion-header'])
        # accordion_item_container.append(header)
        #
        # # Create the toggle button.
        # button = Button(
        #     classes=[
        #         'accordion-button', 'collapsed', 'flex-row-reverse', 'justify-content-end',
        #         'fw-bold', 'p-0', 'border-bottom-0'
        #     ],
        #     **{
        #         'type': 'button',
        #         'data-bs-toggle': 'collapse',
        #         'data-bs-target': f'#{content_id}',
        #         'aria-expanded': 'false',
        #         'aria-controls': content_id,
        #     }
        # )
        # header.append(button)
        #
        # # Create the button label.
        # label = self.arguments[0] if self.arguments else _("Spoiler")
        # button_label = nodes.Text(label)
        # button.append(button_label)
        #
        # # Create the accordion collapse container.
        # accordion_collapse_container = Container(
        #     ids=[content_id],
        #     classes=['accordion-collapse', 'collapse', 'border-bottom-0'],
        #     **{'aria-labelledby': heading_id},
        # )
        # accordion_item_container.append(accordion_collapse_container)
        #
        # # Create the accordion body container.
        # accordion_body_container = Container(classes=['accordion-body'])
        # self.state.nested_parse(self.content, self.content_offset, accordion_body_container)
        # accordion_collapse_container.append(accordion_body_container)
        #
        # return [accordion_container]


class Div(nodes.General, nodes.Element):
    custom_tag_name = 'div'


# class Header(nodes.General, nodes.Element):
#     custom_tag_name = 'span'


# class Button(nodes.General, nodes.Element):
#     custom_tag_name = 'button'


def visit_node(translator, node):
    custom_attr = {k: v for k, v in node.attributes.items() if k not in node.known_attributes}
    translator.body.append(translator.starttag(node, node.custom_tag_name, **custom_attr).rstrip())


def depart_node(translator, node):
    translator.body.append(f'</{node.custom_tag_name}>')


def setup(app):
    app.add_directive('cards', Cards)
    app.add_directive('card', Card)
    app.add_node(Div, html=(visit_node, depart_node))
    # app.add_node(Header, html=(visit_node, depart_node))
    # app.add_node(Button, html=(visit_node, depart_node))
    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
