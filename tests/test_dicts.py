from utils import dicts


def test_dicts():
    assert dicts.get_val({"vcs": "mercurial"}, "vcs") == "mercurial"
    assert dicts.get_val({}, "vcs", "git") == "git"
