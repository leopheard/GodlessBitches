from xbmcswift2 import Plugin, xbmcgui
from resources.lib import godlessbitches

plugin = Plugin()

URL = "https://www.spreaker.com/show/3254937/episodes/feed"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/cc755cd4f34de10f3a890235f533f573.jpg"},
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/cc755cd4f34de10f3a890235f533f573.jpg"},]

    return items


@plugin.route('/all_episodes/')
def all_episodes():
    """
    contains playable podcasts listed as just-in
    """
    soup = godlessbitches.get_soup(URL)
    
    playable_podcast = godlessbitches.get_playable_podcast(soup)
    
    items = godlessbitches.compile_playable_podcast(playable_podcast)

    return items


@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = godlessbitches.get_soup(URL)
    
    playable_podcast1 = godlessbitches.get_playable_podcast1(soup)
    
    items = godlessbitches.compile_playable_podcast1(playable_podcast1)

    return items


if __name__ == '__main__':
    plugin.run()
