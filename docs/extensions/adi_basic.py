###############################################################################
## Copyright (C) 2023 Analog Devices, Inc. All rights reserved.
### SPDX short identifier: ADIBSD
###############################################################################

import os.path
from docutils import nodes
from docutils.statemachine import ViewList
from docutils.parsers.rst import Directive, directives
from sphinx.util.nodes import nested_parse_with_titles
from sphinx.util import logging
from uuid import uuid4
from hashlib import sha1
from adi_basic_static import basic_strings
import contextlib
import re

logger = logging.getLogger(__name__)

dft_hide_collapsible_content = True

class node_base(nodes.Element, nodes.General):
	"""
	Adapted from
	https://github.com/pradyunsg/sphinx-inline-tabs
	https://github.com/dgarcia360/sphinx-collapse
	"""

	@staticmethod
	def visit(translator, node):
		attributes = node.attributes.copy()

		attributes.pop("ids")
		attributes.pop("classes")
		attributes.pop("names")
		attributes.pop("dupnames")
		attributes.pop("backrefs")

		text = translator.starttag(node, node.tagname, **attributes)
		translator.body.append(text.strip())

	@staticmethod
	def depart(translator, node):
		if node.endtag:
			translator.body.append(f"</{node.tagname}>")

	@staticmethod
	def default(translator, node):
		pass

class node_div(node_base):
	tagname = 'div'
	endtag = 'true'

class node_input(node_base):
	tagname = 'input'
	endtag = 'false'

class node_label(node_base):
	tagname = 'label'
	endtag = 'true'

class node_icon(node_base):
	tagname = 'div'
	endtag = 'false'

class node_video(node_base):
	tagname = 'video'
	endtag = 'true'

class node_source(node_base):
	tagname = 'source'
	endtag = 'false'

class node_iframe(node_base):
	tagname = 'iframe'
	endtag = 'false'

class directive_base(Directive):
	has_content = True
	add_index = True
	current_doc = ''
	final_argument_whitespace = True

	def collapsible(self, section, text=""):
		env = self.state.document.settings.env

		_id = sha1(text.encode('utf-8')).hexdigest()
		container = nodes.container(
			"",
			is_div=True,
			classes=['collapsible']
		)
		checked = {"checked": ''} if not env.config.hide_collapsible_content else {}
		input_ = node_input(
			type="checkbox",
			**checked,
			ids=[_id],
			name=_id,
			classes=['collapsible_input']
		)
		label = node_label(
			**{"for": _id}
		)
		icon = node_icon(
			classes=['icon']
		)
		content = nodes.container(
			"",
			is_div=True,
			classes=['collapsible_content']
		)
		label += nodes.paragraph(text=text)
		label += icon

		container += input_
		container += label
		container += content

		section += container

		return (content, label)

class directive_collapsible(directive_base):
	option_spec = {'path': directives.unchanged}
	required_arguments = 1
	optional_arguments = 0

	def run(self):
		self.assert_has_content()

		env = self.state.document.settings.env
		self.current_doc = env.doc2path(env.docname)

		node = node_div()

		content, _ = self.collapsible(node, self.arguments[0].strip())
		self.state.nested_parse(self.content, self.content_offset, content)

		return [ node ]

class directive_video(directive_base):
	option_spec = {'path': directives.unchanged}
	required_arguments = 1
	optional_arguments = 0

	yt_pattern = r'(https?://)?(www\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]+)'
	def run (self):
		url = self.arguments[0].strip()

		yt_match = re.search(self.yt_pattern, url)
		if yt_match:
			node = node_div(
				classes=['iframe-video']
			)
			yt_id = yt_match.group(3)
			iframe = node_iframe(
				src=f"https://www.youtube-nocookie.com/embed/{yt_id}"
			)
			node += iframe
		else:
			node = node_div()
			video = node_video(
				controls="controls"
			)
			source = node_source(
				type="video/mp4",
				src=url
			)
			video += source
			node += video

		return [ node ]

class directive_esd_warning(directive_base):
	option_spec = {'path': directives.unchanged}
	required_arguments = 0
	optional_arguments = 0

	def run(self):
		node = node_div()
		container = nodes.container(
			"",
			is_div=True,
			classes=['esd_warning']
		)
		icon = node_icon(
			classes=['icon']
		)
		container += icon
		container += nodes.paragraph(text=basic_strings.esd_warning)
		node += container

		return [ node ]

def setup(app):
	app.add_directive('collapsible', directive_collapsible)
	app.add_directive('video',       directive_video)
	app.add_directive('esd_warning', directive_esd_warning)

	for node in [node_div, node_input, node_label, node_icon, node_video, node_source, node_iframe]:
		app.add_node(node,
				html =(node.visit, node.depart),
				latex=(node.visit, node.depart),
				text =(node.visit, node.depart))

	app.add_config_value('hide_collapsible_content', dft_hide_collapsible_content, 'env')

	return {
		'version': '0.1',
		'parallel_read_safe': True,
		'parallel_write_safe': True,
	}
