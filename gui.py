import wx
import numpy as np
from model_utils import load_model

# Load ML model
model = load_model()


class CarPriceFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Car Price Predictor', size=(520, 700))

        # Use a panel
        panel = wx.Panel(self)
        panel.SetBackgroundColour("#f5f5f5")  # light modern grey

        main_box = wx.BoxSizer(wx.VERTICAL)

        # ==== HEADER ====
        header = wx.StaticText(panel, label="Car Price Prediction System")
        header_font = wx.Font(16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        header.SetFont(header_font)
        header.SetForegroundColour("#333333")
        main_box.Add(header, flag=wx.ALIGN_CENTER | wx.TOP, border=20)

        main_box.Add((-1, 20))  # spacer

        # Fields dictionary
        self.fields = {}

        # Labels with improved wording
        labels = [
            "Year you bought the car",
            "Price you bought the car for (in lakh)",
            "Total Kilometers Driven",
            "Fuel Type  (Petrol=0, Diesel=1, CNG=2)",
            "Seller Type (Dealer=0, Individual=1)",
            "Transmission (Manual=0, Automatic=1)",
            "Number of Previous Owners (0/1/2/3)"
        ]

        # ==== INPUT FIELDS ====
        for label in labels:
            box = wx.BoxSizer(wx.VERTICAL)

            lbl = wx.StaticText(panel, label=label)
            lbl.SetForegroundColour("#444444")
            lbl_font = wx.Font(11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
            lbl.SetFont(lbl_font)

            txt = wx.TextCtrl(panel, style=wx.BORDER_SIMPLE)
            txt.SetBackgroundColour("#ffffff")
            txt.SetForegroundColour("#000000")
            txt.SetFont(wx.Font(10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

            self.fields[label] = txt

            box.Add(lbl, flag=wx.LEFT | wx.BOTTOM, border=5)
            box.Add(txt, flag=wx.EXPAND | wx.ALL, border=5)

            main_box.Add(box, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=20)

        # ==== PREDICT BUTTON ====
        btn = wx.Button(panel, label="Predict Price", size=(200, 40))
        btn.SetBackgroundColour("#4CAF50")
        btn.SetForegroundColour("white")
        btn_font = wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        btn.SetFont(btn_font)
        btn.Bind(wx.EVT_BUTTON, self.on_predict)

        main_box.Add(btn, flag=wx.ALIGN_CENTER | wx.TOP, border=25)

        # ==== RESULT BOX ====
        self.result = wx.StaticText(panel, label="")
        self.result.SetForegroundColour("#2a2a2a")
        result_font = wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.result.SetFont(result_font)

        main_box.Add(self.result, flag=wx.ALIGN_CENTER | wx.TOP, border=25)

        panel.SetSizer(main_box)
        self.Centre()
        self.Show()

    def on_predict(self, event):
        try:
            # Extract values in correct model order
            values = [float(self.fields[key].GetValue()) for key in self.fields]

            data = np.array(values).reshape(1, -1)

            prediction = model.predict(data)[0]

            self.result.SetLabel(f"Estimated Selling Price: ₹ {prediction:.2f} lakh")

        except Exception as e:
            self.result.SetLabel("⚠ Please fill all fields with valid numbers.")


class App(wx.App):
    def OnInit(self):
        CarPriceFrame()
        return True


if __name__ == "__main__":
    app = App()
    app.MainLoop()
