import wx
import wx.media


class MusicPlayerApp(wx.Frame):
    def __init__(self, parent=None, id=-1):
        wx.Frame.__init__(self, parent, id, 'Music Player using Python', size=(600, 300))
        self.panel = wx.Panel(self)

        mySizer = wx.BoxSizer(wx.VERTICAL)

        self.mc = wx.media.MediaCtrl(self.panel)
        mySizer.Add(self.mc, 0, wx.ALL | wx.EXPAND, 5)

        self.playButton = wx.Button(self.panel, -1, label='Play', size=(80, -1))
        mySizer.Add(self.playButton, 0, wx.ALL | wx.CENTER, 5)
        self.playButton.Disable()
        self.Bind(wx.EVT_BUTTON, self.onPlay, self.playButton)

        loadButton = wx.Button(self.panel, -1, label='Load', size=(80, -1))
        mySizer.Add(loadButton, 0, wx.ALL | wx.CENTER, 5)
        self.Bind(wx.EVT_BUTTON, self.onLoadFile, loadButton)

        pauseButton = wx.Button(self.panel, -1, label='Pause', size=(80, -1))
        mySizer.Add(pauseButton, 0, wx.ALL | wx.CENTER, 5)
        self.Bind(wx.EVT_BUTTON, self.onPause, pauseButton)

        stopButton = wx.Button(self.panel, -1, label='Stop', size=(80, -1))
        mySizer.Add(stopButton, 0, wx.ALL | wx.CENTER, 5)
        stopButton.Bind(wx.EVT_BUTTON, self.onStop, stopButton)

        self.slider = wx.Slider(self.panel, -1, 0, 0, 100, size=(300, -1))
        self.Bind(wx.EVT_SLIDER, self.onSeek, self.slider)
        mySizer.Add(self.slider, 0, wx.ALL | wx.CENTER, 5)

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.onTimer, self.timer)

        self.panel.SetSizer(mySizer)

        self.panel.SetBackgroundColour('#f0f0f0')
        self.playButton.SetBackgroundColour('#e9e9e9')
        loadButton.SetBackgroundColour('#e9e9e9')
        pauseButton.SetBackgroundColour('#e9e9e9')
        stopButton.SetBackgroundColour('#e9e9e9')

        font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.heading = wx.StaticText(self.panel, label='Music Player using Python', size=(300, 40), style=wx.ALIGN_CENTRE)
        self.heading.SetForegroundColour('#007acc')
        self.heading.SetFont(font)

        mySizer.Insert(0, self.heading, 0, wx.ALL | wx.EXPAND, 5)
        self.status_label = wx.StaticText(self.panel, label="No song loaded", size=(300, 20), style=wx.ALIGN_CENTRE)
        mySizer.Insert(1, self.status_label, 0, wx.ALL | wx.EXPAND, 5)

        self.Show()

    def onLoadFile(self, event):
        wildcard = "*.mp3;*wav"
        style = wx.FD_OPEN
        fileDialog = wx.FileDialog(self, "Choose a file", wildcard=wildcard, style=style)
        if fileDialog.ShowModal() == wx.ID_OK:
            path = fileDialog.GetPath()
            self.mc.Load(path)
            self.status_label.SetLabel(f"Loaded Song: {fileDialog.GetFilename()}")
            self.playButton.Enable()

        fileDialog.Destroy()

    def onPlay(self, event):
        self.mc.Play()
        self.timer.Start(100)
        audio_length = self.mc.Length()
        self.slider.SetRange(0, audio_length)

    def onPause(self, event):
        self.mc.Pause()

    def onStop(self, event):
        self.mc.Stop()
        self.slider.SetValue(0)

    def onTimer(self, event):
        updateslider = self.mc.Tell()
        self.slider.SetValue(updateslider)

    def onSeek(self, event):
        dragslider = self.slider.GetValue()
        self.mc.Seek(dragslider)


if __name__ == '__main__':
    app = wx.App()
    frame = MusicPlayerApp()
    app.MainLoop()
