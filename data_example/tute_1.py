import tkinter as tk

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.status = tk.Label(self, anchor="w")
        self.status.pack(side="bottom", fill="x")
        self.text = tk.Text(self, wrap="word", width=40, height=8)
        self.text.pack(fill="both", expand=True)
        self.text.bind('<Triple-1>', self.on_text_button)
        for n in range(1,20):
            self.text.insert("end", "this is line %s\n" % n)


    def on_text_button(self, event):
        index = self.text.index("@%s,%s" % (event.x, event.y))
        line, char = index.split(".")
        self.status.configure(text="you clicked line %s" % line)

if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()

