from CTkToolTip import CTkToolTip

class SafeToolTip(CTkToolTip):
    def _show(self):
        # Não tenta exibir um tooltip destruído.
        if not self.winfo_exists():
            return

        # Se o botão não existe mais, encerra o tooltip.
        if not self.widget.winfo_exists():
            self.destroy()
            return

        # Mantém o comportamento original da biblioteca.
        super()._show()
