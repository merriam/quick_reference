""" Docker quick reference - Creates the Docker Quick Reference HTML. """

# Copyright (c) 2013 Charles Merriam

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from markdown import markdown
from quick import *   # yes, it is intimate with this code



def docker_useful_links():
    docker = links_line("Docker Linux container runtime", [
        ("https://www.docker.io", "Overview"),
        ("http://docker.readthedocs.org/en/latest/", "Documentation"),
        ("https://github.com/dotcloud/docker/", "GitHub repository"),
        ("https://github.com/dotcloud/docker/issues?state=open", "Bugs and Issues"),
        ("irc://chat.freenode.net/docker", "IRC"),
        ("http://stackoverflow.com/questions/tagged/docker", "Stack Overflow"),
        ("https://github.com/dotcloud/docker/blob/master/LICENSE", "License")
        ])

    golang = links_line("Go (GoLang) programming language", [
        ("http://golang.org", "Overview"),
        ("http://golang.org/doc/", "Documentation"),
        ("http://code.google.com/p/go/source/browse", "Source Repo"),
        ("https://code.google.com/p/go/issues/list", "Bugs and Issues"),
        ("http://stackoverflow.com/questions/tagged/go", "Stack Overflow"),
        ("http://golang.org/LICENSE", "License")
        ])
        # ("https://groups.google.com/forum/#!forum/golang-announce", "Announcements"),


    virtbox = links_line("VirtualBox VM manager by Oracle", [
        ("https://www.virtualbox.org", "Overview"),
        ("https://www.virtualbox.org/wiki/Documentation", "Documentation"),
        ("https://www.virtualbox.org/wiki/Downloads", "Download"),
        ("https://www.virtualbox.org/browser/vbox/trunk", "Source Repo"),
        ("https://www.virtualbox.org/wiki/Licensing_FAQ", "License")
        ])
    vagrant = links_line("Vagrant VM creation DSL", [
        ("http://www.vagrantup.com", "Overview"),
        ("http://docs.vagrantup.com/v2/", "Documentation"),
        ("http://www.vagrantbox.es", "Box list"),
        ("https://github.com/mitchellh/vagrant", "GitHub Repository"),
        ("http://stackoverflow.com/questions/tagged/vagrant", "Stack Overflow"),
        ("https://github.com/mitchellh/vagrant/blob/master/LICENSE", "License")
        ])
    chef = links_line("Chef configuration management by OpsCode", [
        ("http://www.getchef.com/chef/", "Overview"),
        ("", "Documentation"),
        ("https://github.com/opscode/chef", "GitHub Repository"),
        ("", "Stack Overflow"),
        ("", "License")
        ])
    puppet = links_line("Puppet configuration management", [
        ("", "Overview"),
        ("", "Documentation"),
        ("", "GitHub Repository"),
        ("", "Stack Overflow"),
        ("", "License")])
    return link_section("Useful Links", (docker, golang, virtbox, vagrant, chef, puppet))

def docker_glossary():
    """ returns a glossary for docker """
    # docker
    # lxc
    # union file system -> aufs
    # configuration management
    # package manager (brew/apt/yum & (pip/pypi),(pyrus/pear), etc)
    # vm (xen, oracle, etc)
    # image, container, image repository
    # dsl
    # """ All images are made up of a set of cumulative layers.
    # A container is a process in a box.  The box, an image,  has a filesystem, system libraries, a network stack but no running process."""

    return ""

def check_both(list1, list2):
    """ what is different between list1 and items in the list of lists """

    list1_set = set(list1.keys())
    list2_set = set()
    for list_of_items in list2.values():
        list2_set.update(list_of_items)
    diff = list1_set.symmetric_difference(list2_set)

    if diff:
        print("Difference = ", diff)


def old_docker_commands():
    """ return command line options with dockerfile equivalents """
    cmds = {
        "attach" : "Attach to a running container",
        "build" : "Build a container from a Dockerfile",
        "commit" : "Create a new image from a container's changes",
        "cp" : "Copy files/folders from the containers filesystem to the host path",
        "diff" : "Inspect changes on a container's filesystem",
        "events" : "Get real time events from the server",
        "export" : "Stream the contents of a container as a tar archive",
        "history" : "Show the history of an image",
        "images" : "List images",
        "import" : "Create a new filesystem image from the contents of a tarball",
        "info" : "Display system-wide information",
        "insert" : "Insert a file in an image",
        "inspect" : "Return low-level information on a container",
        "kill" : "Kill a running container",
        "load" : "Load image from a tar archive",
        "login" : "Register or Login to the docker registry server",
        "logs" : "Fetch the logs of a container",
        "port" : "Lookup the public-facing port which is NAT-ed to PRIVATE_PORT",
        "top" : "Lookup the running processes of a container",
        "ps" : "List containers",
        "pull" : "Pull an image or a repository from the docker registry server",
        "push" : "Push an image or a repository to the docker registry server",
        "restart" : "Restart a running container",
        "rm" : "Remove one or more containers",
        "rmi" : "Remove one or more images",
        "run" : "Run a command in a new container",
        "save" : "Save an image to a tar archive",
        "search" : "Search for an image in the docker index",
        "start" : "Start a stopped container",
        "stop" : "Stop a running container",
        "tag" : "Tag an image into a repository",
        "version" : "Show the docker version information",
        "wait" : "Block until a container stops, then print its exit code"
        }

    groups = { 'files' : ['cp', 'diff', 'insert', 'export', 'import', 'load', 'save'],
               'info' : ['events', 'history', 'images', 'info', 'inspect', 'logs', 'top', 'ps', 'version', 'port'],
               'image' : ['commit', 'restart', 'rmi', 'run', 'start', 'stop', 'tag', 'wait'],
               'container' : ['attach', 'build', 'kill', 'rm'],
               'repos' : ['login', 'push', 'pull', 'search'] }

    check_both(cmds, groups)

    p = ["Docker Commands"]

    for name in sorted(groups.keys()):
        bodies = []
        for cmd in groups[name]:
            bodies.append([cmd, cmds[cmd]])
        p.append(table(name, name, [], bodies))

    return "\n".join(p)

def subheader(name, length=3):
    toc_add(name, subheading=True)
    p = [ anchor(name) + '<div class="subheader">{}</div>'.format(name) ]
    for _ in range(1, length):
        p.append('<div class="subheader">&nbsp;</div>')
    return p

def docker_commands():
    # c = container, r = repository or image set, R = registry, i = image, l = local system
    exp = ("**export** *CONTAINER*",
           "Export **container** filesystem as tar file to *stdout*.  Use like "
           "`docker export a6e5 > a6e5_files.tar`", "(2)")
    imp = ("**import** `-` **|** *url* *[*REPOSITORY*[*:TAG*]**]*",
           "Import tar file of filesystem into new **image**. "
            "Source can be `-` for stdin, like `docker import - < a6ef_files.tar`. "
            " Alternately, source can be an *http* or *https* URL.  Also, the "
            "optional *REPOSITORY* or *REPOSITORY:TAG* will `docker tag` the new image, like "
            "`docker import server.com/files.tar charlesmerriam/dwarf:in_progress`", "")
    cp = ("**cp** *CONTAINER*:*path* *path*",
          "Recursively copy a file or directory out of a **container** filesystem to the local "
          "(host) filesystem.  So, `docker cp a6e5:/var/log .` would copy the directory tree "
          "from the container into a new subdirectory `./log`, while "
          "`docker cp a6e5:var/log/dpkg.log dpkg` copy a single file from the container to "
          "a local *existing directory* `dpkg/dpkg.log`.", "(2)")
    diff = ("**diff** *CONTAINER*", "List differences between the filesytem of the *container* "
            "and the filesystem of the *image* in which it ran.  Output lines have a "
            "code letter for **C**hanged, **D**eleted, or **A**dded followed by the file or "
            "directory name.  Run like `docker diff a6e5`.", "(1)")
    # TODO:  These are just tossed in from the docs and not explored
    insert = ("**insert** *IMAGE* *URL* *PATH*",
              "Insert a file from URL into the IMAGE at PATH, creating a new image. "
              "Returns the new image ID.  It also creates a new container as a side effect.","")
    load = ("**load** *SOURCE*", "Load an image from a tar archive", "")
    save = ("**save** *IMAGE*", "Save an image to a tar archive streamed to *stdout*. "
            "Use like `docker save e71d > e71d.tar`", "")

    events = ('**events** [-since="*timestamp*"]', "Get real time events from the server, "
        "optionally including previous events from the current docker deaemon like "
        '`docker events -since="2013-01-01 04:48:23"`.  Quick with Ctrl-C')
    history = ('**history** [-q][-notrunc] *IMAGE*', "Show the history of an *image*, detailing "
        "which images and commands were used in its creation.   Use `-q` to show only the "
        "IDs and `-notrunc` to show full width IDs and commands", "")
    inspect = ('**inspect** [-format="*go-template*"] *containers_or_images*',
               'Return JSON dump on one or more containers or images.  This dump contains'
               'all metadata and settings.')
    images = ("**images** [-notrunc] [-q]<br>&nbsp;&nbsp;&nbsp;[-a|-tree|-viz|*IMAGE_REGEX*]",
        "List images on your local system.  "
        "`-q` lists IDs only while `-notrunc` prints long IDs.  With no other arguments,"
        "the command prints all images and `-a` will also list intermediate build images."
        "`-tree` and `-viz` print a tree of image ancestory as text or "
        "graphviz format.  Finally, "
        "providing image name or regex lists matching images, like"
        '`docker images "u*"`.', "(3)(4)")

    info = ("**info**", "Display system wide information including the number of containers and images.")

    version = ("**version**", "Display docker version information including the golang version "
               " and git branch of both the client and server.")


    logs = ("**logs** [-f] *container*", "Fetch transcript of *stdout* and *stderr* of "
            "container, outputing to both *stdout* and *stderr*, like "
            "`docker logs ae4d > last.stdout.txt 2> last.stderr.txt`.  Use `-f` to "
            "output transcript and then follow "
            "continuing output of a running container.")

    login = ("**login** [`-e=`*email*] [`-p=`*password*] [`-u=`*username] [*ServerURL*]",
             "Login to a repository, or the {} by default.  Also used to create an account, "
             "which is followed up with a confirmation email.  Login is required for "
             "`docker push`".format(
                 link("https://index.docker.io", "Public Docker Index")), "(5)")

    pull = ('**pull** [-t="*tag_name*"] *IMAGE_SET*',
            "Pull an image set (also called a repository) from the registry.  Use `-t` to pull"
            "only one tagged image from the set, like "
            '`docker pull -t="latest" charlesmerriam/ping`. '
            , "(7)")

    push = ('**push** *image-set*', "Push an image or image set (also called a repository) "
           "to the registry, like `push charlesmerriam/ping2:latest`.  Prompts for login "
           "information unless logged in.", "(7)")

    search = ("**search** [-notrunc] [-stars=*mininum_stars*] [-trusted] *TERM*",
              "Search for images in the {} with *TERM* matching in the name or description "
              "of the image.  You can filter by *mininum_stars* or select only *trusted* "
              "repositories, like `docker search -stars=2 -trusted git`.  Use `-notrunc` to "
              "see the full descriptions.".format(
                 link("https://index.docker.io", "Public Docker Index")), "(6)")
    top = ("**top** *CONTAINER* [-ps_options]",
           "Lists the running processes of a container, like the Unix `top` command. "
           "The *ps_options*, which are listed **after** the *container_id*, can be `-notrunc` "
           "or any of the many ps flags.   You can see a list of options by using a valid "
           "container_id, like `docker top 5e34 -?`.")
    ps = ("**ps** [-q] [-notrunc]", "")
    port = ("**port** CONTAINER PRIVATE_PORT", "Lookup the public-facing port which is NAT-ed to PRIVATE_PORT")

    commit = ("**commit** [OPTIONS] CONTAINER [REPOSITORY[:TAG]]",
              "Create a new image from a container's changes")
    tag = ("**tag**", "Tag an image into a repository")
    rmi = ("**rmi**", "Remove one or more images.")

    run = ("**run** *image* [Command]", "Run a command in a new container.  Lots and lots of options.")
    stop = ("**stop** [-t=*seconds*] *container_list*", "Stop a running container (Send SIGTERM, and then SIGKILL after grace period)")
    start = ("**start** [-a] [-i]", "Restart a stopped container.")
    wait = ("**wait** *container_list*", "Block until containers stop, printing exit code of each container as it finishes.")

    restart = ("**restart** [t=*seconds*", "Restart, meaning stop and then start, a running container.  `-t` is the grace period in seconds to allow container to finish.")
    attach = ("**attach** [-nostdin] [-sig-proxy]", "Attach to a running container")
    build = ("**build** [-q] [-no-cache] [-rm] [-t=*new_name_and_tag*]", "Build a new container image from the source code at PATH.")
    kill = ("**kill** *container_list*", "Kill a running container (send SIGKILL).")
    rm = ("**rm** [-link] [-v] *container-list*", "Remove one or more containers.")

    cmds = [ subheader('File Systems'), imp, exp, load, save, diff, insert, cp,
             subheader('Docker System Information'), events, info, version,
             subheader('Container and Image Status'), history, inspect, images, logs,
                  top, ps, port,
             subheader("Running Images"), run, start, stop, restart, wait,
             subheader("More images"), commit, tag, rmi,
             subheader("Containers"), attach, build, kill, rm,
             subheader('Working with repositories'), login, push, pull, search,

            ]

    see_also = "The {} may have additional examples.\n<br>\n".format(
        link("http://docs.docker.io/en/latest/commandline/cli/", "Command Line Documentation"))
    notes = markdown("* (1) The `docker diff` command lists *aufs* internal files.  These "
                     "files are in the root directory and start with `.wh..wh.`.\n"
                     "* (2) Use `docker export` to copy an entire filesystem; current "
                     "limitations return `Killed` otherwise.\n"
                     "* (3) Current limitations cause `docker image` to ignore the "
                     "`*IMAGE*` and `-q` flags when used with `-tree` or `-viz`.\n"
                     "* (4) You can display graphviz format at "
                     + link("http://graphviz-dev.appspot.com") +
                     " or run locally like `docker images -viz | dot -Tpng -o tree.png`.\n"
                     ' * (5) Your login is stored in ~/.dockercfg.  Remove it to logout.\n'
                     " * (6) The *TERM* uses spaces to denote OR, so "
                     '`docker search "cassandra mysql"` searches documents with `cassandra` or '
                     '`mysql` in either the name or description of the image.   A `*` '
                     'means "followed later by the second term", but use `grep` for AND, like '
                     '`docker search --notrunc sql | grep -i centos`.  Alternately, use the ' +
                     link("https://index.docker.io", "Public Docker Index") +
                     "webpage to search.\n"
                     ' * (7) The `docker run` command also has this functionality.\n'
                     ' * (8) The *image_set* may be the top level public repository, like '
                     '`ubuntu`; in an account of the public repostiory, like '
                     '`charlesmerriam/ubuntu`; '
                     'or in a private repostory, like `localhost:5000/ubuntu`.\n'
                     '* (9) See '+
                     link("http://golang.org/pkg/text/template/") + ' for the Go Language '
                     'template package.'
                     )

    return table1(name="Docker Commands",
                  caption="Organized by type",
                  widths=[150, 270, 10],
                  headers=[
                      link("http://docs.docker.io/en/latest/commandline/cli/", "Command"),
                      "Meaning", "Notes"],
                  cell_lines=cmds) + see_also + notes

def docker_projects():
    wharf = (link("http://dockerwharf.com", "Wharf"), "Try available services quickly using "
             "this open source Software as a Service.")
    stackdock = (link("https://stackdock.com", "StackDock"), "Hosting docker containers on SSD "
                 "based hosts.")
    return table1(name="Projects Related to Docker",
                  headers=['Project', 'Description'],
                  cell_lines=[ stackdock, wharf])

def front_matter():
    toc_add("Front Matter")
    p = [ section_title("Front Matter") ]
    p.append("Client version 0.7.1.  Server version 0.7.1. ({})".format(
        link("http://blog.docker.io/2013/11/docker-0-7-docker-now-runs-on-any-"
             "linux-distribution/", "What's new?")))
    # TODO:  Add spam proofing here.
    p.append('<b>Please</b> report inaccuracies, oversights, and bugs to the ' +
             link("https://github.com/merriam/quick_reference/issues",
                  "GitHub merriam/quick_reference repository"))
    p.append('<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">'
             '<img alt="Creative Commons License" style="border-width:0" '
             'src="http://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />'
             'This work is licensed under a <a rel="license" '
             'href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons '
             'Attribution-NonCommercial-ShareAlike 4.0 International License</a>.')
    p.append("This is a work in progress, last updated in 12/2013.")
    p.append("Webpage design based on {}.".format(
             link("http://rgruet.free.fr/PQR27/PQR2.7.html",
                  "Richard Gruet's Python Quick Reference")))
    return "\n<br>\n".join(p)

def docker_main():
    """ put out the Docker quick reference guide """


    sections = [
           front_matter(),
           docker_useful_links(),
           docker_glossary(),
           docker_commands(),
           docker_projects(),
    ]   # evaluate first so toc is ready

    print( head("Docker Quick Reference"),
           toc(),
           "\n".join(sections),
           tail()
        )

if __name__ == "__main__":
    docker_main()
