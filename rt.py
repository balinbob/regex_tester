import os
os.environ['GTK_DATA_PREFIX'] = 'C:\\msys64\\mingw64'
import re
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GtkSource', '3.0')
from gi.repository import Gtk, GtkSource
from mywindow import MyWindow


class DoIt:
    def __init__(self):
        """
        Initialize the DoIt object.

        This method creates a MyWindow instance and sets it up. It
        connects the window's destroy signal to Gtk.main_quit, shows
        the window, and sets its title. It then calls the
        _connect_signals method to connect the rest of the signals.

        :return: None
        """
        self.buffer = None
        self.window = MyWindow()
        self.window.connect("destroy", Gtk.main_quit)
        self.window.show_all()
        self.window.set_title("Regex Tester")

        self._connect_signals()

    def _connect_signals(self):
        """Connect the signals."""
        pattern_buffer = self.window.pattern.get_buffer()
        pattern_buffer.connect("changed", self._on_entry_changed)
        self.window.subst.connect("changed", self._on_subst_changed)

        self.window.combo.connect("changed", self._on_combo_changed)
        textbuffer = self.window.textview.get_buffer()
        textbuffer.connect("changed", self._on_textview_changed)

    def _get_input_fields(self):
        """Get the text from the pattern entry, substitution entry,
        textview buffer and the selected function from the combo box.

        :return: A tuple containing the pattern, substitution string,
                 text from the textview buffer and the function name.
        :rtype: tuple
        """
        pattern_buffer = self.window.pattern.get_buffer()
        pattern = pattern_buffer.get_text(pattern_buffer.get_start_iter(),
                                        pattern_buffer.get_end_iter(), False)
        # pattern = self.window.pattern.get_buffer().get_text()
        repl = self.window.subst.get_text()
        buffer = self.window.textview.get_buffer()
        text = buffer.get_text(buffer.get_start_iter(),
                               buffer.get_end_iter(), False)
        function = self.window.combo.get_active_text()
        return pattern, repl, text, function

    def _all_together_now(self):
        result = ''
        self.window.result.get_buffer().set_text(result)
        pattern, repl, text, function = self._get_input_fields()
        print('result', result)
        print('pattern', pattern)
        print('repl', repl)
        print('text', text)
        print('function', function)
        result = self._evaluate_regex(function, pattern, text, repl)
        self.window.result.get_buffer().set_text(str(result))

    def _on_textview_changed(self, _widget) -> None:
        """Clear the result text buffer when the text buffer content changes."""
        result_buffer = self.window.result.get_buffer()
        result_buffer.set_text("", -1)
    def _on_entry_changed(self, _widget):
        """Called when the text in the pattern entry changes.

        Evaluates the regex using the currently selected function and
        displays the result in the result text buffer.

        :param widget: The widget that triggered this signal. Unused.
        :type widget: Gtk.Widget
        :return: None
        """
        self._all_together_now()

    def _on_subst_changed(self, _widget):
        """Called when the text in the substitution pattern changes.

        Evaluates the regex using the currently selected function and
        displays the result in the result text buffer.

        :param widget: The widget that triggered this signal. Unused.
        :type widget: Gtk.Widget
        :return: None
        """
        self._all_together_now()

    def _on_combo_changed(self, combo):
        """Called when the selected item in the combo box changes.

        Enables or disables the substitution entry and label based on the
        selected function. Then calls _all_together_now to re-evaluate the regex.

        :param combo: The combo box widget that triggered this signal.
        :type combo: Gtk.ComboBoxText
        :return: None
        """
        function = combo.get_active_text()
        is_sub = function == "sub"
        self.window.subst.set_sensitive(is_sub)
        self.window.subst_label.set_sensitive(is_sub)
        self._all_together_now()

    def _evaluate_regex(self, function, pattern, text, repl=None):
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
            if repl is None:
                return "No replacement pattern provided."
            if not isinstance(repl, str):
                repl = repl.pattern
            if not isinstance(text, str):
                text = str(text)
            try:
                result = re.sub(pattern, repl, text)
            except re.error as e:
                print(e, 'yyy')
                return f"Regex error: {e}"
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
