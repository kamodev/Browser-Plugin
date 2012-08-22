import sublime, sublime_plugin
import webbrowser, os

SETTINGS = "browser.sublime-settings"

class OpenInNewBrowserWindowCommand(sublime_plugin.TextCommand):
  def run(self, edit):

    # The settings for the plugin
    config = sublime.load_settings(SETTINGS).get('domains', {})
        
    # Save the file
    sublime.active_window().run_command('save')
    print "\n\nSaved chages to the current file"

    #url = "http://10.10.10.12/mobile/"
    for title, domain in config.items():
        url = domain + self.view.file_name()[16:len(self.view.file_name())]
    
    if self.view.file_name().endswith(('.php','.html','.htm','.jsp','.cfm','.aspx','.asp','.xhtml')):
        webbrowser.open(url)
    else:
        print "\nThis is not a browsable file\n"


class OpenInNewTabCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # The settings for the plugin
    config = sublime.load_settings(SETTINGS).get('domains', {})

    # Save the file
    sublime.active_window().run_command('save')
    print "\n\nSaved chages to the current file"

    #url = "http://10.10.10.12/mobile/"
    for title, domain in config.items():
        url = domain + self.view.file_name()[16:len(self.view.file_name())]
    
    if self.view.file_name().endswith(('.php','.html','.htm','.jsp','.cfm','.aspx','.asp','.xhtml')):
        webbrowser.open_new_tab(url)
    else:
        print "\nThis is not a browsable file\n"