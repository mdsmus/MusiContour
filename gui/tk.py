#!/usr/bin/env python
# -*- coding: utf-8 -*-

import contour.contour
import contour.diagonal
import contour.matrix
import contour.comparison
import contour.utils
import contour.plot
import Tkinter

sw_name = "Villa-Lobos Contour Module"
version = "0.2"


class App:

    def __init__(self, master):

        ### widgets

        font = 'sans 8 bold'
        self.initial = Tkinter.Label(master, text=sw_name + " v." + version, font=font)

        self.text_output = Tkinter.Text(master)
        self.text_scroll = Tkinter.Scrollbar(master)
        self.text_scroll.config(command=self.text_output.yview)
        self.text_output.config(yscrollcommand=self.text_scroll.set)

        self.main_label = Tkinter.Label(master, text='main entry:')
        self.main_entry = Tkinter.Entry(master, width=13)
        self.main_entry.focus()
        self.main_entry.insert('end', "2 6 3 7 9 1")
        self.main_entry.get()

        self.secondary_label = Tkinter.Label(master, text='second. entry:')

        self.secondary_entry = Tkinter.Entry(master, width=13)
        self.secondary_entry.insert("end", "1")
        self.secondary_entry.get()

        ## buttons

        self.b_clear_output = Tkinter.Button(master, text="Clear Output",
                                     command=self.clear_output, width=10)
        self.b_clear_plot = Tkinter.Button(master, text="Clear Plot",
                               command=self.clear_plot, width=10)
        self.b_clear_main = Tkinter.Button(master, text="Clear Main",
                               command=self.clear_main, width=10)
        self.b_clear_secondary = Tkinter.Button(master, text="Clear Second.",
                               command=self.clear_secondary, width=10)
        self.b_plot = Tkinter.Button(master, text="Plot", command=self.plot,
                           width=10)
        self.b_normal_form = Tkinter.Button(master, text="Normal form",
                                     command=self.normal_form, width=10)
        self.b_prime_form = Tkinter.Button(master, text="Prime form",
                                    command=self.prime_form, width=10)
        self.b_inversion = Tkinter.Button(master, text="Inversion",
                                   command=self.inversion, width=10)
        self.b_rotation = Tkinter.Button(master, text="Rotation",
                               command=self.rotation, width=10)
        self.b_retrograde = Tkinter.Button(master, text="Retrograde",
                                    command=self.retrograde, width=10)
        self.b_ret_inv = Tkinter.Button(master, text="Retrograde inv.",
                                 command=self.ret_inv, width=10)
        self.b_comparison_matrix = Tkinter.Button(master, text="COM Matrix",
                               command=self.comparison_matrix, width=10)
        self.b_n_subsets = Tkinter.Button(master, text="n subsets",
                               command=self.n_subsets, width=10)
        self.b_all_subsets = Tkinter.Button(master, text="All subsets",
                               command=self.all_subsets, width=10)
        self.b_internal = Tkinter.Button(master, text="Int. Diagonal",
                               command=self.internal, width=10)
        self.b_csegs_from_int = Tkinter.Button(master, text="Csegs from INT",
                               command=self.csegs_from_int, width=10)
        self.b_casv = Tkinter.Button(master, text="CASV",
                               command=self.casv, width=10)
        self.b_cis = Tkinter.Button(master, text="CIS",
                               command=self.cis, width=10)
        self.b_ccvi = Tkinter.Button(master, text="CCV I",
                               command=self.ccvi, width=10)
        self.b_ccvii = Tkinter.Button(master, text="CCV II",
                               command=self.ccvii, width=10)
        self.b_cia = Tkinter.Button(master, text="CIA",
                               command=self.cia, width=10)
        self.b_contour_compare = Tkinter.Button(master, text="Contour simil.",
                               command=self.contour_compare, width=10)
        self.b_contour_reduction = Tkinter.Button(master, text="Contour red.",
                               command=self.contour_reduction, width=10)
        self.b_segment_classes = Tkinter.Button(master, text="Cseg classes",
                               command=self.segment_classes, width=10)

        ## key bindings:
        for x in [self.main_entry, master, self.secondary_entry]:
            x.bind("<Escape>", self.clear_plot)
            x.bind("<Control-Escape>", self.clear_output)
            x.bind("<Alt-Escape>", self.clear_main)

            x.bind("<Return>", self.plot)
            x.bind("<p>", self.prime_form)
            x.bind("<n>", self.normal_form)
            x.bind("<r>", self.retrograde)
            x.bind("<R>", self.rotation)
            x.bind("<i>", self.inversion)
            x.bind("<I>", self.ret_inv)

            x.bind("<M>", self.comparison_matrix)
            x.bind("<d>", self.internal)
            x.bind("<s>", self.n_subsets)
            x.bind("<S>", self.all_subsets)
            x.bind("<c>", self.csegs_from_int)
            x.bind("<C>", self.contour_compare)

            x.bind("<a>", self.casv)
            x.bind("<x>", self.cia)
            x.bind("<v>", self.ccvi)
            x.bind("<V>", self.ccvii)

            x.bind("<e>", self.contour_reduction)

        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)
        master.columnconfigure(2, weight=1)
        master.columnconfigure(3, weight=1)

        ## displacement
        ## row 0
        self.initial.grid(row=0, column=0, columnspan=5)

        ## row 1
        self.text_output.grid(row=1, column=0, columnspan=4)
        self.text_scroll.grid(row=1, column=4, sticky=Tkinter.N + Tkinter.S)

        ## row 2
        self.main_label.grid(row=2, column=0)
        self.main_entry.grid(row=2, column=1)
        self.secondary_label.grid(row=2, column=2)
        self.secondary_entry.grid(row=2, column=3)

        ## row 3
        self.b_clear_output.grid(row=3, column=0)
        self.b_clear_plot.grid(row=3, column=1)
        self.b_clear_main.grid(row=3, column=2)
        self.b_clear_secondary.grid(row=3, column=3)

        ##row 4
        self.b_plot.grid(row=4, column=0)
        self.b_normal_form.grid(row=4, column=1)
        self.b_prime_form.grid(row=4, column=2)
        self.b_inversion.grid(row=4, column=3)

        ## row 5
        self.b_rotation.grid(row=5, column=0)
        self.b_retrograde.grid(row=5, column=1)
        self.b_ret_inv.grid(row=5, column=2)
        self.b_comparison_matrix.grid(row=5, column=3)

        ## row 6
        self.b_n_subsets.grid(row=6, column=0)
        self.b_all_subsets.grid(row=6, column=1)
        self.b_internal.grid(row=6, column=2)
        self.b_csegs_from_int.grid(row=6, column=3)

        ## row7
        self.b_casv.grid(row=7, column=0)
        self.b_cis.grid(row=7, column=1)
        self.b_ccvi.grid(row=7, column=2)
        self.b_ccvii.grid(row=7, column=3)

        ## row 8
        self.b_cia.grid(row=8, column=0)
        self.b_contour_compare.grid(row=8, column=1)
        self.b_contour_reduction.grid(row=8, column=2)
        self.b_segment_classes.grid(row=8, column=3)

    ## functions

    def plot(self, event=None):
        get = self.main_entry.get()
        cseg = [int(x) for x in get.split(' ') if x]
        plot_color = 'k'
        result = contour.contour.Contour(cseg).str_print()
        text = "Original: "
        self.text_output.insert(Tkinter.END, text)
        self.text_output.insert(Tkinter.END, result)
        self.text_output.insert(Tkinter.END, "\n")
        contour.plot.plot_preview(cseg, plot_color, "Original")

    def prime_form(self, event=None):
        get = self.main_entry.get()
        cseg = [int(x) for x in get.split(' ') if x]
        plot_color = 'b'
        # Returns csegclass only if cseg has not repeated elements
        if len(set(cseg)) == len(cseg):
            tmp = contour.contour.Contour(cseg).contour_segment_class()
            card, c_class, pr_form, ri = tmp
            pr_form_vis = contour.contour.Contour(pr_form).str_print()
            if ri == True:
                ri = "*"
            else:
                ri = ""
            result = "{0}-{1}{2} {3}".format(card, c_class, ri, pr_form_vis)
        else:
            pr_form = contour.contour.Contour(cseg).pr_form()
            pr_form_vis = contour.contour.Contour(pr_form).str_print()
            result = "{0}".format(pr_form_vis)
        text = "Prime form: "
        self.text_output.insert(Tkinter.END, text)
        self.text_output.insert(Tkinter.END, result)
        self.text_output.insert(Tkinter.END, "\n")
        contour.plot.plot_preview(pr_form, plot_color, "Prime form")

    def normal_form(self, event=None):
        get = self.main_entry.get()
        cseg = [int(x) for x in get.split(' ') if x]
        plot_color = 'g'
        normal_form = contour.contour.Contour(cseg).translation()
        result = contour.contour.Contour(normal_form).str_print()
        text = "Normal form: "
        self.text_output.insert(Tkinter.END, text)
        self.text_output.insert(Tkinter.END, result)
        self.text_output.insert(Tkinter.END, "\n")
        contour.plot.plot_preview(normal_form, plot_color, "Normal form")

    def retrograde(self, event=None):
        get = self.main_entry.get()
        cseg = [int(x) for x in get.split(' ') if x]
        plot_color = 'm'
        retrograde = contour.contour.Contour(cseg).retrograde()
        result = contour.contour.Contour(retrograde).str_print()
        text = "Retrograde: "
        self.text_output.insert(Tkinter.END, text)
        self.text_output.insert(Tkinter.END, result)
        self.text_output.insert(Tkinter.END, "\n")
        contour.plot.plot_preview(retrograde, plot_color, "Retrograde")

    def inversion(self, event=None):
        get = self.main_entry.get()
        cseg = [int(x) for x in get.split(' ') if x]
        plot_color = 'r'
        inversion = contour.contour.Contour(cseg).inversion()
        result = contour.contour.Contour(inversion).str_print()
        text = "Inversion: "
        self.text_output.insert(Tkinter.END, text)
        self.text_output.insert(Tkinter.END, result)
        self.text_output.insert(Tkinter.END, "\n")
        contour.plot.plot_preview(inversion, plot_color, "Inversion")

    def ret_inv(self, event=None):
        get = self.main_entry.get()
        cseg = [int(x) for x in get.split(' ') if x]
        plot_color = 'c'
        ret = contour.contour.Contour(cseg).retrograde()
        ret_inv = contour.contour.Contour(ret).inversion()
        result = contour.contour.Contour(ret_inv).str_print()
        text = "Ret. Inv.: "
        self.text_output.insert(Tkinter.END, text)
        self.text_output.insert(Tkinter.END, result)
        self.text_output.insert(Tkinter.END, "\n")
        contour.plot.plot_preview(ret_inv, plot_color, "Ret.inv.")

    def rotation(self, event=None):
        get = self.main_entry.get()
        second_get = int(self.secondary_entry.get())
        cseg = [int(x) for x in get.split(' ') if x]
        size = len(get)
        # returns a color for each rotation factor
        plot_color = str((second_get / float(size) * .8) + .1)
        rotation = contour.contour.Contour(cseg).rotation(second_get)
        result = contour.contour.Contour(rotation).str_print()
        text = "Rotation ({0}): ".format(second_get)
        self.text_output.insert(Tkinter.END, text)
        self.text_output.insert(Tkinter.END, result)
        self.text_output.insert(Tkinter.END, "\n")
        contour.plot.plot_preview(rotation, plot_color, "Rotation({0})".format(second_get))

    def internal(self, event=None):
        get = self.main_entry.get()
        cseg = [int(x) for x in get.split(' ') if x]
        second_get = int(self.secondary_entry.get())
        int_diag = contour.contour.Contour(cseg).internal_diagonals(second_get)
        format_int_diag = contour.diagonal.InternalDiagonal(int_diag).str_print()
        text = "Internal diagonal ({0}): ".format(second_get)
        self.text_output.insert(Tkinter.END, text)
        self.text_output.insert(Tkinter.END, format_int_diag)
        self.text_output.insert(Tkinter.END, "\n")

    def comparison_matrix(self, event=None):
        get = self.main_entry.get()
        cseg = [int(x) for x in get.split(' ') if x]
        com_matrix = contour.contour.Contour(cseg).comparison_matrix()
        com_matrix_str = contour.matrix.ComparisonMatrix(com_matrix).str_print()
        text = "Comparison Matrix:\n"
        self.text_output.insert(Tkinter.END, text)
        self.text_output.insert(Tkinter.END, com_matrix_str)
        self.text_output.insert(Tkinter.END, "\n")

    def contour_reduction(self, event=None):
        get = self.main_entry.get()
        cseg = [int(x) for x in get.split(' ') if x]
        cseg_obj = contour.contour.Contour(cseg)
        [reduced_c, depth] = cseg_obj.contour_reduction_algorithm()
        reduced_c_print = contour.contour.Contour(reduced_c).str_print()
        text1 = "Morris Contour Reduction\n"
        text2 = "Original:{0}\n".format(cseg_obj.str_print())
        result = "Reduction: {0}\nDepth: {1}".format(reduced_c_print, depth)
        self.text_output.insert(Tkinter.END, text1)
        self.text_output.insert(Tkinter.END, text2)
        self.text_output.insert(Tkinter.END, result)
        self.text_output.insert(Tkinter.END, "\n")

    def n_subsets(self, event=None):
        get = self.main_entry.get()
        cseg = [int(x) for x in get.split(' ') if x]
        cseg_obj = contour.contour.Contour(cseg)
        cseg_print = contour.contour.Contour(cseg).str_print()
        second_get = int(self.secondary_entry.get())
        csubset_normal = cseg_obj.subsets_normal(second_get)
        normal_gr = contour.contour.subsets_grouped(csubset_normal, "normal")
        csubset_prime = contour.contour.Contour(cseg).subsets_prime(second_get)
        prime_gr = contour.contour.subsets_grouped(csubset_prime, "prime")
        plural = "s" if second_get > 1 else ""
        txt1 = "Original: {0}\n".format(cseg_print)
        txt2 = "Contour subsets ({0} element{1}):\n".format(second_get, plural)
        sep1 = ("-" * 22) + "\n"
        sep2 = ("=" * 22) + "\n"
        txt3 = sep2 + "Grouped by normal form\n" + sep1
        txt4 = "\n" + sep2 + "Grouped by prime form\n" + sep1
        self.text_output.insert(Tkinter.END, txt1)
        self.text_output.insert(Tkinter.END, txt2)
        self.text_output.insert(Tkinter.END, txt3)
        self.text_output.insert(Tkinter.END, normal_gr)
        self.text_output.insert(Tkinter.END, txt4)
        self.text_output.insert(Tkinter.END, prime_gr)
        self.text_output.insert(Tkinter.END, "\n")

    def all_subsets(self, event=None):
        get = self.main_entry.get()
        cseg = [int(x) for x in get.split(' ') if x]
        cseg_print = contour.contour.Contour(cseg).str_print()
        csubset_normal = contour.contour.Contour(cseg).all_subsets_normal()
        normal_gr = contour.contour.subsets_grouped(csubset_normal, "normal")
        csubset_prime = contour.contour.Contour(cseg).all_subsets_prime()
        prime_gr = contour.contour.subsets_grouped(csubset_prime, "prime")
        text1 = "Original: {0}\nAll contour subsets:\n".format(cseg_print)
        sep1 = ("-" * 22) + "\n"
        sep2 = ("=" * 22) + "\n"
        text2 = sep2 + "Grouped by normal form\n" + sep1
        text3 = "\n" + sep2 + "Grouped by prime form\n" + sep1
        self.text_output.insert(Tkinter.END, text1)
        self.text_output.insert(Tkinter.END, text2)
        self.text_output.insert(Tkinter.END, normal_gr)
        self.text_output.insert(Tkinter.END, text3)
        self.text_output.insert(Tkinter.END, prime_gr)
        self.text_output.insert(Tkinter.END, "\n")

    def csegs_from_int(self, event=None):
        get = self.main_entry.get()
        int_d = contour.utils.replace_plus_minus_to_list(get)
        if sorted(int_d)[-1] > 1:
            text = "ERROR: Insert Internal diagonal in main entry:\n- + -\n"
            self.text_output.insert(Tkinter.END, text)
        else:
            second_get = int(self.secondary_entry.get())
            csegs = contour.diagonal.InternalDiagonal(int_d).csegs(second_get)
            result = "\n".join([contour.contour.Contour(x).str_print() for x in csegs])
            plural = "s" if second_get > 1 else ""
            text = "Csegs:\n"
            self.text_output.insert(Tkinter.END, text)
            self.text_output.insert(Tkinter.END, result)
            self.text_output.insert(Tkinter.END, "\n")

    def casv(self, event=None):
        get = self.main_entry.get()
        cseg = [int(x) for x in get.split(' ') if x]
        casv = contour.contour.Contour(cseg).contour_adjacency_series_vector()
        text = "Contour Adjacency Series Vector:\n"
        self.text_output.insert(Tkinter.END, text)
        self.text_output.insert(Tkinter.END, casv)
        self.text_output.insert(Tkinter.END, "\n")

    def cis(self, event=None):
        get = self.main_entry.get()
        cseg = [int(x) for x in get.split(' ') if x]
        cis = contour.contour.Contour(cseg).contour_interval_succession()
        result = contour.contour.Contour(cis).str_print()
        text = "Contour Interval Succession:\n"
        self.text_output.insert(Tkinter.END, text)
        self.text_output.insert(Tkinter.END, result)
        self.text_output.insert(Tkinter.END, "\n")

    def cia(self, event=None):
        get = self.main_entry.get()
        cseg = [int(x) for x in get.split(' ') if x]
        cia = list(contour.contour.Contour(cseg).contour_interval_array())
        text = "Contour Interval Array:\n"
        self.text_output.insert(Tkinter.END, text)
        self.text_output.insert(Tkinter.END, cia)
        self.text_output.insert(Tkinter.END, "\n")

    def ccvi(self, event=None):
        get = self.main_entry.get()
        cseg = [int(x) for x in get.split(' ') if x]
        ccvi = list(contour.contour.Contour(cseg).contour_class_vector_i())
        text = "Contour class vector I:\n"
        self.text_output.insert(Tkinter.END, text)
        self.text_output.insert(Tkinter.END, ccvi)
        self.text_output.insert(Tkinter.END, "\n")

    def ccvii(self, event=None):
        get = self.main_entry.get()
        cseg = [int(x) for x in get.split(' ') if x]
        ccvii = list(contour.contour.Contour(cseg).contour_class_vector_ii())
        text = "Contour class vector II:\n"
        self.text_output.insert(Tkinter.END, text)
        self.text_output.insert(Tkinter.END, ccvii)
        self.text_output.insert(Tkinter.END, "\n")

    def contour_compare(self, event=None):
        get1 = self.main_entry.get()
        get2 = self.secondary_entry.get()
        cseg1 = [int(x) for x in get1.split(' ') if x]
        cseg2 = [int(x) for x in get2.split(' ') if x]
        cseg1_p = contour.contour.Contour(cseg1).str_print()
        cseg2_p = contour.contour.Contour(cseg2).str_print()
        tmp = contour.comparison.cseg_similarity_compare(cseg1, cseg2)
        [operation, result] = tmp
        text1 = "{0}: {1:.2f}\n".format(operation, result)
        text2 = "Cseg 1: {0}\nCseg 2: {1}".format(cseg1_p, cseg2_p)
        self.text_output.insert(Tkinter.END, text1)
        self.text_output.insert(Tkinter.END, text2)
        self.text_output.insert(Tkinter.END, "\n")

    def segment_classes(self, event=None):
        result = contour.contour.print_contour_classes(7)
        self.text_output.insert(Tkinter.END, result)
        self.text_output.insert(Tkinter.END, "\n")

    def clear_output(self, event=None):
        self.text_output.delete(0.0, Tkinter.END)

    def clear_plot(self, event=None):
        clear_plot()

    def clear_main(self, event=None):
        self.main_entry.delete(0, Tkinter.END)

    def clear_secondary(self, event=None):
        self.secondary_entry.delete(0, Tkinter.END)


def gui():
    root = Tkinter.Tk()
    root.title(sw_name)
    root.geometry('450x580+0+0')
    root.resizable(Tkinter.FALSE, Tkinter.FALSE)

    app = App(root)

    root.mainloop()
