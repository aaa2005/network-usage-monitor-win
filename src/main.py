
import time
import threading
import netusage
import customtkinter as ck


class App(ck.CTk):
    def __init__(self):
        super().__init__()

        # main setup 
        self.title("Network Usage Monitor")
        self.geometry("300x300")
        self.resizable(False,False)

        # first row
        self.Interface = ck.CTkLabel(self, text="Interfaces")
        self.Interface.grid(row=1, column=1, padx=20, pady=20)

        self.Download = ck.CTkLabel(self, text="Downloaded")
        self.Download.grid(row=1, column=2, padx=20, pady=20)

        self.Upload = ck.CTkLabel(self, text="Uploaded")
        self.Upload.grid(row=1, column=3, padx=20, pady=20)

        # second row 
        self.inter1 = ck.CTkLabel(self, text="Updating")
        self.inter1.grid(row=2, column=1, padx=20, pady=20)

        self.in1 = ck.CTkLabel(self, text="Updating")
        self.in1.grid(row=2, column=2, padx=20, pady=20)

        self.out1 = ck.CTkLabel(self, text="Updating")
        self.out1.grid(row=2, column=3, padx=20, pady=20)

        # therd row
        self.inter2 = ck.CTkLabel(self, text="Updating")
        self.inter2.grid(row=3, column=1, padx=20, pady=20)

        self.in2 = ck.CTkLabel(self, text="Updating")
        self.in2.grid(row=3, column=2, padx=20, pady=20)

        self.out2 = ck.CTkLabel(self, text="Updating")
        self.out2.grid(row=3, column=3, padx=20, pady=20)

        # forth row
        self.inter3 = ck.CTkLabel(self, text="Updating")
        self.inter3.grid(row=4, column=1, padx=20, pady=20)

        self.in3 = ck.CTkLabel(self, text="Updating")
        self.in3.grid(row=4, column=2, padx=20, pady=20)

        self.out3 = ck.CTkLabel(self, text="Updating")
        self.out3.grid(row=4, column=3, padx=20, pady=20)


        self.auto_refresh()

    def get_inters(self):
        interfaces = netusage.usage_info()
        data = list()
        for inter in interfaces:
            data.append([inter.name, inter.byteIn, inter.byteOut])
        return data

    def format_bytes(self, size):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
            if size < 1024.0:
                return f"{size:.2f} {unit}"
            size /= 1024.0
        return f"{size:.2f} PB"

    def update_data(self):
        infos = self.get_inters() 

        var1 = infos[0][0]
        var2 = infos[1][0]
        var3 = infos[2][0]

        # inter
        self.inter1.configure(text=var1)
        self.inter2.configure(text=var2)
        self.inter3.configure(text=var3)
        ########
        var1 = self.format_bytes(infos[0][1])
        var2 = self.format_bytes(infos[1][1])
        var3 = self.format_bytes(infos[2][1])

        # in

        self.in1.configure(text=var1)
        self.in2.configure(text=var2)
        self.in3.configure(text=var3)
        ########
        var1 = self.format_bytes(infos[0][2])
        var2 = self.format_bytes(infos[1][2])
        var3 = self.format_bytes(infos[2][2])

        # out
        self.out1.configure(text=var1)
        self.out2.configure(text=var2)
        self.out3.configure(text=var3)


    def auto_refresh(self):
        def loop():
            while True:
                self.update_data()
                time.sleep(2)
        threading.Thread(target=loop, daemon=True).start()

app = App()
app.mainloop()

