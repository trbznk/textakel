import unittest
import textakel


class TestApi(unittest.TestCase):

    def test_get_function(self):
        function_name = "title"
        function = textakel.get_function(function_name)
        s = function("textakel")
        self.assertEqual(s, "Textakel")

    def test_get_functions(self):
        function_names = textakel.get_functions()
        self.assertTrue(len(function_names) > 1)

    def test_takel(self):
        function_name = "upper"
        s = textakel.takel(function_name, "textakel")
        self.assertEqual(s, "TEXTAKEL")


class TestFunctions(unittest.TestCase):

    def test_alphabetical(self):
        s = textakel.alphabetical("Textakel is fine, right?")
        self.assertEqual(s, "   ,?Taeeefghiiiklnrsttx")

    def test_capitalize(self):
        s = textakel.capitalize("textakel developed in germany")
        self.assertEqual(s, "Textakel developed in germany")

    def test_casefold(self):
        s = textakel.casefold("Thiß iß aweßome")
        self.assertEqual(s, "thiss iss awessome")

    def test_count_multiples(self):
        s = textakel.count_multiples("Texxtakelll is      wonderfull")
        self.assertEqual(s, "Te2xtake3l is6 wonderfu2l")

    def test_lower(self):
        s = textakel.lower("Textakel Is Nice")
        self.assertEqual(s, "textakel is nice")

    def test_stretch(self):
        s = textakel.stretch("Textakel")
        self.assertEqual(s, "T e x t a k e l")

    def test_swapcase(self):
        s = textakel.swapcase("Textakel Is Nice")
        self.assertEqual(s, "tEXTAKEL iS nICE")

    def test_swap_pairs(self):
        s1 = textakel.swap_pairs("textakel")
        s2 = textakel.swap_pairs("tx")
        s3 = textakel.swap_pairs("t")
        s4 = textakel.swap_pairs("textake")
        self.assertEqual(s1, "ettxkale")
        self.assertEqual(s2, "xt")
        self.assertEqual(s3, "t")
        self.assertEqual(s4, "ettxkae")

    def test_swap_umlaut(self):
        s = textakel.swap_umlaut("ä ö ü Ä Ö Ü")
        self.assertEqual(s, "ae oe ue Ae Oe Ue")

    def test_title(self):
        s = textakel.title("textakel is nice")
        self.assertEqual(s, "Textakel Is Nice")

    def test_remove_consonant(self):
        s = textakel.remove_consonant("Textakel is nice")
        self.assertEqual(s, "eae i ie")

    def test_remove_digit(self):
        s = textakel.remove_digit("eins1 zwei2 drei3 vier4")
        self.assertEqual(s, "eins zwei drei vier")

    def test_remove_letter(self):
        s = textakel.remove_letter("eins1 zwei2 drei3 ßechß4")
        self.assertEqual(s, "1 2 3 4")

    def test_remove_punctuation(self):
        s = textakel.remove_punctuation("1!34$5%6&7/8(9)0=")
        self.assertEqual(s, "134567890")

    def test_remove_space(self):
        s = textakel.remove_space("1 2 3 4 5 6 7 8 9")
        self.assertEqual(s, "123456789")

    def test_remove_vowel(self):
        s = textakel.remove_vowel("Textakel Is nice")
        self.assertEqual(s, "Txtkl s nc")

    def test_reverse(self):
        s = textakel.reverse("Textakel Is Nice!")
        self.assertEqual(s, "!eciN sI lekatxeT")

    def test_rot13(self):
        s = textakel.rot13("HeLlO")
        self.assertEqual(s, "UrYyB")

    def test_upper(self):
        s = textakel.upper("Textakel is nice")
        self.assertEqual(s, "TEXTAKEL IS NICE")


def main():
    unittest.main()


if __name__ == "__main__":
    main()
