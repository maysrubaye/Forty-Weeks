from django.db import models
from django.http import HttpResponseRedirect

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.core import hooks
from poemsite import custom_blocks
from wagtail.search import index

class HomePage(Page):
    main_text = RichTextField(blank=True)
    sub_text = RichTextField(blank=True)
    scroll_text = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('main_text', blocks.RichTextBlock(required=False)),
        FieldPanel('sub_text', blocks.RichTextBlock(required=False)),
        FieldPanel('scroll_text', blocks.RichTextBlock(required=False))
    ]
    
class About(Page):
    main_text = RichTextField(blank=True)
    sub_text = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('main_text', blocks.RichTextBlock(required=False)),
        FieldPanel('sub_text', blocks.RichTextBlock(required=False))
    ]



class Poem(Page):
    semester_sent = RichTextField(blank=True)
    author = RichTextField(blank=True)
    body = StreamField([
        ('poem_body', blocks.RichTextBlock()
            )], null=True, blank=True)
    comments = RichTextField(blank=True)
    biography = RichTextField(blank=True)

    search_fields = Page.search_fields + [ # Inherit search_fields from Page
        index.SearchField('semester_sent', partial_match=True),
        index.SearchField('title', partial_match=True),
        index.SearchField('author', partial_match=True),
        index.SearchField('body', partial_match=True),
        index.SearchField('comments', partial_match=True),
        index.SearchField('biography', partial_match=True),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('semester_sent', blocks.RichTextBlock(required=False)),
        FieldPanel('author', blocks.RichTextBlock(required=False)),
        StreamFieldPanel('body', classname="full"),
        FieldPanel('comments', blocks.RichTextBlock(required=False)),
        FieldPanel('biography', blocks.RichTextBlock(required=False)),
        ]
