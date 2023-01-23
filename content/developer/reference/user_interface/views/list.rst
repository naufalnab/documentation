List
====

The root element of list views is ``<tree>``\ [#treehistory]_. The list view's
root can have the following attributes:

.. rst-class:: o-definition-list

``editable``
    by default, selecting a list view's row opens the corresponding
    :ref:`form view <reference/user_interface/views/form>`. The ``editable`` attributes makes
    the list view itself editable in-place.

    Valid values are ``top`` and ``bottom``, making *new* records appear
    respectively at the top or bottom of the list.

    The architecture for the inline :ref:`form view <reference/user_interface/views/form>` is
    derived from the list view. Most attributes valid on a :ref:`form view
    <reference/user_interface/views/form>`'s fields and buttons are thus accepted by list
    views although they may not have any meaning if the list view is
    non-editable

    .. note:: if the ``edit`` attribute is set to ``false``, the ``editable`` option will be ignored.

``multi_edit``
    editable or not editable list can activate the multi-editing feature by defining
    the `multi_edit=1`

``default_group_by``
    whether the list view should be grouped if no grouping is specified via
    the action or the current search. Should be the name of the field to group
    by when no grouping is otherwise specified

``default_order``
    overrides the ordering of the view, replacing the model's order (:attr:`~odoo.models.BaseModel._order` model attribute).
    The value is a comma-separated list of fields, postfixed by ``desc`` to
    sort in reverse order:

    .. code-block:: xml

        <tree default_order="sequence,name desc">
            ...
        </tree>

``decoration-{$name}``
    allow changing the style of a row's text based on the corresponding
    record's attributes.

    ``{$name}`` can be ``bf`` (``font-weight: bold``), ``it``
    (``font-style: italic``), or any `bootstrap contextual color`_ (``danger``,
    ``info``, ``muted``, ``primary``, ``success`` or ``warning``).
``create``, ``edit``, ``delete``, ``import``, ``export_xlsx``
    allows *dis*\ abling the corresponding action in the view by setting the
    corresponding attribute to ``false``
``limit``
    the default size of a page. It must be a positive integer
``groups_limit``
    when the list view is grouped, the default number of groups of a page. It
    must be a position integer
``expand``
    when the list view is grouped, automatically open the first level of groups
    if set to true (default: false)

Possible children elements of the list view are:

.. _reference/user_interface/views/list/button:

.. rst-class:: o-definition-list

``button``
    displays a button in a list cell

   .. rst-class:: o-definition-list

    ``icon``
        icon to use to display the button
    ``string``
        * if there is no ``icon``, the button's text
        * if there is an ``icon``, ``alt`` text for the icon
    ``type``
        type of button, indicates how it clicking it affects Odoo:

        .. rst-class:: o-definition-list

        ``object``
            call a method on the list's model. The button's ``name`` is the
            method, which is called with the current row's record id and the
            current context.

            .. web client also supports a @args, which allows providing
               additional arguments as JSON. Should that be documented? Does
               not seem to be used anywhere

        ``action``
            load an execute an ``ir.actions``, the button's ``name`` is the
            database id of the action. The context is expanded with the list's
            model (as ``active_model``), the current row's record
            (``active_id``) and all the records currently loaded in the list
            (``active_ids``, may be just a subset of the database records
            matching the current search)
    ``name``
        see ``type``
    ``groups``
        lists the groups which should be able to see the button
    ``args``
        see ``type``
    ``invisible``
        standard dynamic attributes based on record values. Hide the field
        if trully or if the domain result is trully
    ``context``
        merged into the view's context when performing the button's Odoo call

    .. todo:: declared but unused: help

``field``
    defines a column where the corresponding field should be displayed for
    each record. Can use the following attributes:

    .. rst-class:: o-definition-list

    ``name``
        the name of the field to display in the current model. A given name
        can only be used once per view
    ``string``
        the title of the field's column (by default, uses the ``string`` of
        the model's field)
    ``invisible``
        standard dynamic attributes based on record values. Hide the field
        if trully or if the domain result is trully.

        Fetches and stores the field, but doesn't display the column in the
        table. Necessary for fields which shouldn't be displayed but are
        used by e.g. ``@colors`` or a domain.
    ``readonly``
        standard dynamic attributes based on record values. If the value is
        trully or the domain result is trully, display the field in both readonly
        and edit mode, but never make it editable
    ``required``
        standard dynamic attributes based on record values. If the value is
        trully or the domain result is trully, generates an error and prevents
        saving the record if the field doesn't have a value
    ``groups``
        lists the groups which should be able to see the field
    ``widget``
        alternate representations for a field's display. Possible list view
        values are (among others):

        .. rst-class:: o-definition-list

        ``progressbar``
            displays ``float`` fields as a progress bar.
        ``handle``
            for ``sequence`` (or ``integer``) fields by which records are
            sorted, instead of displaying the field's value just displays a
            drag&drop icon to reorder records.
    ``sum``, ``avg``
        displays the corresponding aggregate at the bottom of the column. The
        aggregation is only computed on *currently displayed* records. The
        aggregation operation must match the corresponding field's
        ``group_operator``
    ``width`` (for ``editable``)
        when there is no data in the list, the width of a column can be forced
        by setting this attribute. The value can be an absolute width (e.g.
        '100px'). Note that when there are records in the list, we let the
        browser automatically adapt the column's widths according to their
        content, and this attribute is thus ignored.
    ``decoration-{$name}``
        allow changing the style of a cell's text based on the corresponding
        record's attributes.

        ``{$name}`` can be ``bf`` (``font-weight: bold``), ``it``
        (``font-style: italic``), or any `bootstrap contextual color`_ (``danger``,
        ``info``, ``muted``, ``primary``, ``success`` or ``warning``).
    ``nolabel``
        if set to "1", the column header will remain empty. Also, the column
        won't be sortable.

    .. note::

        if the list view is ``editable``, any field attribute from the
        :ref:`form view <reference/user_interface/views/form>` is also valid and will
        be used when setting up the inline form view.

    .. note::

        In case of list sub-views (One2many/Many2many display in a form view),
        The attribute ``column_invisible`` can be useful to hide a column
        depending on the parent object.

        .. code-block:: xml

           <field name="product_is_late" column_invisible="[('parent.has_late_products', '=', False)]"/>

    .. note:: When a list view is grouped, numeric fields are aggregated and
              displayed for each group.  Also, if there are too many records in
              a group, a pager will appear on the right of the group row. For
              this reason, it is not a good practice to have a numeric field in
              the last column, when the list view is in a situation where it can
              be grouped (it is however fine for x2manys field in a form view:
              they cannot be grouped).

``groupby``
  defines custom headers (with buttons) for the current view when grouping
  records on many2one fields. It is also possible to add `field`, inside the
  `groupby` which can be used for modifiers. These fields thus belong on the
  many2one comodel. These extra fields will be fetched in batch.

  .. rst-class:: o-definition-list

  ``name``
      the name of a many2one field (on the current model). Custom header will be
      displayed when grouping the view on this field name.

  .. code-block:: xml

    <groupby name="partner_id">
      <field name="name"/> <!-- name of partner_id -->
      <button type="edit" name="edit" string="Edit"/>
      <button type="object" name="my_method" string="Button1"
        invisible="[('name', '=', 'Georges')]"/>
    </groupby>

  A special button (`type="edit"`) can be defined to open the many2one form view.

.. include:: header_buttons.rst

``control``
  defines custom controls for the current view.

  This makes sense if the parent ``tree`` view is inside a One2many field.

  Does not support any attribute, but can have children:

  .. rst-class:: o-definition-list

  ``create``
    adds a button to create a new element on the current list.

    .. rst-class:: o-definition-list

    .. note:: If any ``create`` is defined, it will overwrite the default
              "add a line" button.

    The following attributes are supported:

    .. rst-class:: o-definition-list

    ``string`` (required)
      The text displayed on the button.

    ``context``
      This context will be merged into the existing context
      when retrieving the default value of the new record.

      For example it can be used to override default values.


  The following example will override the default "add a line" button
  by replacing it with 3 new buttons:
  "Add a product", "Add a section" and "Add a note".

  "Add a product" will set the field 'display_type' to its default value.

  The two other buttons will set the field 'display_type'
  to be respectively 'line_section' and 'line_note'.

  .. code-block:: xml

    <control>
      <create
        string="Add a product"
      />
      <create
        string="Add a section"
        context="{'default_display_type': 'line_section'}"
      />
      <create
        string="Add a note"
        context="{'default_display_type': 'line_note'}"
      />
    </control>

.. [#treehistory] for historical reasons, it has its origin in tree-type views
                  later repurposed to a more table/list-type display


.. _bootstrap contextual color: https://getbootstrap.com/docs/3.3/components/#available-variations
