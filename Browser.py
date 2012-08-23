import sublime
import sublime_plugin
import webbrowser
import os
import sys
import platform


# Constant of settings file
SETTINGS = "browser.sublime-settings"

# All the global functions
def saveFile():
    sublime.active_window().run_command('save')
    print "\n\nSaved chages to the current file"

def getDomainConfig():
    return sublime.load_settings(SETTINGS).get('domains', {})

def getFileName(self):
    return self.view.file_name()[16:len(self.view.file_name())]

def getExtList():
    return ('.php','.html','.htm','.jsp','.cfm','.aspx','.asp','.xhtml')


# Open page in new browser
class OpenInNewBrowserWindowCommand(sublime_plugin.TextCommand):
  def run(self, edit):

    # Save the changes to the browser
    saveFile()

    # Get the domain to open
    for title, domain in getDomainConfig().items():
        url = domain + getFileName(self)

    # Check to see if the file can be displayed in the browser
    if self.view.file_name().endswith(getExtList()):
        if os.platform == "win32":
            print "Need to fix the error with windows"
        else:
            webbrowser.open(url)
    else:
        print "\nThis is not a browsable file\n"

class OpenInNewTabCommand(sublime_plugin.TextCommand):
  def run(self, edit):

    # Save the changes to the browser
    saveFile()

    # Get the domain to open
    for title, domain in getDomainConfig().items():
        url = domain + getFileName(self)

    # Check to see if the file can be displayed in the browser
    if self.view.file_name().endswith(getExtList()):
        if os.platform == "win32":
            print "Need to fix the error with windows"
        else:            
            webbrowser.open_new_tab(url)
    else:
        print "\nThis is not a browsable file\n"