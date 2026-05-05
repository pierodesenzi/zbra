import pytest
from src.question2 import solve_address


def write_commands(tmp_path, commands: list[str]) -> str:
    """Helper: write a list of commands to a temp file, return its path."""
    p = tmp_path / "commands.txt"
    p.write_text("\n".join(commands))
    return str(p)


class TestNoOp:
    def test_single_noop(self, tmp_path):
        assert solve_address(write_commands(tmp_path, ["25"])) == 0

    def test_all_noops(self, tmp_path):
        assert solve_address(write_commands(tmp_path, ["25", "99", "402"])) == 0


class TestAdd:
    def test_single_add(self, tmp_path):
        assert solve_address(write_commands(tmp_path, ["201"])) == 1

    def test_add_double_digit(self, tmp_path):
        assert solve_address(write_commands(tmp_path, ["2010"])) == 10

    def test_multiple_adds(self, tmp_path):
        assert solve_address(write_commands(tmp_path, ["201", "202", "205"])) == 8

    def test_add_zero(self, tmp_path):
        # "200" → add 0, valid edge case
        assert solve_address(write_commands(tmp_path, ["200"])) == 0


class TestJump:
    def test_jump_skips_add(self, tmp_path):
        # 52 skips 1 line (203), lands on 201
        cmds = ["52", "203", "201"]
        assert solve_address(write_commands(tmp_path, cmds)) == 1

    def test_jump_of_one_executes_next(self, tmp_path):
        # 51 skips 0 extra lines, so 201 runs normally
        cmds = ["51", "201"]
        assert solve_address(write_commands(tmp_path, cmds)) == 1

    def test_jump_past_end_is_safe(self, tmp_path):
        # 510 jumps well beyond the file — should terminate cleanly
        cmds = ["510", "201", "201"]
        assert solve_address(write_commands(tmp_path, cmds)) == 0


class TestProvidedExample:
    def test_example(self, tmp_path):
        cmds = ["25", "52", "53", "202", "54", "402", "203", "510", "201"]
        assert solve_address(write_commands(tmp_path, cmds)) == 3


class TestEdgeCases:
    def test_empty_file(self, tmp_path):
        assert solve_address(write_commands(tmp_path, [])) == 0

    def test_single_add_at_end_after_jump(self, tmp_path):
        # jump lands exactly on the last line
        cmds = ["52", "999", "205"]
        assert solve_address(write_commands(tmp_path, cmds)) == 5

    def test_consecutive_jumps(self, tmp_path):
        # 52 skips 203, lands on 53; 53 skips 201 and 201, lands on 205
        cmds = ["52", "203", "53", "201", "201", "205"]
        assert solve_address(write_commands(tmp_path, cmds)) == 5