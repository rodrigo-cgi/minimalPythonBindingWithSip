import os
from sipbuild import Option, Project


class FibProject(Project):
    """configuration options to specify the locations of the helloSip header file and library.

    You can do this only in the pyproject.toml file, but this is an example of how you can expand 
    your building project. 
    The sip-install command looks for a project.py file in the same folder of the sip and toml.
    After it it looks for a child class of sipbuild.Project

    """

    def get_options(self):
        """ Return the sequence of configurable options. """

        # Get the standard options.
        options = Project.get_options(self)

        # Add our new options.
        self.inc_dir_option = Option('hello-sip-include-dir',
                help="the directory containing helloSip.h", metavar="DIR")
        options.append(self.inc_dir_option)

        self.lib_dir_option = Option('hello-sip-library-dir',
                help="the directory containing the helloSip library",
                metavar="DIR")
        options.append(self.lib_dir_option)

        return options
