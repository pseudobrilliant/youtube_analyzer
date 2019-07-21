import argparse
from bs4 import BeautifulSoup as soup
from src.parser.video_metadata import VideoMetadata
from src.parser.comment_data import CommentData
import json


class CommentParser(object):

    def __init__(self, source):

        parser = soup(source, "html5lib")

        self.video_metadata = VideoMetadata(parser)

        self.comments = []

        self._parse_comments(parser)

    def _parse_comments(self, parser):

        comment_blocks = parser.find_all('div', id ='main', class_='ytd-comment-renderer')

        for blk in comment_blocks:

            comment = CommentData(blk)
            if comment.author is not None and comment.author != '':
                self.comments.append(comment)

        print(len(self.comments))

    def to_json(self):

        json = {}

        json['metadata'] = self.video_metadata.to_json()

        json['comments'] = []

        for c in self.comments:

            json['comments'].append(c.to_json())

        return json

    def export_json(self, path):

        with open(path, 'w') as flh:
            json.dump(self.to_json(), flh)

    def comments_to_csv(self):

        csv_list = []

        for c in self.comments:

            csv_list.append(c.to_csv())

        return csv_list

    def export_comments_csv(self, path):

        import csv

        with open(path, 'w') as flh:
            csv_list = self.comments_to_csv()
            headers = sorted(list(csv_list[0]))
            writer = csv.DictWriter(flh, fieldnames=headers)
            writer.writeheader()

            writer.writerows(self.comments_to_csv())


if __name__ == '__main__':

    arg_parser = argparse.ArgumentParser(description='Parse html source for video metadata and comments')
    arg_parser.add_argument('--name', type=str, help='name of video page stored in data folder.', required=True)

    args = arg_parser.parse_args()

    with open('../../data/{}_source.html'.format(args.name), 'r') as flh:

        content = flh.read()
        cp = CommentParser(content)
        cp.export_json('../../data/{}_parsed.json'.format(args.name))
        cp.export_comments_csv('../../data/{}_comments.csv'.format(args.name))
