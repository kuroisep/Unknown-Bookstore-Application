class CustomTreeview(ttk.Treeview):
            def __init__(self, parent, *args, **kwargs):
                ttk.Treeview.__init__(self, parent, *args, **kwargs)
                self.vanilla_xview = tk.XView.xview

            def xview(self, *args):
                #   here's our multiplier
                multiplier = 100

                if 'units' in args:
                    #   units in args - user clicked the arrows
                    #   time to build a new args with desired increment
                    mock_args = args[:1] + (str(multiplier * int(args[1])),) + args[2:]
                    return self.vanilla_xview(self, *mock_args)
                else:
                    #   just do default things
                    return self.vanilla_xview(self, *args)