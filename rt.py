import re
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from mywindow import MyWindow


class DoIt:
    def __init__(self):
        self.window = MyWindow()
        self.window.connect("destroy", Gtk.main_quit)
        self.window.show_all()
        self.window.set_title("Regex Tester")

        self.window.eval_button.connect("clicked", self.on_eval_button_clicked)
        self.window.entry.connect("changed", self.on_entry_changed)
        self.window.subst.connect("changed", self.on_subst_changed)

        self.window.combo.connect("changed", self.on_combo_changed)
        buffer = self.window.textview.get_buffer()
        buffer.connect("changed", self.on_textview_changed)
    def on_textview_changed(self, widget):
        result = ''
        self.window.result.set_text(result)
    def on_entry_changed(self, widget):
        result = ''
        self.window.result.set_text(result)
        pattern = self.window.entry.get_text()
        repl = self.window.subst.get_text()
        buffer = self.window.textview.get_buffer()
        text = buffer.get_text(buffer.get_start_iter(),
                                     buffer.get_end_iter(), False)
        function = self.window.combo.get_active_text()
        result = None
        result = self.evaluate_regex(function, pattern, text, repl)
        self.window.result.set_text(str(result))

    def on_eval_button_clicked(self, widget):
        self.buffer = self.window.textview.get_buffer()
        text = self.buffer.get_text(self.buffer.get_start_iter(),
                                     self.buffer.get_end_iter(), False)
        pattern = self.window.entry.get_text()
        repl = self.window.subst.get_text()
        function = self.window.combo.get_active_text()
        result = None
        result = self.evaluate_regex(function, pattern, text, repl)
        print('pattern:', pattern)
        print('repl:', repl)
        print('result:', result)
        self.window.result.set_text(result)

    def on_subst_changed(self, widget):
        result = ''
        self.window.result.set_text(result)
        pattern = self.window.entry.get_text()
        repl = self.window.subst.get_text()
        buffer = self.window.textview.get_buffer()
        text = buffer.get_text(buffer.get_start_iter(),
                                     buffer.get_end_iter(), False)
        function = self.window.combo.get_active_text()
        result = None
        result = self.evaluate_regex(function, pattern, text, repl)
        self.window.result.set_text(str(result))

    def on_combo_changed(self, widget):
        result = ''
        self.window.result.set_text(result)
        pattern = self.window.entry.get_text()
        repl = self.window.subst.get_text()
        buffer = self.window.textview.get_buffer()
        text = buffer.get_text(buffer.get_start_iter(),
                                     buffer.get_end_iter(), False)
        result = None
        function = self.window.combo.get_active_text()
        if function == "sub":
            self.window.subst.set_sensitive(True)
            self.window.subst_label.set_sensitive(True)
        else:
            self.window.subst.set_sensitive(False)
        result = self.evaluate_regex(function, pattern, text, repl)
        self.window.result.set_text(str(result))

    def evaluate_regex(self, function, pattern, text, repl=None):
        """Evaluate the regex function based on the selected option."""
        try:
            pattern = re.compile(pattern)
        except re.error as e:
            print(e)
            return f"Regex error: {e}"
        if function == "match":
            result = re.match(pattern, text)
        elif function == "findall":
            result = re.findall(pattern, text)
        elif function == "sub":
            result = re.sub(pattern, repl, text)
        elif function == "split":
            result = re.split(pattern, text)
        elif function == "fullmatch":
            result = re.fullmatch(pattern, text)
        elif function == "search":
            result = re.search(pattern, text)
        else:
            result = None
        return result

if __name__ == "__main__":
    DoIt()
    Gtk.main()
