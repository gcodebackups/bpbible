# This file was automatically generated by pywxrc.
# -*- coding: UTF-8 -*-

import wx
import wx.xrc as xrc

__res = None

def get_resources():
    """ This function provides access to the XML resources in this module."""
    global __res
    if __res == None:
        __init_resources()
    return __res




class xrcSearchPanel(wx.Panel):
#!XRCED:begin-block:xrcSearchPanel.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrcSearchPanel.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PrePanel()
        self.PreCreate(pre)
        get_resources().LoadOnPanel(pre, parent, "SearchPanel")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.panel_1 = xrc.XRCCTRL(self, "panel_1")
        self.searchkey = xrc.XRCCTRL(self, "searchkey")
        self.search_button = xrc.XRCCTRL(self, "search_button")
        self.genindex = xrc.XRCCTRL(self, "genindex")
        self.collapsible_panel = xrc.XRCCTRL(self, "collapsible_panel")
        self.tp_holder = xrc.XRCCTRL(self, "tp_holder")
        self.gui_search_type = xrc.XRCCTRL(self, "gui_search_type")
        self.proximity = xrc.XRCCTRL(self, "proximity")
        self.case_sensitive = xrc.XRCCTRL(self, "case_sensitive")
        self.exclude = xrc.XRCCTRL(self, "exclude")
        self.wholebible = xrc.XRCCTRL(self, "wholebible")
        self.oldtestament = xrc.XRCCTRL(self, "oldtestament")
        self.newtestament = xrc.XRCCTRL(self, "newtestament")
        self.dummy_radio = xrc.XRCCTRL(self, "dummy_radio")
        self.range_top = xrc.XRCCTRL(self, "range_top")
        self.range_bottom = xrc.XRCCTRL(self, "range_bottom")
        self.label_2 = xrc.XRCCTRL(self, "label_2")
        self.custom_range = xrc.XRCCTRL(self, "custom_range")
        self.search_label = xrc.XRCCTRL(self, "search_label")
        self.search_splitter = xrc.XRCCTRL(self, "search_splitter")
        self.verselist = xrc.XRCCTRL(self, "verselist")
        self.versepreview = xrc.XRCCTRL(self, "versepreview")
        self.progressbar = xrc.XRCCTRL(self, "progressbar")
        self.wxID_CLOSE = xrc.XRCCTRL(self, "wxID_CLOSE")



class xrcsearch_holder(wx.Panel):
#!XRCED:begin-block:xrcsearch_holder.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrcsearch_holder.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PrePanel()
        self.PreCreate(pre)
        get_resources().LoadOnPanel(pre, parent, "search_holder")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers





# ------------------------ Resource data ----------------------

def __init_resources():
    global __res
    __res = xrc.EmptyXmlResource()

    __res.Load('search.xrc')
