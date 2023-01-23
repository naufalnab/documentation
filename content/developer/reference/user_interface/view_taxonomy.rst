
.. _reference/user_interface/views/attributes:

Attributes
==========

The different view types have a wide variety of attributes allowing customizations of
the generic behaviors. Some main attributes will be explained here. They do not all have
an impact on all view types.

.. note:: The current context and user access rights may also impact the view abilities.

.. todo:: info on create/... 
* ``edit`` (``form`` & ``list`` & ``gantt``)

  Disable/enable record editing on the view.

* ``delete`` (``form`` & ``list``)

  Disable/enable record deletion on the view through the **Action** dropdown.

* ``duplicate`` (``form``)

  Disable/enable record duplication on the view through the **Action** dropdown.

* ``decoration-{$name}`` (``list`` & ``gantt``)

  Define a conditional display of a record in the style of a row's text based on the corresponding
  record's attributes.

  Values are Python expressions. For each record, the expression is evaluated
  with the record's attributes as context values and if ``true``, the
  corresponding style is applied to the row. Here are some of the other values
  available in the context:

  * ``uid``: the id of the current user,
  * ``today``: the current local date as a string of the form ``YYYY-MM-DD``,
  * ``now``: same as ``today`` with the addition of the current time.
    This value is formatted as ``YYYY-MM-DD hh:mm:ss``.

  .. code-block:: xml

    <tree decoration-info="state == 'draft'"
        decoration-danger="state == 'help_needed'"
        decoration-bf="state='busy'">
        <!-- TREE_VIEW_CONTENT -->
    </tree>

  .. warning::
     Supported values differ for the two view types. The Gantt view only supports ``success``,
     ``info``, ``warning``, ``danger`` and ``secondary`` displays. The list view supports ``bf``,
     ``it``, ``success``, ``info``, ``warning``, ``danger``, ``muted`` and ``primary`` displays.

* ``sample`` (``kanban`` & ``list`` & ``gantt`` & ``graph`` & ``pivot`` & ``cohort`` & ``dashboard``)

  Populate the view with a set of sample records if none are found for the current model.
  This attribute is false by default.

  These fake records will have heuristics for certain field names/models. For example,
  a field 'display_name' on the model 'res.users' will be populated with sample people names
  while an 'email' field will be in the form 'firstname.lastname@sample.demo'.

  The user will not be able to interact with these data and they will be discarded as soon as
  an action is performed (record created, column added, etc.)

* ``banner_route``
  a route address to be fetched and prepended to the view.

  If this attribute is set, the
  :ref:`controller route url<reference/controllers>` will be fetched and
  displayed above the view. The json response from the controller should
  contain an "html" key.

  If the html contains a stylesheet <link> tag, it will be
  removed and appended to <head>.

  To interact with the backend you can use <a type="action"> tags. Please take
  a look at the documentation of the _onActionClicked method of
  AbstractController (*addons/web/static/src/js/views/abstract_controller.js*)
  for more details.

  Only views extending AbstractView and AbstractController can use this
  attribute, like :ref:`reference/user_interface/views/form`, :ref:`reference/user_interface/views/kanban`,
  :ref:`reference/user_interface/views/list`, ...

  Example:

  .. code-block:: xml

      <tree banner_route="/module_name/hello" />

  .. code-block:: python

      class MyController(odoo.http.Controller):
          @http.route('/module_name/hello', auth='user', type='json')
          def hello(self):
              return {
                  'html': """
                      <div>
                          <link href="/module_name/static/src/css/banner.css"
                              rel="stylesheet">
                          <h1>hello, world</h1>
                      </div> """
              }

.. todo:: Views main content section, with field, group & separator ?

.. _reference/user_interface/views/types:
