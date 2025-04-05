# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="My Regex Tester")
        self.set_border_width(10)
        self.set_default_size(600, 900)

        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(10)
        self.add(grid)

        grid.attach(Gtk.Label(label="Text:"), 0, 0, 1, 1)
        self.textview = Gtk.TextView()
        self.textview.set_wrap_mode(Gtk.WrapMode.WORD)
        self.textview.set_tooltip_text("Enter text to match against the regex pattern")
        self.textview.set_sensitive(True)
        self.textview.set_size_request(500, 400)
        grid.attach(self.textview, 1, 0, 1, 1)

        self.combo = Gtk.ComboBoxText()
        self.combo.append_text("match")
        self.combo.append_text("findall")
        self.combo.append_text("sub")
        self.combo.append_text("split")
        self.combo.append_text("fullmatch")
        self.combo.append_text("search")
        self.combo.set_sensitive(True)
        self.combo.set_active(0)
        self.combo.set_tooltip_text("Select the type of input")
        grid.attach(self.combo, 1, 1, 1, 1)
        grid.attach(Gtk.Label(label="Function:"), 0, 1, 1, 1)
        self.combo_label = Gtk.Label()
        grid.attach(self.combo_label, 1, 1, 1, 1)


        self.pattern_label = Gtk.Label(label="Pattern:")
        self.pattern_label.set_sensitive(True)
        self.pattern_label.set_tooltip_text("Regex pattern to match against the text")
        grid.attach(self.pattern_label, 0, 2, 1, 1)

        self.entry = Gtk.Entry()
        self.entry.set_sensitive(True)
        grid.attach(self.entry, 1, 2, 1, 1)


        self.entry.set_placeholder_text("Enter regex pattern")
        self.entry.set_tooltip_text("Enter a regex pattern to match against the text")
        self.entry.set_sensitive(True)
        self.entry.set_icon_from_icon_name(Gtk.EntryIconPosition.SECONDARY, "edit-find-symbolic")
        self.entry.set_icon_tooltip_text(Gtk.EntryIconPosition.SECONDARY, "Search")
        self.entry.set_icon_activatable(Gtk.EntryIconPosition.SECONDARY, True)
        self.entry.set_icon_sensitive(Gtk.EntryIconPosition.SECONDARY, True)
        self.entry.set_icon_tooltip_text(Gtk.EntryIconPosition.SECONDARY, "Search")

        grid.attach(Gtk.Label(label="Substitutions:"), 0, 3, 1, 1)
        self.subst_label = Gtk.Label()
        grid.attach(self.subst_label, 0, 3, 1, 1)

        self.subst = Gtk.Entry()
        self.subst.set_placeholder_text("Enter substitutions")
        grid.attach(self.subst, 1, 3, 1, 1)

        self.subst_label.set_tooltip_text("Substitutions made by the regex pattern")
        self.subst_label.set_sensitive(True)
        self.subst.set_icon_from_icon_name(Gtk.EntryIconPosition.SECONDARY, "edit-find-symbolic")
        self.subst.set_icon_tooltip_text(Gtk.EntryIconPosition.SECONDARY, "Substitutions")
        self.subst.set_icon_activatable(Gtk.EntryIconPosition.SECONDARY, True)
        self.subst.set_icon_sensitive(Gtk.EntryIconPosition.SECONDARY, True)

        grid.attach(Gtk.Label(label="Result:"), 0, 4, 1, 1)
        self.result_label = Gtk.Label()
        grid.attach(self.result_label, 1, 4, 1, 1)
        self.result_label.set_tooltip_text("Results found by the regex pattern")

        self.result = Gtk.Entry()
        self.result.set_sensitive(True)
        self.result.set_editable(False)
        self.result.set_can_focus(False)
        grid.attach(self.result, 1, 4, 1, 1)

        self.eval_button = Gtk.Button(label="Evaluate")
        self.eval_button.set_tooltip_text("Evaluate the regex pattern against the text")
        grid.attach(self.eval_button, 1, 5, 1, 1)


