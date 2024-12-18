from tkinter import *
from tkinter import ttk
import visualisation as vis
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Interface:
    def __init__(self, window, statements, upload_statement, file_handle):

        # set up
        self.window = window
        self.window.title("Expenses App")
        self.window.minsize(width=600, height=800)

        self.top_frame = Frame(self.window, width=500, height=400, borderwidth=10, relief=GROOVE)
        self.top_frame.pack()

        # frames for buttons of the month
        self.month_frame = Frame(self.top_frame, width=160, height=400, borderwidth=10, relief=GROOVE)
        self.month_frame.pack(side="left")

        self.month_frame_left = Frame(self.month_frame, width=160, height=400, borderwidth=10)
        self.month_frame_left.pack(side="left")

        self.month_frame_right = Frame(self.month_frame, width=160, height=400, borderwidth=10)
        self.month_frame_right.pack(side="left")

        self.middle_frame = Frame(self.window, width=500, height=50, borderwidth=10, relief=GROOVE)
        self.middle_frame.pack()
        self.bottom_frame = Frame(self.window, width=500, height=50, borderwidth=10, relief=GROOVE)
        self.bottom_frame.pack(padx=20)

        # handle inheritance
        self.upload_statement = upload_statement
        self.file_handle = file_handle

        # year drop down
        self.year_value = StringVar(self.middle_frame)
        self.year_value.set("2024")
        self.year_options = ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018",
                             "2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026"]
        self.year_dropdown = OptionMenu(self.middle_frame, self.year_value, *self.year_options,
                                        command=self.update_month_buttons)
        self.year_dropdown.pack(fill="both", padx=10)

        # statement handle
        self.statements = statements

        try:
            for statement in self.statements:
                self.selected_month = statement
            print(self.selected_month)
            self.selected_statement = self.statements[self.selected_month]

        except KeyError:
            self.selected_month = "jan" + "-" + self.year_value.get()
            print(self.selected_month)
            # self.selected_statement = self.statements[self.selected_month]

        # add pie
        self.pie_frame = Frame(self.top_frame)
        self.pie_frame.pack(side="left")
        self.bar_frame = Frame

        # month buttons
        self.add_month_buttons()

        # statement buttons
        self.btn_expenses = Button(self.middle_frame, text="Expenses", command=self.show_statement_expenses)
        self.btn_expenses.pack(side="left", fill="both", padx=10)

        self.btn_income = Button(self.middle_frame, text="Income", command=self.show_statement_income)
        self.btn_income.pack(side="left", fill="both", padx=10)

        self.btn_all = Button(self.middle_frame, text="All", command=self.show_statement_full)
        self.btn_all.pack(side="left", fill="both", padx=10)

        # display full statement by default
        self.treeview = None
        self.show_statement_full()
        self.add_pie()

    def update_month_buttons(self, selected_year):
        for widget in self.month_frame_left.winfo_children():
            widget.destroy()
        for widget in self.month_frame_right.winfo_children():
            widget.destroy()

        self.add_month_buttons()

    def add_month_buttons(self):
        btn_jan = Button(self.month_frame_left, text="January", pady=10, command=self.jan_btn_clicked)
        btn_jan.pack(fill="both")
        try:
            if self.statements["jan" + "-" + self.year_value.get()]:
                pass

        except KeyError:
            btn_jan.config(bg="#B7B7B7")

        btn_feb = Button(self.month_frame_right, text="February", pady=10, command=self.feb_btn_clicked)
        btn_feb.pack(fill="both")
        try:
            if self.statements["feb" + "-" + self.year_value.get()]:
                pass

        except KeyError:
            btn_feb.config(bg="#B7B7B7")

        btn_mar = Button(self.month_frame_left, text="March", pady=10, command=self.mar_btn_clicked)
        btn_mar.pack(fill="both")
        try:
            if self.statements["mar" + "-" + self.year_value.get()]:
                pass

        except KeyError:
            btn_mar.config(bg="#B7B7B7")

        btn_apr = Button(self.month_frame_right, text="April", pady=10, command=self.apr_btn_clicked)
        btn_apr.pack(fill="both")
        try:
            if self.statements["apr" + "-" + self.year_value.get()]:
                pass

        except KeyError:
            btn_apr.config(bg="#B7B7B7")

        btn_may = Button(self.month_frame_left, text="May", pady=10, command=self.may_btn_clicked)
        btn_may.pack(fill="both")
        try:
            if self.statements["may" + "-" + self.year_value.get()]:
                pass

        except KeyError:
            btn_may.config(bg="#B7B7B7")

        btn_jun = Button(self.month_frame_right, text="June", pady=10, command=self.jun_btn_clicked)
        btn_jun.pack(fill="both")
        try:
            if self.statements["jun" + "-" + self.year_value.get()]:
                pass

        except KeyError:
            btn_jun.config(bg="#B7B7B7")

        btn_jul = Button(self.month_frame_left, text="July", pady=10, command=self.jul_btn_clicked)
        btn_jul.pack(fill="both")
        try:
            if self.statements["jul" + "-" + self.year_value.get()]:
                pass

        except KeyError:
            btn_jul.config(bg="#B7B7B7")

        btn_aug = Button(self.month_frame_right, text="August", pady=10, command=self.aug_btn_clicked)
        btn_aug.pack(fill="both")
        try:
            if self.statements["aug" + "-" + self.year_value.get()]:
                pass

        except KeyError:
            btn_aug.config(bg="#B7B7B7")

        btn_sep = Button(self.month_frame_right, text="September", pady=10, command=self.sep_btn_clicked)
        btn_sep.pack(fill="both")
        try:
            if self.statements["sep" + "-" + self.year_value.get()]:
                pass

        except KeyError:
            btn_sep.config(bg="#B7B7B7")

        btn_oct = Button(self.month_frame_left, text="October", pady=10, command=self.oct_btn_clicked)
        btn_oct.pack(fill="both")
        try:
            if self.statements["oct" + "-" + self.year_value.get()]:
                pass

        except KeyError:
            btn_oct.config(bg="#B7B7B7")

        btn_nov = Button(self.month_frame_right, text="November", pady=10, command=self.nov_btn_clicked)
        btn_nov.pack(fill="both")
        try:
            if self.statements["nov" + "-" + self.year_value.get()]:
                pass

        except KeyError:
            btn_nov.config(bg="#B7B7B7")

        btn_dec = Button(self.month_frame_left, text="December", pady=10, command=self.dec_btn_clicked)
        btn_dec.pack(fill="both")
        try:
            if self.statements["dec" + "-" + self.year_value.get()]:
                pass

        except KeyError:
            btn_dec.config(bg="#B7B7B7")

    def display_statement(self, month_statement):
        if self.treeview:
            self.treeview.destroy()
        self.treeview = ttk.Treeview(self.bottom_frame, columns=list(month_statement.columns), show="headings")

        # Define columns and headings
        for col in month_statement.columns:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=150)

        # Insert DataFrame data into Treeview
        for row in month_statement.itertuples(index=False):
            self.treeview.insert("", "end", values=row)

        self.treeview.pack(padx=10, pady=10)

    def show_statement_income(self):
        try:
            self.display_statement(self.selected_statement.statement_income)

        except KeyError:
            print(f"No statement found for selected month {self.selected_month}\n"
                  f"please upload a statement for that month then try again")

    def show_statement_expenses(self):
        try:
            self.display_statement(self.selected_statement.statement_expenses)

        except KeyError:
            print(f"No statement found for selected month {self.selected_month}\n"
                  f"please upload a statement for that month then try again")

    def show_statement_full(self):
        try:
            self.display_statement(self.selected_statement.statement)

        except KeyError:
            print(f"No statement found for selected month {self.selected_month}\n"
                  f"please upload a statement for that month then try again")
        except AttributeError:
            print("No statements found. Please upload statement and try again.")

    def add_pie(self):
        try:
            # Group data for the pie chart
            grouped_data = self.selected_statement.statement_expenses.groupby("Category")["Debit Amount"].sum()

            # Create a new Matplotlib figure for the pie chart
            fig = vis.create_pie(grouped_data.index, grouped_data, "Expenses")

            # Clear the frame before adding the new canvas
            for widget in self.pie_frame.winfo_children():
                widget.destroy()

            # Embed the Matplotlib figure into the Tkinter frame
            canvas = FigureCanvasTkAgg(fig, master=self.pie_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=BOTH, expand=True)

        except AttributeError:
            print("No data available to display the pie chart.")

    def jan_btn_clicked(self):
        self.selected_month = "Jan" + "-" + self.year_value.get()
        try:
            self.selected_statement = self.statements[self.selected_month.lower()]
            self.show_statement_full()
            self.add_pie()

        except KeyError:
            file_name = self.selected_month.lower()
            self.upload_statement(file_name)

    def feb_btn_clicked(self):
        self.selected_month = "Feb" + "-" + self.year_value.get()
        try:
            self.selected_statement = self.statements[self.selected_month.lower()]
            self.show_statement_full()
            self.add_pie()

        except KeyError:
            file_name = self.selected_month.lower()
            self.upload_statement(file_name)

    def mar_btn_clicked(self):
        self.selected_month = "Mar" + "-" + self.year_value.get()
        try:
            self.selected_statement = self.statements[self.selected_month.lower()]
            self.show_statement_full()
            self.add_pie()

        except KeyError:
            file_name = self.selected_month.lower()
            self.upload_statement(file_name)

    def apr_btn_clicked(self):
        self.selected_month = "Apr" + "-" + self.year_value.get()
        try:
            self.selected_statement = self.statements[self.selected_month.lower()]
            self.show_statement_full()
            self.add_pie()

        except KeyError:
            file_name = self.selected_month.lower()
            self.upload_statement(file_name)

    def may_btn_clicked(self):
        self.selected_month = "May" + "-" + self.year_value.get()
        try:
            self.selected_statement = self.statements[self.selected_month.lower()]
            self.show_statement_full()
            self.add_pie()

        except KeyError:
            file_name = self.selected_month.lower()
            self.upload_statement(file_name)

    def jun_btn_clicked(self):
        self.selected_month = "Jun" + "-" + self.year_value.get()
        try:
            self.selected_statement = self.statements[self.selected_month.lower()]
            self.show_statement_full()
            self.add_pie()

        except KeyError:
            file_name = self.selected_month.lower()
            self.upload_statement(file_name)

    def jul_btn_clicked(self):
        self.selected_month = "Jul" + "-" + self.year_value.get()
        try:
            self.selected_statement = self.statements[self.selected_month.lower()]
            self.show_statement_full()
            self.add_pie()

        except KeyError:
            file_name = self.selected_month.lower()
            self.upload_statement(file_name)

    def aug_btn_clicked(self):
        self.selected_month = "Aug" + "-" + self.year_value.get()
        try:
            self.selected_statement = self.statements[self.selected_month.lower()]
            self.show_statement_full()
            self.add_pie()

        except KeyError:
            file_name = self.selected_month.lower()
            self.upload_statement(file_name)

    def sep_btn_clicked(self):
        self.selected_month = "Sep" + "-" + self.year_value.get()
        try:
            self.selected_statement = self.statements[self.selected_month.lower()]
            self.show_statement_full()
            self.add_pie()

        except KeyError:
            file_name = self.selected_month.lower()
            self.upload_statement(file_name)

    def oct_btn_clicked(self):
        self.selected_month = "Oct" + "-" + self.year_value.get()
        try:
            self.selected_statement = self.statements[self.selected_month.lower()]
            self.show_statement_full()
            self.add_pie()

        except KeyError:
            file_name = self.selected_month.lower()
            self.upload_statement(file_name)

    def nov_btn_clicked(self):
        self.selected_month = "Nov" + "-" + self.year_value.get()
        try:
            self.selected_statement = self.statements[self.selected_month.lower()]
            self.show_statement_full()
            self.add_pie()

        except KeyError:
            file_name = self.selected_month.lower()
            self.upload_statement(file_name)

    def dec_btn_clicked(self):
        self.selected_month = "Dec" + "-" + self.year_value.get()
        try:
            self.selected_statement = self.statements[self.selected_month.lower()]
            self.show_statement_full()
            self.add_pie()

        except KeyError:
            file_name = self.selected_month.lower()
            self.upload_statement(file_name)
