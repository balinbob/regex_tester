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

    def on_eval_button_clicked(self, widget):
        self.buffer = self.window.textview.get_buffer()
        text = self.buffer.get_text(self.buffer.get_start_iter(),
                                     self.buffer.get_end_iter(), False)
        pattern = self.window.entry.get_text()
        repl = self.window.subst.get_text()
        result = re.sub(pattern, repl, text)
        print('pattern:', pattern)
        print('repl:', repl)
        print('result:', result)
        self.window.matches.set_text(result)




if __name__ == "__main__":
    DoIt()
    Gtk.main()