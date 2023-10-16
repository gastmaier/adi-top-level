.. _docs_guidelines:

Documentation guidelines
================================================================================

A brief set-of-rules for the documentation.

.. note::
   The old wiki uses `dokuwiki <https://www.dokuwiki.org/dokuwiki>`_. When
   importing text from there, consider the automated options that are provided
   in this page to convert it to reST.

Convert DokuWiki format to reST
--------------------------------------------------------------------------------

To convert from the DokuWiki format to reST, use pandoc:

.. code:: bash

   pandoc imported.txt -f dokuwiki -t rst --columns=80 -s -o imported.rst

Then, review it.

Path structure
--------------------------------------------------------------------------------

All user guides are stored in the user-guide folder, with each project assets
within its own folder, e.g. ``user-guide/adrv9009/*``.

To organize in categories, the user guide is included to the toctree at the proper
category in the categories folder, for example ADRV9009 is included in the toctree
of the file ``categories/transceiver-radio-boards.rst`` as:

.. code::

   ../user-guide/adrv9009/index

Notice the relative path.
New categories have to be included to the top ``index.rst`` and have it included
to the ``categories`` folder.

.. _git-lfs:

Git Large File Storage
--------------------------------------------------------------------------------

This repository uses Git Large File Storage (LFS) to replace large files with
text pointers inside Git, reducing cloning time.

To setup, install from your package manager and init:

.. code:: bash

   apt install git-lfs
   git lfs install

The files that will use Git LFS are tracked at ``.gitattributes``, to add new
files use a pattern at the repo root, for example:

.. code:: bash

   git lfs track *.jpg

Or edit ``.gitattributes`` directly.


Templates
--------------------------------------------------------------------------------

Templates are available:

Remove the ``:orphan:`` in the first line, it is to hide the templates from the
`TOC tree <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree>`_.

Indentation
--------------------------------------------------------------------------------

Directives are indented with 3 space, which is Sphinx's default.
At code directives, the code keeps its original indentation (e.g. 2 spaces for
verilog code), but is offset by 3 spaces at the beginning of every line, to
instruct Sphinx the beginning and end of the code directive.

References
--------------------------------------------------------------------------------

References have the label format ``context section``.

Prefer using hyphen ``-`` separation, for example, ``adrv9009 table-contents``
instead of ``adrv9009 table_contents``.
Also, keep the label concise and human friendly.

External references
--------------------------------------------------------------------------------

For references to other Sphinx documentations, the ``sphinx.ext.intershinx`` is used.
It has the syntax :code:`:ref:\`external:label\``,
e.g. :code:`:ref:\`hdl:spi_engine control-interface\`` renders as
:ref:`hdl:spi_engine control-interface`.
It is also possible to customize the text, e.g.
:code:`:ref:\`Custom text <hdl:spi_engine control-interface>\`` renders as
:ref:`Custom text <hdl:spi_engine control-interface>`.

When a external reference is not found, it will throw a warning.

To show all links of an Intersphinx mapping file, use:

.. code:: bash

   python -m sphinx.ext.intersphinx https://analogdevicesinc.github.io/hdl/objects.inv

Text width
--------------------------------------------------------------------------------

Each line must be less than 80 columns wide.

Tables
--------------------------------------------------------------------------------

Prefer
`list-tables <https://docutils.sourceforge.io/docs/ref/rst/directives.html#list-table>`_

Images
--------------------------------------------------------------------------------

Binary images (e.g. PNG, JPG) are stored in :ref:`git-lfs`.
For vectors, use SVG format saved as *Optimized SVG* in
`inkscape <https://inkscape.org/>`_ to use less space.

Third-party directives and roles
--------------------------------------------------------------------------------

Third-party tools are used to expand Sphinx functionality, if you haven't already,
do:

.. code:: bash

   pip install -r requirements.txt

Custom directives and roles
--------------------------------------------------------------------------------

To expand Sphinx functionality beyond existing tools, custom directives and roles
have been written, which are located in the *extensions* folder.
Extensions are straight forward to create, if some functionality is missing,
consider requesting or creating one.

.. note::

   Link-like roles use the :code:`:role:\`text <link>\`` synthax, like external
   links, but without the undescore in the end.


Color role
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To print text in red or green, use :code:`:red:\`text\`` and :code:`:green:\`text\``.

Link roles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The link roles are a group of roles defined by ``adi_links.py``.

The ``validate_links`` gloabl option is used to validate each link during build.
These links are not managed, that means, only links from changed files are checked.
You can run a build with it set to False, then touch the desired files to check
the links of only these files.

Git role
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The Git role allows to create links to the Git repository with a shorter syntax.
The role syntax is :code:`:git-repo:\`text <branch:path>\``, for example:

* :code:`:git-hdl:\`master:docs/user_guide/docs_guidelines.rst\``
  renders as :git-hdl:`master:docs/user_guide/docs_guidelines.rst`.
* :code:`:git-hdl:\`Guidelines <docs/user_guide/docs_guidelines.rst>\``
  renders as :git-hdl:`Guidelines <docs/user_guide/docs_guidelines.rst>`.

The branch field is optional and will be filled with the current branch.
The text field is optional and will be filled with the file or directory name.

Finally, you can do :code:`:git-repo:\`/\`` for a link to the root of the
repository with pretty naming, for example, :code:`:git-hdl:\`/\`` is rendered
as :git-hdl:`/`.

ADI role
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The adi role creates links for a webpage to the Analog Devices Inc. website.

The role syntax is :code:`:adi:\`text <webpage>\``, for example,
:code:`:adi:\`AD7175-2 <ad7175-2>\``.
Since links are case insensitive, you can also reduce it to
:code:`:adi:\`AD7175-2\``, when *webpage* is the same as *text* and will render
as :adi:`AD7175-2`.

Datasheet role
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The datasheet role creates links for a datasheet in the Analog Devices Inc. website.

The role syntax is :code:`:datasheet:\`part_id:anchor\``, for example,
:code:`:datasheet:\`AD7984:[{"num"%3A51%2C"gen"%3A0}%2C{"name"%3A"XYZ"}%2C52%2C713%2C0]\``
is rendered as
:datasheet:`AD7984:[{"num"%3A51%2C"gen"%3A0}%2C{"name"%3A"XYZ"}%2C52%2C713%2C0]`.
The anchor is optional and is a link to a section of the PDF, and can be obtained
by just copying the link in the table of contents.

.. caution::

   Since not all PDF readers support anchors, always provide the page and/or
   figure number!

Dokuwiki role
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The dokuwiki role creates links to the Analog Devices Inc. wiki website.
The role syntax is :code:`:dokuwiki:\`text <path>\``, for example,
:code:`:dokuwiki:\`pulsar-adc-pmods <resources/eval/user-guides/circuits-from-the-lab/pulsar-adc-pmods>\``
gets rendered as
:dokuwiki:`pulsar-adc-pmods <resources/eval/user-guides/circuits-from-the-lab/pulsar-adc-pmods>`.

EngineerZone role
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The ez role creates links to the Analog Devices Inc. EngineerZone support website.
The role syntax is :code:`:ez:\`community\``, for example, :code:`:ez:\`fpga\``
gets rendered as :ez:`fpga`.

Vendor role
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The vendor role creates links to vendors' website.
The role syntax is :code:`:vendor:\`text <path>\``, for example,
:code:`:xilinx:\`Zynq-7000 SoC Overview <support/documentation/data_sheets/ds190-Zynq-7000-Overview.pdf>\``
gets rendered
:xilinx:`Zynq-7000 SoC Overview <support/documentation/data_sheets/ds190-Zynq-7000-Overview.pdf>`.

The text parameter is optional, if absent, the file name will be used as the text,
for example,
:code:`:intel:\`content/www/us/en/docs/programmable/683780/22-4/general-purpose-i-o-overview.html\``
gets rendered
:intel:`content/www/us/en/docs/programmable/683780/22-4/general-purpose-i-o-overview.html`
(not very readable).

Supported vendors are: ``xilinx`` (AMD Xilinx), ``intel`` (Intel Altera) and
``mw`` (MathWorks).

Collapsible directive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The collapsible directive creates a collapsible/dropdown/"HTML details".

The directive syntax is:

.. code:: rst

   .. collapsible:: <label>

      <content>

For example:

.. code:: rst

   .. collapsible:: Python code example.

      .. code:: python

         print("Hello World!")

Renders as:

.. collapsible:: Python code example.

   .. code:: python

      print("Hello World!")

Notice how you can use any Sphinx syntax, even nest other directives.

The ``hide_collapsible_content`` global option is used to set the default state of
the collapsibles, if you set to False, they be expanded by default.

Video directive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The video directive creates a embedded video.
Currently, only direct MP4 are supported, but could be easily expanded to support
third-party services.

The directive syntax is:

.. code:: rst

   .. video:: <url>

For example:

.. code:: rst

   .. video:: http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4

Renders as:

.. video:: http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4


ESD warning directive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ESD warning directive creates a ESD warning, for example:

.. code:: rst

   .. esd_warning::

Renders as:

.. esd_warning::

