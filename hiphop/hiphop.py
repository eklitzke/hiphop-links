import argparse
import hashlib
import jinja2
import re

META_RE = re.compile(r'^(\d+-\d+-\d+ \d+:\d+:\d+)\s+(\S+)')

REGEXES = [
    re.compile(r'\b(https?://soundcloud.com\S+)'),
    re.compile(r'\b(https?://www.youtube.com\S+)'),
    re.compile(r'\b(https?://open.spotify.com\S+)'),
    re.compile(r'\b(https?://hypem.com\S+)'),
    re.compile(r'\b(https?://www.mixcloud.com\S+)'),
]

# top secret
MANGLE = frozenset([
    'SpencerFang',
])


def generate(title, input_file, output_file):
    seen = set()  # because things are relogged after restarting bitlbee
    links = []
    for line in input_file:
        for r in REGEXES:
            m = r.search(line)
            if m:
                link = m.groups()[0]
                m2 = META_RE.match(line)
                if not m2:
                    continue
                when, who = m2.groups()
                who = who.lstrip('@')
                if who == 'Link':
                    continue
                if who == '--':
                    continue
                key = (who, link)
                if key in seen:
                    continue
                else:
                    if who in MANGLE:
                        who = hashlib.sha1(who).hexdigest()[:8]
                    seen.add(key)
                    links.append((when, who, link))

    links.reverse()

    template_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader('templates/'),
        autoescape=True)
    template = template_env.get_template('index.html')
    output_file.write(template.render(links=links, title=title))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--title', default='hiphop links')
    parser.add_argument('--outfile', default='index.html')
    parser.add_argument('logfile')
    args = parser.parse_args()
    with open(args.logfile) as logfile:
        with open(args.outfile, 'w') as outfile:
            generate(args.title, logfile, outfile)


if __name__ == '__main__':
    main()
