#!/usr/bin/python3


def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text


def main():
    print_h1 = html_tag('h1')
    print_h1('Test Headline!')
    print_h1('Another Headline!')
    
    print_p = html_tag('p')
    print_p('Test Paragraph!')


if __name__ == '__main__':
    main()
