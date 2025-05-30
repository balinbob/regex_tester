# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later

import os
os.environ['GTK_DATA_PREFIX'] = 'C:\\msys64\\mingw64'
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GtkSource', '3.0')
import re
from gi.repository import Gtk, Gdk, GtkSource, Pango

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="My Regex Tester")
        self.set_border_width(10)
        self.set_default_size(600, 900)
        self.set_resizable(True)
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
        self.textview.set_accepts_tab(False)
        self.textview.set_cursor_visible(True)
        self.textview.set_hexpand(True)
        self.textview.set_vexpand(True)
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

        lang_path = r"C:\msys64\mingw64\share\gtksourceview-3.0\language-specs"
        lang_path = os.path.abspath(lang_path)  # Ensure it resolves cleanly

        lm = GtkSource.LanguageManager()
        lm.set_search_path([lang_path])


        buffer = GtkSource.Buffer()
        buffer.set_language(lm.get_language('regex')) #lm.get_language('python')
        print('language', buffer.get_language())
        GtkSource.StyleSchemeManager().get_scheme('classic')
        buffer.set_style_scheme(GtkSource.StyleSchemeManager().get_scheme('classic'))

        buffer.set_highlight_syntax(True)
        buffer.set_highlight_syntax(True)
        buffer.set_highlight_matching_brackets(True)

        overlay = Gtk.Overlay()
        overlay.set_hexpand(True)
        # overlay.set_vexpand(True)
        
        copy_button = Gtk.Button()
        icon = Gtk.Image.new_from_icon_name("edit-copy", Gtk.IconSize.BUTTON)
        copy_button.add(icon)
        copy_button.connect("clicked", self._on_copy_button_clicked)
        copy_button.set_tooltip_text("Copy the regex pattern to clipboard")

        overlay.add_overlay(copy_button)
        overlay.set_overlay_pass_through(copy_button, False)

        copy_button.set_halign(Gtk.Align.END)
        copy_button.set_valign(Gtk.Align.START)
        copy_button.set_margin_top(5)
        copy_button.set_margin_end(5)
        grid.attach(overlay, 1, 2, 1, 1)

        self.pattern = GtkSource.View.new_with_buffer(buffer)
        self.pattern.set_sensitive(True)

        self.pattern.modify_font(Pango.FontDescription("monospace 10 Bold"))
        self.pattern.set_tooltip_text("Enter a regex pattern to match against the text")
        self.pattern.set_sensitive(True)
        self.pattern.set_size_request(500, 100)
        self.pattern.set_accepts_tab(False)
        self.pattern.set_cursor_visible(True)
        
        overlay.add(self.pattern)

        grid.attach(Gtk.Label(label="Substitutions:"), 0, 3, 1, 1)
        self.subst_label = Gtk.Label()
        grid.attach(self.subst_label, 0, 3, 1, 1)


        self.subst = Gtk.Entry()
        self.subst.set_placeholder_text("Enter substitutions")
        grid.attach(self.subst, 1, 3, 1, 1)

        
        self.subst.modify_font(Pango.FontDescription("monospace 10 Bold"))
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

        self.result = Gtk.TextView()
        self.result.set_sensitive(True)
        self.result.set_editable(False)
        self.result.set_can_focus(False)
        self.result.set_wrap_mode(Gtk.WrapMode.WORD)
        self.result.set_tooltip_text("Results found by the regex pattern")
        self.result.set_size_request(500, 100)
        self.result.set_hexpand(True)
        self.result.set_vexpand(True)
        grid.attach(self.result, 1, 4, 1, 1)

    def _on_copy_button_clicked(self, button):
        buffer = self.pattern.get_buffer()
        text = buffer.get_text(buffer.get_start_iter(), buffer.get_end_iter(), False)
        clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        clipboard.set_text(text, -1)
