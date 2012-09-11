import sublime
import sublime_plugin
import webbrowser
import os
import sys
import platform


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
class OpenInNewBrowserWindowCommand(sublime_plugin.WindowCommand):
  
    def run(self):

        self.manager = BrowserManager()

        # Save the changes to the browser
        self.manager.saveFile()

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
        #print "\n\n\nUser entered: " + dom + "\n\n\n"
        self.domainName = dom
        self.window.show_input_panel("Enter Domain Type:",'', lambda txt: self.addDomainType(txt),None,None)
        # self.currWin.show_quick_panel(["Test", "Mobile", "Paytiva"], None)

    def addDomainType(self, domType):
        self.domainType = domType
        #print "\n\n\nUser domain type entered: " + domType + "\n\n\n"
        self.domains[self.domainType] = self.domainName
        
        # Print the domains
        # for title, domain in self.domains.items():
        #    print title + ":" + domain

        self.domSettings.set('domains', self.domains)

        

       
class OpenInNewTabCommand(sublime_plugin.TextCommand):
  def run(self, edit):

    # Save the changes to the browser
    BrowserManager.saveFile()

    # Get the domain to open
    for title, domain in BrowserManager.getDomainConfig().items():
        url = domain + BrowserManager.getFileName(self)

    # Check to see if the file can be displayed in the browser
    if self.view.file_name().endswith(BrowserManager.getExtList()):
        if sys.platform == "win32":
            print "Need to fix the error with windows"
        else:            
            webbrowser.open_new_tab(url)
    else:
        print "\nThis is not a browsable file\n"