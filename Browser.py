import sublime
import sublime_plugin
import webbrowser

# Constant of settings file
SETTINGS = "browser.sublime-settings"

# The Browser Manager
class BrowserManager():
    
    def __init__(self):
        self.currWin = sublime.active_window()
        self.Settings = sublime.load_settings(SETTINGS)

    # Save the file in the current Window
    def saveFile(self):
        self.currWin.run_command('save')
        print "\nSaved changes to the current file"

    def getDomainConfig(self):
        return self.Settings.get('domains', {})

    def getSettings(self):
        return self.Settings

    def getExtList(self):
        return ('.php','.html','.htm','.jsp','.cfm','.aspx','.asp','.xhtml')
    
# Open page in new browser
class OpenInBrowserCommand(sublime_plugin.WindowCommand):
  
    def run(self):

        self.manager = BrowserManager()

        # Save the changes to the browser
        self.manager.saveFile()
        self.browserList = ["Internet Explorer", "FireFox", "Chrome", "Opera", "Safari"]

        # Get the domain to open
        for title, domain in self.manager.getDomainConfig().items():
            if self.manager.getSelectedDomain() == domain:
                url = domain + self.window.active_view().file_name()[16:len(self.window.active_view().file_name())]

        # Check to see if the file can be displayed in the browser
        if self.window.active_view().file_name().endswith(self.manager.getExtList()):
            if sublime.platform == "windows":
                webbrowser.get('windows-default').open(url)
            else:
                webbrowser.open(url)
        else:
            print "\nThis is not a browsable file\n"
  
# Add domain to the settings file
class AddDomainCommand(sublime_plugin.WindowCommand):
    
    def run(self):
        self.manager = BrowserManager()
        self.domSettings = self.manager.getSettings()
        self.domains = self.manager.getDomainConfig()
        self.domainName = "";
        self.domainType = "";
        self.window.show_input_panel("Enter Domain:",'', lambda txt: self.addDomain(txt),None,None)

    def addDomain(self, dom):
        self.domainName = dom
        self.window.show_input_panel("Enter Domain Type:",'', lambda txt: self.addDomainType(txt),None,None)

    def addDomainType(self, domType):
        self.domainType = domType
        self.domains[self.domainType] = self.domainName
        self.domSettings.set('domains', self.domains)