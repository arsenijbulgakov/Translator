"""UI logic of the app."""
import gettext
import tkinter as tk
from tkinter import Entry, ttk

import model

translation = gettext.translation("msg", "po", fallback=True)
_, ngettext = translation.gettext, translation.ngettext


class SampleApp(tk.Tk):
    """Class for main tkinter window."""

    languages_from = ["ru", "en", "zh"]
    languages_to = ["ru", "en", "zh"]
    print(_("The weights of the model are being loaded, please wait"))
    print(_("This process can usually take up to 2 minutes"))
    local_model = None
    lang_from = None
    lang_to = None
    outp = None
    inp_text = None

    def __init__(self):
        """Set params of the window."""
        tk.Tk.__init__(self)
        self._frame = None
        self.geometry('400x300')
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class, lang_f="strange", lang_t="strange", inp_text=None):
        """Destroys current frame and replaces it with a new one."""
        if lang_f == "" or lang_t == "":
            return
        if lang_f in self.languages_from:
            self.lang_from = lang_f
        elif lang_t != "strange":
            return
        if lang_f in self.languages_to:
            self.lang_to = lang_t
            self.local_model.change_dst_lang(lang_t)
        elif lang_f != "strange":
            return

        if inp_text is not None:
            self.inp_text = inp_text
            self.outp = self.local_model.translate(inp_text)

        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    """Class for start page window."""

    def __init__(self, master):
        """Set params of the start page window."""
        tk.Frame.__init__(self, master)
        tk.Button(self, text=_("Go to the translation"),
                  command=lambda: master.switch_frame(ChooseLanguage)).pack()
        master.local_model = model.TranslateModel()


class ChooseLanguage(tk.Frame):
    """Class for choosing language window."""

    def __init__(self, master):
        """Set params of the choosing language window."""
        tk.Frame.__init__(self, master)
        tk.Label(self, text=_("Translate from:")).pack()
        languages_from = ["ru", "en", "zh"]
        languages_to = ["ru", "en", "zh"]
        combobox_from = ttk.Combobox(self, values=languages_from, state="readonly")
        combobox_from.pack()
        tk.Label(self, text=_("Translate to:")).pack()
        combobox_to = ttk.Combobox(self, values=languages_to, state="readonly")
        combobox_to.pack()

        def _command_func():
            return master.switch_frame(TranslatePage, lang_f=combobox_from.get(), lang_t=combobox_to.get())

        b = tk.Button(self, text=_("Confirm!"), command=_command_func)
        b.pack()


class TranslatePage(tk.Frame):
    """Class for translation window."""

    def __init__(self, master):
        """Set params of the translation window."""
        tk.Frame.__init__(self, master)
        tk.Label(self, text=_("Text for translation")).pack()
        input_entry = Entry(self, bg="lightgreen")
        input_entry.pack()
        tk.Button(self, text=_("Translate"), command=lambda: master.switch_frame(ResultPage, inp_text=input_entry.get())).pack()


class ResultPage(tk.Frame):
    """Class for result window."""

    def __init__(self, master):
        """Set params of the result window."""
        tk.Frame.__init__(self, master)
        printable_text = f"{master.inp_text}->{master.outp}"
        tk.Label(self, text=printable_text).pack(side="top", fill="x", pady=10)
        master.outp = None
        tk.Button(self, text=_("Translate another text"),
                  command=lambda: master.switch_frame(TranslatePage)).pack()
        tk.Button(self, text=_("Change the translation language"),
                  command=lambda: master.switch_frame(ChooseLanguage)).pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
