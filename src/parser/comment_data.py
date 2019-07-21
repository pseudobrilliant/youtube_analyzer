class CommentData(object):

    def __init__(self, parser):
        self.author = None
        self.created = None
        self.comment = None
        self.likes = 0
        self.dislikes = 0

        self._get_content_data(parser)

    def _get_content_data(self, parser):
        """Searches the page for video metadata (uploaded, author, description, etc)"""

        self._parse_author(parser)
        self._parse_created(parser)
        self._parse_comment(parser)
        self._parse_likes_dislikes(parser)

        print(vars(self))

    def _parse_author(self, parser):

        author_block = parser.find('a', id="author-text")
        if author_block and author_block.span and author_block.span.string:
            author = author_block.span.string
            self.author = author.strip()

    def _parse_created(self, parser):
        header_block = parser.find('div', id="header-author")
        if header_block:
            created = header_block.find('yt-formatted-string').string
            self.created = created

    def _parse_comment(self, parser):

        comment_block = parser.find('yt-formatted-string', id='content-text')
        comment = ''

        if comment_block:

            for line in comment_block.strings:
                    simple_line = line.replace('\n', ' ')
                    comment += simple_line.strip() + ' '

            self.comment = comment

    def _parse_likes_dislikes(self, parser):

        views_block = parser.find('span', id="vote-count-middle")
        if views_block and 'aria-label' in views_block:
            likes = views_block['aria-label'].replace(' likes', '').replace(' like', '')
            self.likes = likes

    def to_json(self):

        json = {'author': self.author,
                'created': self.created,
                'comment': self.comment,
                'likes': self.likes,
                'dislikes': self.dislikes}

        return json

    def to_csv(self):

        temp = self.to_json()

        return temp
