Dashboard
=========

.. raw:: html

   <span class="badge" style="background-color:#AD5E99">Enterprise feature</span>

Like pivot and graph view, The dashboard view is used to display aggregate data.
However, the dashboard can embed sub views, which makes it possible to have a
more complete and interesting look on a given dataset.

The dashboard view can display sub views, aggregates for some fields (over a
domain), or even *formulas* (expressions which involves one or more aggregates).
For example, here is a very simple dashboard:

.. code-block:: xml

    <dashboard>
        <view type="graph" ref="sale_report.view_order_product_graph"/>
        <group string="Sale">
            <aggregate name="price_total" field="price_total" widget="monetary"/>
            <aggregate name="order_id" field="order_id" string="Orders"/>
            <formula name="price_average" string="Price Average"
                value="record.price_total / record.order_id" widget="percentage"/>
        </group>
        <view type="pivot" ref="sale_report.view_order_product_pivot"/>
    </dashboard>

The root element of the Dashboard view is <dashboard>, it does not accept any
attributes.

There are 5 possible type of tags in a dashboard view:

.. rst-class:: o-definition-list

``view``
    declares a sub view.

    Admissible attributes are:

    .. rst-class:: o-definition-list

    ``type`` (mandatory)
        The type of the sub view.  For example, *graph* or *pivot*.

    ``ref`` (optional)
        An xml id for a view. If not given, the default view for the model will
        be used.

    ``name`` (optional)
        A string which identifies this element.  It is mostly
        useful to be used as a target for an xpath.

``group``
    defines a column layout.  This is actually very similar to the group element
    in a form view.

    Admissible attributes are:

    .. rst-class:: o-definition-list

    ``string`` (optional)
        A description which will be displayed as a group title.

    ``colspan`` (optional)
        The number of subcolumns in this group tag. By default, 6.

    ``col`` (optional)
        The number of columns spanned by this group tag (only makes sense inside
        another group). By default, 6.


``aggregate``
    declares an aggregate.  This is the value of an aggregate for a given field
    over the current domain.

    Note that aggregates are supposed to be used inside a group tag (otherwise
    the style will not be properly applied).

    Admissible attributes are:

    .. rst-class:: o-definition-list

    ``field`` (mandatory)
        The field name to use for computing the aggregate. Possible field types
        are:

        - ``integer`` (default group operator is sum)
        - ``float``  (default group operator is sum)
        - ``many2one`` (default group operator is count distinct)

    ``name`` (mandatory)
        A string to identify this aggregate (useful for formulas)

    ``string`` (optional)
        A short description that will be displayed above the value. If not
        given, it will fall back to the field string.

    ``domain`` (optional)
        An additional restriction on the set of records that we want to aggregate.
        This domain will be combined with the current domain.

    ``domain_label`` (optional)
        When the user clicks on an aggregate with a domain, it will be added to
        the search view as a facet.  The string displayed for this facet can
        be customized with this attribute.

    ``group_operator`` (optional)
        A valid postgreSQL aggregate function identifier to use when aggregating
        values (see https://www.postgresql.org/docs/12/static/functions-aggregate.html).
        If not provided, By default, the group_operator from the field definition is used.
        Note that no aggregation of field values is achieved if the group_operator value is "".

        .. note:: The special aggregate function ``count_distinct`` (defined in odoo) can also be used here

        .. code-block:: xml

          <aggregate name="price_total_max" field="price_total" group_operator="max"/>



    ``col`` (optional)
        The number of columns spanned by this tag (only makes sense inside a
        group). By default, 1.

    ``widget`` (optional)
        A widget to format the value (like the widget attribute for fields).
        For example, monetary.

    ``help`` (optional)
        A help message to dipslay in a tooltip (equivalent of help for a field in python)

    ``measure`` (optional)
        This attribute is the name of a field describing the measure that has to be used
        in the graph and pivot views when clicking on the aggregate.
        The special value __count__ can be used to use the count measure.

        .. code-block:: xml

          <aggregate name="total_ojects" string="Total Objects" field="id" group_operator="count" measure="__count__"/>

    ``clickable`` (optional)
        A boolean indicating if this aggregate should be clickable or not (default to true).
        Clicking on a clickable aggregate will change the measures used by the subviews
        and add the value of the domain attribute (if any) to the search view.

    ``value_label`` (optional)
        A string put on the right of the aggregate value.
        For example, it can be useful to indicate the unit of measure
        of the aggregate value.

``formula``
    declares a derived value.  Formulas are values computed from aggregates.

    Note that like aggregates, formulas are supposed to be used inside a group
    tag (otherwise the style will not be properly applied).

    Admissible attributes are:

    .. rst-class:: o-definition-list

    ``value`` (mandatory)
        A string expression that will be evaluated, with the builtin python
        evaluator (in the web client).  Every aggregate can be used in the
        context, in the ``record`` variable.  For example,
        ``record.price_total / record.order_id``.

    ``name`` (optional)
        A string to identify this formula

    ``string`` (optional)
        A short description that will be displayed above the formula.

    ``col`` (optional)
        The number of columns spanned by this tag (only makes sense inside a
        group). By default, 1.

    ``widget`` (optional)
        A widget to format the value (like the widget attribute for fields).
        For example, monetary. By default, it is 'float'.

    ``help`` (optional)
        A help message to dipslay in a tooltip (equivalent of help for a field in python)

    ``value_label`` (optional)
        A string put on the right of the formula value.
        For example, it can be useful to indicate the unit of measure
        of the formula value.

``widget``
    Declares a specialized widget to be used to display the information. This is
    a mechanism similar to the widgets in the form view.

    Admissible attributes are:

    .. rst-class:: o-definition-list

    ``name`` (mandatory)
        A string to identify which widget should be instantiated. The view will
        look into the ``widget_registry`` to get the proper class.

    ``col`` (optional)
        The number of columns spanned by this tag (only makes sense inside a
        group). By default, 1.
