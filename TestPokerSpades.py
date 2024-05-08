import unittest
import PokerSpades


class MyTestCase(unittest.TestCase):
    def test_check_straight_in_order(self):
        self.assertEqual(PokerSpades.check_straight("S2","S3", "S4"), 4)
    def test_check_straight_out_of_order(self):
        self.assertEqual(PokerSpades.check_straight("S3","S4", "S2"), 4)
    def test_check_straight_face_cards(self):
        self.assertEqual(PokerSpades.check_straight("SJ","SQ", "SK"), 13)
    def test_check_straight_no_straight(self):
        self.assertEqual(PokerSpades.check_straight("S2","S5", "SK"), 0)

    def test_check_3ofa_kind_true(self):
        self.assertEqual(PokerSpades.check_3ofa_kind("S2","S2", "S2"), 2)
    def test_check_3ofa_kind_true_face_cards(self):
        self.assertEqual(PokerSpades.check_3ofa_kind("SK","SK", "SK"), 13)
    def test_check_3ofa_kind_true_7(self):
        self.assertEqual(PokerSpades.check_3ofa_kind("S7","S7", "S7"), 7)
    def test_check_3ofa_kind_false_2ofa_kind(self):
        self.assertEqual(PokerSpades.check_3ofa_kind("S2","S4", "S2"), 0)
    def test_check_3ofa_kind_false_completely(self):
        self.assertEqual(PokerSpades.check_3ofa_kind("S2","S4", "S3"), 0)
    def test_check_3ofa_kind_false_face_cards(self):
        self.assertEqual(PokerSpades.check_3ofa_kind("SK","SQ", "S3"), 0)

    def test_check_royal_flush_true(self):
        self.assertEqual(PokerSpades.check_royal_flush("SK","SQ", "SA"), 14)
    def test_check_royal_flush_false_close(self):
        self.assertEqual(PokerSpades.check_royal_flush("SK","SQ", "S10"), 0)
    def test_check_royal_flush_false_straight(self):
        self.assertEqual(PokerSpades.check_royal_flush("S3","S4", "S5"), 0)


    def test_play_cards_left_wins_royal_flush(self):
        self.assertEqual(PokerSpades.play_cards("SA","SK", "SQ","S4","SJ","SQ"), -1)
    def test_play_cards_left_wins_royal_flush_over_straight(self):
        self.assertEqual(PokerSpades.play_cards("SA","SK", "SQ","S10","SJ","SQ"), -1)
    def test_play_cards_left_wins_royal_flush_over_3ofa_kind(self):
        self.assertEqual(PokerSpades.play_cards("SA","SK", "SQ","S10","S10","S10"), -1)
    def test_play_cards_right_wins_royal_flush(self):
        self.assertEqual(PokerSpades.play_cards("S10","S2","S5","SA","SK", "SQ"), 1)
    def test_play_cards_right_wins_royal_flush_over_straight(self):
        self.assertEqual(PokerSpades.play_cards("S2", "S3", "S4", "SA", "SK", "SQ"), 1)
    def test_play_cards_right_wins_royal_flush_over_3ofa_kind(self):
        self.assertEqual(PokerSpades.play_cards("S3","S3", "S3","SK","SA","SQ"), 1)
    def test_play_cards__royal_flush_draw(self):
        self.assertEqual(PokerSpades.play_cards("SA","SK","SQ","SA","SK", "SQ"), 0)

    def test_play_cards_left_straight_wins(self):
        self.assertEqual(PokerSpades.play_cards("SJ","SK","SQ","S2","S3", "SQ"), -1)
    def test_play_cards_left_higher_straight_wins(self):
        self.assertEqual(PokerSpades.play_cards("SJ","SK","SQ","S2","S3", "S4"), -1)
    def test_play_cards_left_straight_wins_over_3ofa_kind(self):
        self.assertEqual(PokerSpades.play_cards("SJ","SK","SQ","S2","S2", "S2"), -1)

    def test_play_cards_right_straight_wins(self):
        self.assertEqual(PokerSpades.play_cards("SJ","S3","SQ","S2","S3", "S4"), 1)

    def test_play_cards_right_higher_straight_wins(self):
        self.assertEqual(PokerSpades.play_cards("S2","S3","S4","S10","SJ", "SQ"), 1)

    def test_play_cards_right_straight_wins_over_3ofa_kind(self):
        self.assertEqual(PokerSpades.play_cards("SJ","SJ","SJ","S2","S3", "S4"), 1)

    def test_play_cards_straight_draw(self):
        self.assertEqual(PokerSpades.play_cards("SJ","SK","SQ","SJ","SK", "SQ"), 0)

    def test_play_cards_left_3ofa_kind_wins(self):
        self.assertEqual(PokerSpades.play_cards("SJ","SJ","SJ","S5","S6", "S2"), -1)
    def test_play_cards_left_higher_3ofa_kind_wins(self):
        self.assertEqual(PokerSpades.play_cards("SJ","SJ","SJ","S5","S5", "S5"), -1)

    def test_play_cards_right_3ofa_kind_wins(self):
        self.assertEqual(PokerSpades.play_cards("SJ","S4","S5","S5","S5", "S5"), 1)

    def test_play_cards_right_higher_3ofa_kind_wins(self):
        self.assertEqual(PokerSpades.play_cards("S3","S3","S3","S5","S5", "S5"), 1)

    def test_play_cards_3ofa_kind_draw(self):
        self.assertEqual(PokerSpades.play_cards("S3","S3","S3","S3","S3", "S3"), 0)

    def test_play_cards_no_win_draw(self):
        self.assertEqual(PokerSpades.play_cards("S5","S7","S4","S2","S5", "SJ"), 0)


if __name__ == '__main__':
    unittest.main()
