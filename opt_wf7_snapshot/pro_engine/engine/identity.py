from .version import __version__, __name__

def banner():
    return f"""
================================
 {__name__}
 Version: {__version__}
 Host Monitoring Agent
================================
"""
