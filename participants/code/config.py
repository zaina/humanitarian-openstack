from ConfigParser import ConfigParser

def get_config(path="libcloud.conf"):
    """Load a configuration file to find provider-specific options."""
    cp = ConfigParser()
    cp.read(path)

    def to_dict(items):
        """Shortcut to create a dictionary from ConfigParser item lists."""
        return dict((item[0], item[1]) for item in items)

    if "active" in cp.sections():
        active = to_dict(cp.items("active"))
    else:
        raise Exception("No active section found in %s." % path)

    conf = to_dict(cp.items(active["provider"]))
    # Update the dictionary to include the `active` section.
    conf.update(active)
    
    return conf
