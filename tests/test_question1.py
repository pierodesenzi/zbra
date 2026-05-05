import pytest
from src.question1 import calculate_num_passwords_part1, password_follows_rules_part1, calculate_num_passwords_part2, password_follows_rules_part2


class TestPart1Rules:
    def test_all_same_digits(self):
        assert password_follows_rules_part1(222222) is True

    def test_double_and_increase(self):
        assert password_follows_rules_part1(122346) is True

    def test_decreasing_with_pair(self):
        assert password_follows_rules_part1(236775) is False

    def test_strictly_increasing_no_double(self):
        assert password_follows_rules_part1(135678) is False

    def test_double_at_end(self):
        assert password_follows_rules_part1(134599) is True

    def test_double_at_start(self):
        assert password_follows_rules_part1(112345) is True

    def test_boundary_lo(self):
        # 184759 — has a decrease (7→5), invalid
        assert password_follows_rules_part1(184759) is False

    def test_boundary_hi(self):
        # 856920 — decreases (9→2→0), invalid
        assert password_follows_rules_part1(856920) is False

    def test_answer_is_correct(self):
        assert calculate_num_passwords_part1() == 1687


class TestPart2Rules:
    def test_run_of_two(self):
        # 445555: has a run of exactly 2 (44), valid
        assert password_follows_rules_part2(445555) is True

    def test_run_of_three_invalid_if_no_other_double(self):
        # 444555: runs are 444 and 555, neither is exactly 2
        assert password_follows_rules_part2(444555) is False

    def test_all_same(self):
        assert password_follows_rules_part2(444444) is False

    def test_two_separate_doubles(self):
        # 112233: three runs of exactly 2 — valid
        assert password_follows_rules_part2(112233) is True

    def test_double_at_end(self):
        assert password_follows_rules_part2(134599) is True
        
    def test_large_run_plus_double(self):
        # 111122: run of 4 + run of 2 — the pair of 2s qualifies
        assert password_follows_rules_part2(111122) is True

    def test_double_at_start(self):
        assert password_follows_rules_part2(112345) is True

    def test_no_double(self):
        assert password_follows_rules_part2(345789) is False

    def test_decreasing(self):
        assert password_follows_rules_part2(236775) is False

    def test_run_of_exactly_two_among_larger_runs(self):
        # 122333: run of 1, run of 2 (22), run of 3 (333) — the 22 qualifies
        assert password_follows_rules_part2(122333) is True

    def test_answer_is_correct(self):
        assert calculate_num_passwords_part2() == 1148