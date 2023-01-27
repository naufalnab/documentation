=====
India
=====

.. _india/installation:

Installation
============

:ref:`Install <general/install>` the following modules to get all the features of the Indian
localization:

.. list-table::
   :header-rows: 1

   * - Name
     - Technical name
     - Description
   * - :guilabel:`Indian - Accounting`
     - `l10n_in`
     - Default :doc:`fiscal localization package <../overview/fiscal_localization_packages>`
   * - :guilabel:`Indian E-invoicing`
     - `l10n_in_edi`
     - :ref:`Indian e-invoicing integration <india/e-invoicing>`
   * - :guilabel:`Indian E-waybill`
     - `l10n_in_edi_ewaybill`
     - :ref:`Indian E-waybill integration <india/e-waybill>`
   * - :guilabel:`Indian GST Return Filing`
     - `l10n_in_reports_gstr`
     - :ref:`Indian GST Return Filing <india/gstr>`
   * - :guilabel:`Indian Reports`
     - `l10n_in_reports`
     - :ref:`Indian Tax Reports <india/gstr_reports>`

.. _india/e-invoicing:

Indian e-invoicing
==================

Odoo is compliant with the **Indian Goods and Services Tax (GST) e-Invoice system** requirements.

.. important::
   Indian e-invoicing is available from Odoo 15.0. If needed, :doc:`upgrade
   </administration/upgrade>` your database.

.. _india/e-invoicing-api:

Registration on your NIC e-Invoice web portal
---------------------------------------------

You must register on the **NIC e-Invoice** web portal to get your **API credentials**. You need
these credentials to :ref:`configure your Odoo Accounting app <india/e-invoicing-configuration>`.

#. Log in to the NIC e-Invoice web portal at https://einvoice1.gst.gov.in/ by clicking on
   :guilabel:`Login` and entering your :guilabel:`Username` and :guilabel:`Password`.

   .. note::
      If you have already registered on the NIC Eway Bill Production portal, then you can use the
      same login credentials here.

   .. image:: india/e-invoice-system-login.png
      :align: center
      :alt: Register Odoo ERP system on e-invoice web portal

#. From your dashboard, go to :menuselection:`API Registration --> User Credentials --> Create API
   User`.

   .. image:: india/e-invoice-create-api-user.png
      :align: center
      :alt: Click on User Credentials and Create API User

#. After that, you receive an :abbr:`OTP (one-time password)` code to your registered mobile number.
#. Enter the OTP code and click on :guilabel:`Verify OTP`.

   .. image:: india/trigger-otp.png
      :align: center
      :alt: Trigger an OTP to your registered phone number

#. Select :guilabel:`Through GSP` in the first field, select :guilabel:`Tera Software Limited`
   as your GSP, and type in a :guilabel:`Username` and :guilabel:`Password` for your API.

   .. image:: india/submit-api-registration-details.png
      :align: center
      :alt: Submit API specific Username and Password

#. Click on :guilabel:`Submit`.

.. _india/e-invoicing-configuration:

Configuration on Odoo
---------------------

To set up the e-invoice service, go to :menuselection:`Accounting --> Configuration --> Settings -->
Indian Electronic Invoicing`, and enter the :guilabel:`Username` and :guilabel:`Password`.

.. image:: india/e-invoice-setup.png
   :align: center
   :alt: Setup e-invoice service

.. _india/e-invoicing-journals:

Journals
~~~~~~~~

Your default *sales* journal should be already configured correctly. You can check it or configure
other journals by going to :menuselection:`Accounting --> Configuration --> Journals`. Then, open
your *sales* journal, and in the :guilabel:`Advanced Settings` tab, under :guilabel:`Electronic Data
Interchange`, check :guilabel:`E-Invoice (IN)` and :guilabel:`Save`.

.. image:: india/journal-configuration.png
   :align: center
   :alt: Journal configuration

.. _india/e-invoicing-workflow:

Workflow
--------

To start invoicing from Odoo, an invoice must be created using the standard invoicing flow, that is,
either from a sales order or the invoice menu in the Accounting application.

.. _india/invoice-validation:

Invoice validation
~~~~~~~~~~~~~~~~~~

Once the invoice is validated, a confirmation message is displayed at the top.

Odoo automatically uploads the JSON-signed file to the government portal after a while. If you want
to process the invoice immediately, you can click on :guilabel:`Process Now`.

.. image:: india/e-invoice-process.png
   :align: center
   :alt: Indian e-invoicing confirmation message: "The invoice will be processed asynchronously by
         the following E-invoicing service : E-Invoice (IN)"

.. note::
   - You can find the JSON-signed file in the attached files, in the chatter.
   - You can check the status of EDI with web-service under the :guilabel:`EDI Document` tab or the
     :guilabel:`Electronic invoicing` field.

.. _india/invoice-pdf-report:

Invoice PDF Report
~~~~~~~~~~~~~~~~~~

Once the invoice is submitted and validated, you can print the invoice PDF report. The report
includes the :abbr:`IRN (Invoice Reference Number)`, acknowledgment number and date, and QR code.
They certify that the invoice is a valid fiscal document.

.. image:: india/invoice-report.png
   :align: center
   :alt: IRN and QR code

.. _india/edi-cancellation:

EDI Cancellation
~~~~~~~~~~~~~~~~

If you want to cancel an e-invoice, go to the :guilabel:`Other info` tab of the invoice and fill out
the :guilabel:`Cancel reason` and :guilabel:`Cancel remarks` fields. Then, click on
:guilabel:`Request EDI cancellation`. The status of the :guilabel:`Electronic invoicing` field
changes to :guilabel:`To Cancel`.

.. important::
   Doing so cancels both the :ref:`E-invoice <india/e-invoicing>` and the :ref:`E-waybill
   <india/e-waybill>`.

.. image:: india/e-invoice-cancellation.png
   :align: center
   :alt: cancel reason and remarks

.. note::
   - If you want to abort the cancellation before processing the invoice, then click on
     :guilabel:`Call Off EDI Cancellation`.
   - Once you request to cancel the e-invoice, Odoo automatically submits the JSON Signed file to
     the government portal. You can click on :guilabel:`Process Now` if you want to process the
     invoice immediately.

.. _india/verify-e-invoice:

Verify the e-invoice from the GST
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After submitting an e-invoice, you can also verify the signed invoice from the GST e-Invoice system
website.

#. Download the JSON file from the attached files.
#. Open the e-invoice portal: https://einvoice1.gst.gov.in/ and go to :menuselection:`Search -->
   Verify Signed Invoice`.
#. Select the JSON file and submit it.

   .. image:: india/verify-invoice.png
      :align: center
      :alt: select the JSON file for verify invoice

#. You can check the verified signed e-invoice here.

   .. image:: india/signed-invoice.png
      :align: center
      :alt: verified e-invoice

.. _india/e-waybill:

Indian E-waybill
================

Odoo is compliant with the **Indian Goods and Services Tax (GST) E-waybill system** requirements.

.. important::
   Indian E-waybill is available from Odoo 15.0. If needed, :doc:`upgrade </administration/upgrade>`
   your database.

.. _india/e-waybill-api:

API Registration on your NIC E-waybill web portal
--------------------------------------------------

You must register on the **NIC E-waybill** web portal to create your **API credentials**. You need
these credentials to :ref:`configure your Odoo Accounting app <india/e-waybill-configuration>`.

#. Log in to the NIC E-waybill web portal at https://ewaybillgst.gov.in/ by clicking on
   :guilabel:`Login` and entering your :guilabel:`Username` and :guilabel:`Password`.

   .. image:: india/e-waybill-system-login.png
      :align: center
      :alt: E-waybill login

#. From your dashboard, go to :menuselection:`Registration --> For GSP`.

   .. image:: india/e-waybill-registration-menu.png
      :align: center
      :alt: E-waybill registration

#. Click on :guilabel:`Send OTP`; you should receive an :abbr:`OTP (one-time password)` code to your
   registered mobile number.
#. Enter the OTP code and click on :guilabel:`Verify OTP`.

   .. image:: india/e-waybill-gsp-registration.png
      :align: center
      :alt: E-waybill OTP verification

#. Check if :guilabel:`Tera Software Limited` is already on the list of registered GSP/ERP. If so,
   use this username and password. Otherwise, follow the next steps.

   .. image:: india/e-waybill-gsp-list.png
      :align: center
      :alt: E-waybill list of registered GSP/ERP

#. Select :guilabel:`Add/New`, select :guilabel:`Tera Software Limited` as your GSP Name, create a
   :guilabel:`Username` and a :guilabel:`Password` for your API, and click on :guilabel:`Add`.

   .. image:: india/e-waybill-registration-details.png
      :align: center
      :alt: Submit GSP API registration details

.. _india/e-waybill-configuration:

Configuration on Odoo
---------------------

To set up the E-waybill service, go to :menuselection:`Accounting --> Configuration --> Settings -->
Indian Electronic WayBill --> Setup E-Waybill`, and enter your :guilabel:`Username` and
:guilabel:`Password`.

.. image:: india/e-waybill-configuration.png
   :align: center
   :alt: E-waybill setup odoo

.. _india/e-waybill-workflow:

Workflow
--------

To issue an E-waybill from Odoo, you must create an invoice/bill with the details of the E-waybill
using the standard invoicing/bill flow (either from a sales/purchase order or the invoice/bill menu
in Accounting).

.. _india/e-waybill-send:

Send an E-waybill
~~~~~~~~~~~~~~~~~

You can manually send an E-waybill by clicking on :guilabel:`Send E-waybill`.

.. image:: india/e-waybill-send-button.png
   :align: center
   :alt: Send E-waybill button on invoices

To send the E-waybill automatically when you confirm an invoice or a bill, enable
:guilabel:`E-waybill (IN)` in your :ref:`Sale/Purchase Journal <india/e-invoicing-journals>`.

.. _india/invoice-validation-e-way:

Invoice validation
~~~~~~~~~~~~~~~~~~

Once you have issued the invoice and clicked on :guilabel:`Send E-waybill`, a confirmation message
is displayed.

.. note::
   - Odoo automatically uploads the JSON-signed file to the government portal after a while. You can
     click on :guilabel:`Process Now` if you want to process the invoice immediately.
   - You can find the JSON-signed file in the attached files in the chatter.

.. image:: india/e-waybill-process.png
   :align: center
   :alt: Indian e-waybill confirmation message: "The invoice will be processed asynchronously by
         the following E-waybill service : E-waybill (IN)"

Invoice PDF Report
~~~~~~~~~~~~~~~~~~

You can print the invoice PDF report once you have submitted the E-waybill. The report includes the
**E-waybill number** and the **E-waybill validity date**.

.. image:: india/e-waybill-invoice-report.png
   :align: center
   :alt: E-waybill acknowledgment number and date

.. _india/e-waybill-cancellation:

E-waybill Cancellation
~~~~~~~~~~~~~~~~~~~~~~

If you want to cancel an E-waybill, go to the :guilabel:`eWayBill` tab of the invoice and fill out
the :guilabel:`Cancel reason` and :guilabel:`Cancel remarks` fields. Then, click on
:guilabel:`Request EDI Cancellation`.

.. important::
   Doing so cancels both the :ref:`E-invoice <india/e-invoicing>` and the :ref:`E-waybill
   <india/e-waybill>`.

.. image:: india/e-waybill-cancellation.png
   :align: center
   :alt: cancel reason and remarks

.. note::
   - If you want to abort the cancellation before processing the invoice, click on :guilabel:`Call
     Off EDI Cancellation`.
   - If the E-invoice is applicable for this invoice, then it will also be canceled.
   - Once you request to cancel the E-waybill, Odoo automatically submits the JSON Signed file to
     the government portal. You can click on :guilabel:`Process Now` if you want to process the
     invoice immediately.

.. _india/gstr:

Indian GST Return Filing
========================

Odoo supports **Indian Goods and Services Tax (GST) return filing** requirements.

.. _india/gstr_api:

Enable API Access
-----------------

You must enable API Access on the GST Portal.

#. Login to the :guilabel:`GST Portal` on - https://services.gst.gov.in/services/login by entering your
   :guilabel:`Username` and :guilabel:`Password`.

   .. image:: india/gst-portal-login.png
      :align: center
      :alt: Register On GST portal

#. Now, go to :guilabel:`My Profile`.

   .. image:: india/gst-portal-my-profile.png
      :align: center
      :alt: Click On the My Profile from profile

#. Select :guilabel:`Manage API Access`.

   .. image:: india/gst-quick-links.png
      :align: center
      :alt: Select Manage API access under the Quick Links.

#. Click :guilabel:`Yes` To Enable API Access.

   .. image:: india/gst-portal-api-yes.png
      :align: center
      :alt: Click Yes

#. Now, You will be able to see duration dropdown menu. Select :guilabel:`duration` of your preference.

   .. image:: india/gst-portal-duration-dropdown.png
      :align: center
      :alt: dropdown list for duration

#. Now, Click on the :guilabel:`Confirm`. You are all set to configure it in odoo
   :ref:`Configure Your Odoo Indian GST Service <india/gstr_configuration>`.

   .. image:: india/gst-portal-api-confirm.png
      :align: center
      :alt: confirm the duration choice

.. _india/gstr_configuration:

Configuration Of Indian GST Service In Odoo
-------------------------------------------

#. To set up the Indian GST service, go to :menuselection:`Accounting --> Configuration --> Settings -->
   Indian GST Service` and enter the :guilabel:`GST Username`. Then click on the :guilabel:`Send OTP`.

   .. image:: india/gst-setup.png
      :align: center
      :alt: Please enter your GST Portal Username as Username

#. Enter the OTP code and click on the :guilabel:`Validate` Button.

   .. image:: india/gst-otp.png
      :align: center
      :alt: Enter the OTP

.. _india/gstr_workflow:

Workflow of Filing GST Return
-----------------------------

GST Return Filing using Odoo is a multi-step process.

#. Send GSTR-1
#. Receive GSTR-2B And Reconcile With Odoo Bills
#. GSTR-3

.. important::
   User can set the Tax Return Periodicity. If need to change, Please refer
   :ref:`Tax Return Periodicity <reporting/declarations/tax_returns/tax_return_periodicity>`.

After Configuration Of Indian GST Service, You can file your GST Return.
Go to :menuselection:`Accounting --> Reporting --> India --> GST Return Periods` and Create a new GST
Return Period if not exist.

   .. image:: india/gst-return-period.png
      :align: center
      :alt: Create GST Return Period

.. _india/gstr-1:

Send GSTR-1
~~~~~~~~~~~

#. User can verify the :ref:`GSTR-1 Report <india/gstr-1_report>` before pushing it to the :guilabel:`GST Portal` by clicking on
   the :ref:`GSTR-1 Report <india/gstr-1_report>`.

#. If :ref:`GSTR-1 Report <india/gstr-1_report>` is verified then click on the :guilabel:`Push to GSTN`
   to send it to the :guilabel:`GST Portal`. Now, state of the :guilabel:`GSTR-1` will be :guilabel:`Sending`.

   .. image:: india/gst-gstr-1-sending.png
      :align: center
      :alt: GSTR-1 in the Sending Status

#. After few minutes, You can see the state of the :guilabel:`GSTR-1` changes to :guilabel:`Waiting for Status`.
   It means that your :ref:`GSTR-1 Report <india/gstr-1_report>` is sent to the :guilabel:`GST Portal` and
   is being verified on the :guilabel:`GST Portal`.

   .. image:: india/gst-gstr-1-waiting.png
      :align: center
      :alt: GSTR-1 in the Waiting for Status

#. Check after few minutes, You will be able to see the state has been changed to
   :guilabel:`Sent` or :guilabel:`Error in Invoice`. The state :guilabel:`Error in Invoice`
   indicates that some of the invoices are not as same as it has to be inorder to submit
   on the :guilabel:`GST Portal`.

   If the state of the :guilabel:`GSTR-1` is :guilabel:`Sent`. It means that your
   :ref:`GSTR-1 Report <india/gstr-1_report>` is ready to be filed on the :guilabel:`GST Portal`.

      .. image:: india/gst-gstr-1-sent.png
         :align: center
         :alt: GSTR-1 Sent

   If the state of the :guilabel:`GSTR-1` is :guilabel:`Error in Invoice`:

      .. image:: india/gst-gstr-1-error.png
         :align: center
         :alt: GSTR-1 Error in Invoice

   You can check for invoices that has error in the :guilabel:`Log Note`. After resolving issues in such
   invoices user can click on the :guilabel:`Push to GSTN` to submit.

   .. image:: india/gst-gstr-1-error-log.png
      :align: center
      :alt: GSTR-1 Error in Invoice Log

#. You can click on the :guilabel:`Mark as Filed` after filing the :ref:`GSTR-1 Report <india/gstr-1_report>` on
   the :guilabel:`GST Portal`. It will change your :guilabel:`GSTR-1` state as :guilabel:`Filed`.

   .. image:: india/gst-gstr-1-filed.png
      :align: center
      :alt: GSTR-1 in the Filed Status

.. _india/gstr-2B:

Receive GSTR-2B
~~~~~~~~~~~~~~~

In this step, User can receive the :guilabel:`GSTR-2B Report` from GST Portal. This will automatically
Reconcile :guilabel:`GSTR-2B Report` with your Odoo bills.

#. By clicking on the :guilabel:`Fetch GSTR-2B Summary` user can conveniently reconcile with their Odoo bills.

#. After few minutes, State of the :guilabel:`GSTR-2B` is changed to :guilabel:`Waiting for Reception`. It indicates that
   the Odoo is trying to receive the :guilabel:`GSTR-2B Report` from the :guilabel:`GST Portal`.

   .. image:: india/gst-gstr-2b-waiting.png
      :align: center
      :alt: GSTR-2B in Waiting for Reception

#. After few minutes, you can see the state of the :guilabel:`GSTR-2B` is changed to the :guilabel:`Being Processed`.
   It means that Odoo is reconciling :guilabel:`GSTR-2B Report` with your Odoo bills.

   .. image:: india/gst-gstr-2b-processed.png
      :align: center
      :alt: GSTR-2B in Waiting for Reception

#. Check after few seconds. The state of the :guilabel:`GSTR-2B` will be :guilabel:`Matched` or
   :guilabel:`Partially Matched`.

   If state of the :guilabel:`GSTR-2B` is :guilabel:`Matched`:

      .. image:: india/gst-gstr-2b-matched.png
         :align: center
         :alt: GSTR-2B Matched

   If state of the :guilabel:`GSTR-2B` is :guilabel:`Partially Matched`:

      .. image:: india/gst-gstr-2b-partially.png
         :align: center
         :alt: GSTR-2B Partially Matched

   After clicking on :guilabel:`View Reconciled Bills`, You can see the bills grouped in the different
   category. You can make changes in bills accordingly. After that click on the :guilabel:`re-match`.

      .. image:: india/gst-gstr-2b-reconcile.png
         :align: center
         :alt: GSTR-2B Reconciled Bills

.. _india/gstr-3:

GSTR-3
~~~~~~

:ref:`GSTR-3 Report <india/gstr-3_report>` is a monthly summary of sales and purchases.
This return is auto-generated by extracting information from GSTR-1 and GSTR-2.

#. User can verify :ref:`GSTR-3 Report <india/gstr-3_report>` with the GSTR-3 Report available on the
   :guilabel:`GST Portal` by clicking on the :ref:`GSTR-3 Report <india/gstr-3_report>`.

#. Once, :ref:`GSTR-3 Report <india/gstr-3_report>` is verified by the user and user has paid the Tax amount on
   the :guilabel:`GST Portal`, user can click on the :guilabel:`Draft Entry`.

   .. image:: india/gst-gstr-3.png
      :align: center
      :alt: GSTR-3

#. Here, In closing entry add the tax amount paid on the :guilabel:`GST Portal` using challan.

   .. image:: india/gst-gstr-3-post.png
      :align: center
      :alt: GSTR-3 Post Entry


#. Once, user clicks on the :guilabel:`POST`, :ref:`GSTR-3 Report <india/gstr-3_report>` state will be
   changed to the :guilabel:`Filed`.

   .. image:: india/gst-gstr-3-filed.png
      :align: center
      :alt: GSTR-3 Filed

.. _india/gstr_reports:

Indian Tax Reports
==================

Odoo supports **GSTR-1** and **GSTR-3** reports.

.. _india/gstr-1_report:

GSTR-1 Report
-------------

:guilabel:`GSTR-1 Report` is divided into mutliple sections. It displays Base Amount, CGST, SGST, IGST and CESS
for each of the section.

   .. image:: india/gst-gstr-1-sale-report.png
      :align: center
      :alt: GSTR-1 Report

.. _india/gstr-3_report:

GSTR-3 Report
-------------

:guilabel:`GSTR-3 Report` contains different section.

* Details of outward and inward supply subject to reverse charge
* Eligible ITC(Income Tax Credit)
* Values of Exempt, Nil rated and non-GST inward supply
* Details of inter-state supplies made to unregistered person

   .. image:: india/gst-gstr-3-report.png
         :align: center
         :alt: GSTR-3 Report
