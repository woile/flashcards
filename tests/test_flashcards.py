import unittest
from flashcards import flashcards


class TestFlashcard(unittest.TestCase):

    def setUp(self):
        self.topic = "Dolor sit amet"
        self.short_content = "I am a short content"
        self.long_content = ("I am a very long content, I'm used to test, that "
                             "does not look like "
                             "a really meaningful purpose but Im okay with "
                             "that, I'm the best content there "
                             "is and no one will be better than me. "
                             "This actually has to be a bit longer, so I'll "
                             "just write first thing that pops in my "
                             "mind, hu? what do you think about that? "
                             "I guess you din't think at all about what "
                             "I'm thinking.")
        self.keywords = "lorem, ipsum, pretium"
        self.fc_short = flashcards.Flashcard(topic=self.topic,
                                             content=self.short_content)
        self.fc_long = flashcards.Flashcard(topic=self.topic,
                                            content=self.long_content,
                                            keywords=self.keywords)

    def test_format_raw_lower_than_max(self):
        format_content = self.fc_short.format_raw(self.short_content,
                                                  len(self.short_content) + 10)
        # import ipdb; ipdb.set_trace()
        self.assertEqual(len(format_content), 1)

    def test_format_raw_not_lower_than_max(self):
        format_content = self.fc_short.format_raw(self.short_content,
                                                  len(self.short_content) - 2)
        self.assertNotEqual(len(format_content), 3)

    def test_get_topic(self):
        topic_parsed = self.fc_short.get_topic()
        self.assertEqual(len(topic_parsed), 3)

    def test_get_short_content_height_equal_to_minimum(self):
        self.fc_short.hide_content = False
        content_parsed = self.fc_short.get_content(self.short_content)
        self.assertEqual(len(content_parsed), self.fc_short.min_content_height)

    def test_get_long_content(self):
        self.fc_long.hide_content = False
        content_parsed = self.fc_long.get_content(self.long_content)
        self.assertEqual(len(content_parsed), 8)

    def test_get_keywords(self):
        keywords_parsed = self.fc_long.get_keywords()
        self.assertEqual(len(keywords_parsed), 3)

    def test_get_lines_to_draw(self):
        get_lines_to_draw = self.fc_short.get_lines_to_draw()
        self.assertEqual(len(get_lines_to_draw), 14)

    def test_get_lines_to_draw_with_placeholder(self):
        get_lines_to_draw = self.fc_short.get_lines_to_draw(
            show_placeholder=True)
        self.assertEqual(len(get_lines_to_draw), 14)


if __name__ == '__main__':
    unittest.main()
