class VideoMetadata:

    def __init__(self, parser):

        self.title = None
        self.description = None
        self.published = None
        self.author = None
        self.views = None
        self.likes = None
        self.dislikes = None

        self._get_video_metadata(parser)

    def _get_video_metadata(self, parser):
        """Searches the page for video metadata (uploaded, author, description, etc)"""

        self._parse_title(parser)
        self._parse_description(parser)
        self._parse_published(parser)
        self._parse_author(parser)
        self._parse_views(parser)
        self._parse_likes_dislikes(parser)

        print(vars(self))

    def _parse_title(self, parser):

        title = parser.title.string
        if title:
            self.title = title.replace(' - YouTube', '')

    def _parse_description(self, parser):

        description_block = parser.find('div', id="description")
        if description_block:
            self.description = '\n'.join(description_block.strings)

    def _parse_published(self, parser):

        date_block = parser.find('span', class_="date", slot="date")
        if date_block and date_block.string:
            date = date_block.string.replace('Published on ', '')
            self.published = date

    def _parse_author(self, parser):

        owner = parser.find('yt-formatted-string', id="owner-name")
        if owner and owner.a and owner.a.string:
            self.author = owner.a.string

    def _parse_views(self, parser):

        count_block = parser.find('span', class_='view-count')
        if count_block and count_block.string:
            count = count_block.string.replace(' views', '')
            self.views = count

    def _parse_likes_dislikes(self, parser):

        views_block = parser.find_all('yt-formatted-string', id="text", class_='ytd-toggle-button-renderer')
        if views_block and views_block[0]['aria-label']:
            likes = views_block[0]['aria-label'].replace(' likes', '').replace(' like', '')
            self.likes = likes

        if views_block and views_block[1]['aria-label']:
            dislikes = views_block[1]['aria-label'].replace(' dislikes', '').replace(' dislike', '')
            self.dislikes = dislikes

    def to_json(self):

        json = {'title': self.title,
                'description': self.description,
                'published': self.published,
                'author':self.author,
                'views': self.views,
                'likes': self.likes,
                'dislikes': self.dislikes}

        return json
