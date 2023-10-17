ADRV9009 & ADRV9008
===============================================================================

.. image:: adrv9009-bc.jpg
   :align: left
   :width: 150

The :adi:`ADRV9009-W/PCBZ <EVAL-ADRV9008-9009>`, :adi:`ADRV9008-1W/PCBZ <EVAL-ADRV9008-9009>`
and :adi:`ADRV9008-2W/PCBZ <EVAL-ADRV9008-9009>` are FMC radio cards for the
:adi:`ADRV9009` and :adi:`ADRV9008`, respectively, a highly integrated RF Transceiver™.
While the complete chip level design package can be found on
:adi:`the ADI web site <en/design-center/landing-pages/001/integrated-rf-agile-transceiver-design-resources.html>`,
information on the card and how to use it, the design package that surrounds it,
and the software which can make it work can be found here.

.. image:: adrv9009-pcb.jpg
   :align: center

Table of Contents
-------------------------------------------------------------------------------

People who follow the flow that is outlined, have a much better experience with
things. However, like many things, documentation is never as complete as it should be.
If you have any questions, feel free to :ref:`ask <ad-fmcomms2-ebz help_and_support>`.

#. Use the board to better understand the ADRV9009/ADRV9008-1/ADRV9008-2

   #. `What you need to get started <adrv9009 prerequisites>`__
   #. `Quick Start Guides <adrv9009 quickstart>`__

      #. :ref:`Linux on ZCU102 <adrv9009 quickstart zynqmp>`
      #. :dokuwiki:`Configure a pre-existing SD-Card <resources/tools-software/linux-software/zynq_images#preparing_the_image>`
      #. :dokuwiki:`Update the old card you received with your hardware <resources/tools-software/linux-software/zynq_images#staying_up_to_date>`

   #. Linux Applications

      #. :dokuwiki:`IIO Scope <resources/tools-software/linux-software/iio_oscilloscope>`

         #. :dokuwiki:`ADRV9009/ADRV9008 IIO Scope View <resources/tools-software/linux-software/adrv9009_osc_main>`
         #. :dokuwiki:`ADRV9009/ADRV9008 Control IIO Scope Plugin <resources/tools-software/linux-software/adrv9009_plugin>`
         #. :dokuwiki:`Advanced ADRV9009/ADRV9008 Control IIO Scope Plugin <resources/tools-software/linux-software/adrv9009_advanced_plugin>`

      #. :dokuwiki:`FRU EEPROM Utility <resources/eval/user-guides/ad-fmcomms1-ebz/software/linux/applications/fru_dump>`

   #. Push custom data into/out of the ADRV9009/ADRV9008

      #. :ref:`Basic Data files and formats <adrv9009 software basic_iq_datafiles>`
      #. :dokuwiki:`Stream data into/out of MATLAB <resources/tools-software/transceiver-toolbox>`
      #. :dokuwiki:`Python Interfaces <resources/tools-software/linux-software/pyadi-iio>`

#. Design with the ADRV9009/ADRV9008

   #. :ref:`Understanding the ADRV9009/ADRV9008 <adrv9009 adrv9008>`

      #. :adi:`ADRV9009 Product page <ADRV9009>`
      #. :adi:`ADRV9008 Product page <ADRV9008>`
      #. :adi:`Full Datasheet and chip design package <en/design-center/landing-pages/001/integrated-rf-agile-transceiver-design-resources.html>`
      #. :adi:`MATLAB Filter Wizard / Profile Generator for ADRV9009 <media/en/evaluation-boards-kits/evaluation-software/ADRV9008-x-ADRV9009-profile-config-tool-filter-wizard-v2.4.zip>`

   #. Hardware in the Loop / How to design your own custom BaseBand

      #. :dokuwiki:`GNU Radio <resources/tools-software/linux-software/gnuradio>`
      #. :dokuwiki:`Transceiver Toolbox <resources/tools-software/transceiver-toolbox>`

   #. Design a custom ADRV9009/ADRV9008 based platform

      #. Linux software

         #. :dokuwiki:`ADRV9009/ADRV9008 Linux Device Driver <resources/tools-software/linux-drivers/iio-transceiver/adrv9009>`

            #. :dokuwiki:`ADRV9009/ADRV9008 Device Driver Customization <resources/tools-software/linux-drivers/iio-transceiver/adrv9009-customization>`
            #. :dokuwiki:`Customizing the devicetree on the target <resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynq_tips_tricks>`

         #. :dokuwiki:`JESD204 (FSM) Interface Linux Kernel Framework <resources/tools-software/linux-drivers/jesd204/jesd204-fsm-framework>`
         #. :dokuwiki:`AD9528 Low Jitter Clock Generator Linux Driver <resources/tools-software/linux-drivers/iio-pll/ad9528>`
         #. :dokuwiki:`AD7291 IIO ADC Linux Driver <resources/tools-software/linux-drivers/iio-adc/ad7291>`
         #. :dokuwiki:`AXI-DMAC DMA Controller Linux Driver <resources/tools-software/linux-drivers/axi-dmac>`
         #. :dokuwiki:`JESD204B Transmit Linux Driver <resources/tools-software/linux-drivers/jesd204/axi_jesd204_tx>`

            #. :dokuwiki:`JESD204B Status Utility <resources/tools-software/linux-software/jesd_status>`

         #. :dokuwiki:`JESD204B Receive Linux Driver <resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`

            #. :dokuwiki:`JESD204B Status Utility <resources/tools-software/linux-software/jesd_status>`

         #. :dokuwiki:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver <resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`

            #. :dokuwiki:`JESD204 Eye Scan <resources/tools-software/linux-software/jesd_eye_scan>`

         #. :dokuwiki:`AXI ADC HDL Linux Driver <resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`
         #. :dokuwiki:`AXI DAC HDL Linux Driver <resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`

      #. :dokuwiki:`Changing the VCXO frequency and updating the default RF Transceiver Profile <resources/eval/user-guides/rf-trx-vcxo-and-profiles>`
      #. :dokuwiki:`ADRV9009/ADRV9008 No-OS System Level Design Setup <resources/eval/user-guides/adrv9009/no-os-setup>`
      #. :dokuwiki:`HDL Reference Design <resources/eval/user-guides/adrv9009/reference_hdl>` which you must use in your FPGA.
      #. :dokuwiki:`HDL Targeting From MATLAB and Simulink <resources/tools-software/transceiver-toolbox>`

#. :ref:`Additional Documentation about SDR Signal Chains - The math behind the RF <ad-fmcomms1-ebz math>`
#. :ref:`Help and Support <ad-fmcomms2-ebz help-and-support>`

Videos
-------------------------------------------------------------------------------

Software Defined Radio using the Linux IIO Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. video:: http://ftp.fau.de/fosdem/2015/devroom-software_defined_radio/iiosdr.mp4

ADI Articles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Four Quick Steps to Production: Using Model-Based Design for Software-Defined Radio

   #. :adi:`Part 1 - The Analog Devices/Xilinx SDR Rapid Prototyping Platform: Its Capabilities, Benefits, and Tools <library/analogDialogue/archives/49-09/four-step-sdr-01.html>`
   #. :adi:`Part 2 - Mode S Detection and Decoding Using MATLAB and Simulink <library/analogDialogue/archives/49-10/four-step-sdr-02.html>`
   #. :adi:`Part 3 - Mode S Signals Decoding Algorithm Validation Using Hardware in the Loop <library/analogDialogue/archives/49-11/four-step-sdr-03.html>`
   #. :adi:`Part 4 - Rapid Prototyping Using the Zynq SDR Kit and Simulink Code Generation Workflow <library/analogDialogue/archives/49-12/four-step-sdr-04.html>`

MathWorks Webinars
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. :mw:`Modelling and Simulating Analog Devices’ RF Transceivers with MATLAB and SimRF <videos/modelling-and-simulating-analog-devices-rf-transceivers-with-matlab-and-simrf-89934.html>`
#. :mw:`Getting Started with Software-Defined Radio using MATLAB and Simulink <videos/getting-started-with-software-defined-radio-using-matlab-and-simulink-108646.html>`

Warning
-------------------------------------------------------------------------------

.. esd_warning::
