from wagtail.core import blocks

class PoemBlock(blocks.StructBlock):
    """Title and text and nothing else."""
    title = blocks.RawHTMLBlock(required=False, help_text="Add your svg image")
    text = blocks.RichTextBlock(required=False, help_text="Add Hyperlink")
    class Meta:  # noqa
        template = "streams/poem_block.html"
        icon = "edit"
        label = "Poem Block"