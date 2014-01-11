import os

symlinksdirname = 'symlinks'
# name of the location of source files to be symlinked

symlinksdir = os.getcwd() + '/' + symlinksdirname + '/'
contents = os.listdir(symlinksdir)
for content in contents:
    os.symlink(symlinksdir + content, '/home/macrman/.' + content)

